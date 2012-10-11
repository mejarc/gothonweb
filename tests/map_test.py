from nose.tools import *
from gothonweb.map import *

def test_room(): #note there isn't a parameter, not even self
    gold = Room("Name is GoldRoom", 
                """Here's the description: room has gold in it. There's a door to the north.""")
    assert_equal(gold.name, "Name is GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center")
    north = Room("North", "Test room, north") #creating a room, using its name and description
    south = Room("South", "Test room- south!")
    
    center.add_paths({'north':north, 'south': south})
    assert_equal(center.go("north"), north)
    assert_equal(center.go("south"), south)

def test_map(): #the tests seem to self-execute. "Print" doesn't print?
    start = Room("Start", "you can go west, then down a hole")
    west = Room("Trees", "trees here--go east")
    down = Room("Dungeon", "Dark here; go up")
    
    start.add_paths({"west": west, "down": down})
    west.add_paths({"east": start})
    down.add_paths({"up": start})
     
    assert_equal(start.go("west"), west)
    assert_equal(start.go("west").go("east"), start) # chaining!!
    assert_equal(start.go("down").go("up"), start)
    
    assert_equals(west.go("east"), start) #why not??

def test_gothon_game_map():
    assert_equal(START.go("shoot!"), vocal_death)
    assert_equal(START.go("dodge!"), vocal_death)
    
    room = START.go("tell a joke")
    assert_equal(room, laser_weapon_armory)