sudo apt-get install libzmq3-dev libmsgpack-dev

g++ -o UEMPS UEMPS.cpp -lzmq -lmsgpackc
g++ -o UEMPC UEMPC.cpp -lzmq -lmsgpackc
mkdir -p build/
mv UEMPS build/UEMPS
mv UEMPC build/UEMPC