import enum


class MSG_ID(enum.IntEnum):
    NONE = 0
    STATE_PLAYER = 1
    STATE_NPC = 2


class MSG:
    def __init__(self, id=MSG_ID.NONE, msg=None):
        self.id = id
        self.msg = msg

    def pack(self):
        return [self.id, self.msg.pack()]

    def unpack(self, data):
        self.id = MSG_ID(data[0])
        if self.id == MSG_ID.NONE:
            self.msg = None
        elif self.id == MSG_ID.STATE_PLAYER:
            self.msg = STATE_PLAYER()
        elif self.id == MSG_ID.STATE_NPC:
            self.msg = STATE_NPC()
        self.msg.unpack(data[1])

    def __dict__(self):
        return {"id": self.id,
                "msg": self.msg.__dict__()}

    def __str__(self):
        return str(self.__dict__())


class STATE_PLAYER:
    def __init__(self, id=0, name="", health=0):
        self.id = id
        self.name = name
        self.health = health

    def pack(self):
        return [self.id, self.name, self.health]

    def unpack(self, data):
        self.id = data[0]
        self.name = data[1]
        self.health = data[2]

    def __dict__(self):
        return {"id": self.id,
                "name": self.name,
                "health": self.health}

    def __str__(self):
        return str(self.__dict__())


class STATE_NPC:
    def __init__(self, id=0, name="", health=0, strength=0):
        self.id = id
        self.name = name
        self.health = health
        self.strength = strength

    def pack(self):
        return [self.id, self.name, self.health, self.strength]

    def unpack(self, data):
        self.id = data[0]
        self.name = data[1]
        self.health = data[2]
        self.strength = data[3]

    def __dict__(self):
        return {"id": self.id,
                "name": self.name,
                "health": self.health,
                "strength": self.strength}

    def __str__(self):
        return str(self.__dict__())
