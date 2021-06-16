import interface_values_pb2
import sys
import os


drone1_name = "Drone 1"
#location: [x,y], assume upper right corner of screen is [0,0}, x moves right, y moves down
drone1_loc = [0,0]
#boundary order: up, left, down, right
drone1_bounds = [0,0,50,50]

drone2_name = "Drone 2"
drone2_loc = [50,0]
drone2_bounds = [0,50,50,100]

drone3_name = "Drone 3"
drone3_loc = [0,50]
drone3_bounds = [50,0,100,50]

drone4_name = "Drone 4"
drone4_loc = [50,50]
drone4_bounds = [50,50,100,100]

map_info = interface_values_pb2.MapInfo()


# Read the existing address book.
try:
   f = open(sys.argv[1], "rb")
   map_info.ParseFromString(f.read())
   f.close()
   map_info.Clear() #clear all old values to overwrite
except IOError:
   print sys.argv[1] + ": Could not open file.  Creating a new one."

drone1 = map_info.droneinfo.add()
drone1.name = drone1_name
drone1_location = drone1.location.add()
drone1_location.xcoord = drone1_loc[0]
drone1_location.ycoord = drone1_loc[1]
drone1_boundaries = drone1.searcharea.add()
drone1_boundaries.upperbound = drone1_bounds[0]
drone1_boundaries.leftbound = drone1_bounds[1]
drone1_boundaries.lowerbound = drone1_bounds[2]
drone1_boundaries.rightbound = drone1_bounds[3]

drone2 = map_info.droneinfo.add()
drone2.name = drone2_name
drone2_location = drone2.location.add()
drone2_location.xcoord = drone2_loc[0]
drone2_location.ycoord = drone2_loc[1]
drone2_boundaries = drone2.searcharea.add()
drone2_boundaries.upperbound = drone2_bounds[0]
drone2_boundaries.leftbound = drone2_bounds[1]
drone2_boundaries.lowerbound = drone2_bounds[2]
drone2_boundaries.rightbound = drone2_bounds[3]

drone3 = map_info.droneinfo.add()
drone3.name = drone3_name
drone3_location = drone3.location.add()
drone3_location.xcoord = drone3_loc[0]
drone3_location.ycoord = drone3_loc[1]
drone3_boundaries = drone3.searcharea.add()
drone3_boundaries.upperbound = drone3_bounds[0]
drone3_boundaries.leftbound = drone3_bounds[1]
drone3_boundaries.lowerbound = drone3_bounds[2]
drone3_boundaries.rightbound = drone3_bounds[3]

drone4 = map_info.droneinfo.add()
drone4.name = drone4_name
drone4_location = drone4.location.add()
drone4_location.xcoord = drone4_loc[0]
drone4_location.ycoord = drone4_loc[1]

drone4_boundaries = drone4.searcharea.add()
drone4_boundaries.upperbound = drone4_bounds[0]
drone4_boundaries.leftbound = drone4_bounds[1]
drone4_boundaries.lowerbound = drone4_bounds[2]
drone4_boundaries.rightbound = drone4_bounds[3]

f = open(sys.argv[1], "wb")
f.write(map_info.SerializeToString())
f.close()

