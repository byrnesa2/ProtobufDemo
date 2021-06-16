#include <fstream>
#include <string>
#include "interface-values.pb.h"
using namespace std;

int main(int argc, char* argv[]){
string drone1_name = "Drone 1";
//location: {x,y}, assume upper right corner of screen is {0,0}, x moves right, y moves down
int drone1_loc[2] = {0,0};
//boundary order: up, left, down, right
int drone1_bounds[4] = {0,0,50,50};

string drone2_name = "Drone 2";
int drone2_loc[2] = {50,0};
int drone2_bounds[4] = {0,50,50,100};

string drone3_name = "Drone 3";
int drone3_loc[2] = {0,50};
int drone3_bounds[4] = {50,0,100,50};

string drone4_name = "Drone 4";
int drone4_loc[2] = {50,50};
int drone4_bounds[4] = {50,50,100,100};

interfacevalues::MapInfo map_info;
interfacevalues::DroneInfo* drone1_info = map_info.add_droneinfo();
interfacevalues::DroneInfo::Location* drone1_location  = drone1_info->add_location();
interfacevalues::DroneInfo::SearchArea* drone1_search_area = drone1_info->add_searcharea();
interfacevalues::DroneInfo* drone2_info = map_info.add_droneinfo();
interfacevalues::DroneInfo::Location* drone2_location  = drone2_info->add_location();
interfacevalues::DroneInfo::SearchArea* drone2_search_area = drone2_info->add_searcharea();
interfacevalues::DroneInfo* drone3_info = map_info.add_droneinfo();
interfacevalues::DroneInfo::Location* drone3_location  = drone3_info->add_location();
interfacevalues::DroneInfo::SearchArea* drone3_search_area = drone3_info->add_searcharea();
interfacevalues::DroneInfo* drone4_info = map_info.add_droneinfo();
interfacevalues::DroneInfo::Location* drone4_location  = drone4_info->add_location();
interfacevalues::DroneInfo::SearchArea* drone4_search_area = drone4_info->add_searcharea();


drone1_info->set_name(drone1_name);
drone1_location->set_xcoord(drone1_loc[0]);
drone1_location->set_ycoord(drone1_loc[1]);
drone1_search_area->set_upperbound(drone1_bounds[0]);
drone1_search_area->set_leftbound(drone1_bounds[1]);
drone1_search_area->set_lowerbound(drone1_bounds[2]);
drone1_search_area->set_rightbound(drone1_bounds[3]);

drone2_info->set_name(drone2_name);
drone2_location->set_xcoord(drone2_loc[0]);
drone2_location->set_ycoord(drone2_loc[1]);
drone2_search_area->set_upperbound(drone2_bounds[0]);
drone2_search_area->set_leftbound(drone2_bounds[1]);
drone2_search_area->set_lowerbound(drone2_bounds[2]);
drone2_search_area->set_rightbound(drone2_bounds[3]);

drone3_info->set_name(drone3_name);
drone3_location->set_xcoord(drone3_loc[0]);
drone3_location->set_ycoord(drone3_loc[1]);
drone3_search_area->set_upperbound(drone3_bounds[0]);
drone3_search_area->set_leftbound(drone3_bounds[1]);
drone3_search_area->set_lowerbound(drone3_bounds[2]);
drone3_search_area->set_rightbound(drone3_bounds[3]);

drone4_info->set_name(drone4_name);
drone4_location->set_xcoord(drone4_loc[0]);
drone4_location->set_ycoord(drone4_loc[1]);
drone4_search_area->set_upperbound(drone4_bounds[0]);
drone4_search_area->set_leftbound(drone4_bounds[1]);
drone4_search_area->set_lowerbound(drone4_bounds[2]);
drone4_search_area->set_rightbound(drone4_bounds[3]);



{
    // Read the existing address book.
    fstream input(argv[1], ios::in | ios::binary);
    if (!input) {
      cout << argv[1] << ": File not found.  Creating a new file." << endl;
    } else if (!map_info.ParseFromIstream(&input)) {
      cerr << "Failed to parse address book." << endl;
      return -1;
    }
  }


{
fstream output(argv[1], ios::out | ios::trunc | ios::binary);
if (!map_info.SerializeToOstream(&output)) {
      cerr << "Failed to write info." << endl;
      return -1;
    }
}

return 0;

}



