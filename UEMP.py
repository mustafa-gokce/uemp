import enum


class MSG_ID(enum.IntEnum):
    MSG_ID_NONE = 0
    MSG_ID_USER = 1
    MSG_ID_NPC = 2


class MSG:
    def __init__(self, msg_id=MSG_ID.MSG_ID_NONE, msg=None):
        self.msg_id = msg_id
        self.msg = msg

    def pack(self):
        return [self.msg_id, self.msg.pack()]

    def unpack(self, data):
        self.msg_id = MSG_ID(data[0])
        if self.msg_id == MSG_ID.MSG_ID_NONE:
            self.msg = None
        elif self.msg_id == MSG_ID.MSG_ID_USER:
            self.msg = MSG_USER()
        elif self.msg_id == MSG_ID.MSG_ID_NPC:
            self.msg = MSG_NPC()
        self.msg.unpack(data[1])

    def __dict__(self):
        return {"msg_id": self.msg_id,
                "msg": self.msg.__dict__()}

    def __str__(self):
        return str(self.__dict__())


class MSG_USER:
    def __init__(self, usr_id=0, usr_name="", usr_health=0):
        self.usr_id = usr_id
        self.usr_name = usr_name
        self.usr_health = usr_health

    def pack(self):
        return [self.usr_id, self.usr_name, self.usr_health]

    def unpack(self, data):
        self.usr_id = data[0]
        self.usr_name = data[1]
        self.usr_health = data[2]

    def __dict__(self):
        return {"usr_id": self.usr_id,
                "usr_name": self.usr_name,
                "usr_health": self.usr_health}

    def __str__(self):
        return str(self.__dict__())


class MSG_NPC:
    def __init__(self, npc_id=0, npc_name="", npc_health=0, npc_strength=0):
        self.npc_id = npc_id
        self.npc_name = npc_name
        self.npc_health = npc_health
        self.npc_strength = npc_strength

    def pack(self):
        return [self.npc_id, self.npc_name, self.npc_health, self.npc_strength]

    def unpack(self, data):
        self.npc_id = data[0]
        self.npc_name = data[1]
        self.npc_health = data[2]
        self.npc_strength = data[3]

    def __dict__(self):
        return {"npc_id": self.npc_id,
                "npc_name": self.npc_name,
                "npc_health": self.npc_health,
                "npc_strength": self.npc_strength}

    def __str__(self):
        return str(self.__dict__())
