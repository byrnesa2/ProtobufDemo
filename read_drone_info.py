import interface_values_pb2
import sys

def ListDrones(map_info):
   for drone in map_info.droneinfo:
      for location in drone.location:
         x = location.xcoord
         y = location.ycoord
      for bounds in drone.searcharea:
         upper_b = bounds.upperbound
         left_b = bounds.leftbound
         lower_b = bounds.lowerbound
         right_b = bounds.rightbound
      print("Drone Name: %s" % drone.name)
      print("Coordinates: (%d,%d)" % (x,y))
      print("Boundary Box: (%d,%d,%d,%d)" % (upper_b, left_b, lower_b, right_b))

map_info = interface_values_pb2.MapInfo()
f = open(sys.argv[1], "rb")
map_info.ParseFromString(f.read())
f.close()

ListDrones(map_info)
