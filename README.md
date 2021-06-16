#Installation
Follow C++ installation instructions [here](https://github.com/protocolbuffers/protobuf/tree/master/src).
Follow Python installation instructions [here](https://github.com/protocolbuffers/protobuf/tree/master/python)

#Compiling Protocol Buffers

To compile your Python C++ protocol buffers in current directory (Already done, no need to do this):
`protoc --python_out=$PWD interface-values.proto`

To compile your C++ protocol buffers in current directory (Already done, no need to do this):
`protoc --cpp_out=$PWD interface-values.proto`

#Writing from C++ and reading from Python


To write info to drone file:
``c++ -std=c++11 write_drone_info.cc interface-values.pb.cc -o write_drone_info_cpp `pkg-config --cflags --libs protobuf` ``
`./write_drone_info_cpp drone_info.data`

To read info from drone file:
`python read_drone_info.py drone_info.data`

#Writing from Python and reading from C++ (Have yet to add these files)

To write info to drone file:
`python write_drone_info.py drone_info.data`

To read info from drone file:
``c++ -std=c++11 read_drone_info.cc interface-values.pb.cc -o read_drone_info_cpp `pkg-config --cflags --libs protobuf` ``
`./read_drone_info_cpp drone_info.data`
