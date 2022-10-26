g++ -o UEMPS UEMPS.cpp -lzmq -lmsgpackc -lboost_filesystem -lrestbed
g++ -o UEMPC UEMPC.cpp -lzmq -lmsgpackc -lboost_filesystem -lrestbed
mkdir -p build/
mv UEMPS build/UEMPS
mv UEMPC build/UEMPC