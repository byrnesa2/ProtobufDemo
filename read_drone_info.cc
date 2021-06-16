#include <fstream>

#include <iostream>
#include <string>

#include "interface-values.pb.h"

using namespace std;


// Iterates though all Drones in the interface values and prints info about them.
void ListDrones(const interfacevalues::MapInfo& map_info) {
  for (int i = 0; i < map_info.droneinfo_size(); i++) {
    const interfacevalues::DroneInfo& drone = map_info.droneinfo(i);

    cout << "drone ID: " << drone.name() << endl;


    for (int j = 0; j < drone.location_size(); j++) {
      const interfacevalues::DroneInfo::Location& loc = drone.location(j);
	 cout << "Location: (" << loc.xcoord() << "," << loc.ycoord() << ")" << endl;
     }

    for (int j = 0; j < drone.searcharea_size(); j++) {
      const interfacevalues::DroneInfo::SearchArea& bounds = drone.searcharea(j);
	cout << "Boundary Box: [" << bounds.upperbound() << " " << bounds.leftbound() << " " << bounds.lowerbound() << " " << bounds.rightbound() << "]" << endl;

     }
}
}

// Main function:  Reads the entire map info from a file and prints all
//   the information inside.
int main(int argc, char* argv[]) {
  // Verify that the version of the library that we linked against is
  // compatible with the version of the headers we compiled against.
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  if (argc != 2) {
    cerr << "Usage:  " << argv[0] << " map_info_FILE" << endl;
    return -1;
  }

  interfacevalues::MapInfo map_info;

  {
    // Read the existing map info.
    fstream input(argv[1], ios::in | ios::binary);
    if (!map_info.ParseFromIstream(&input)) {
      cerr << "Failed to parse map info." << endl;
      return -1;
    }
  }

  ListDrones(map_info);


  return 0;
}
