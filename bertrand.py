import random
import math

# Utility functions

def test_radius_of_point(point):
    length = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
    return length

'''
Point1 and Point2 should be tuples in the form of (x,y)
'''
def get_chord_length(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    return math.sqrt(math.pow(x,2) + math.pow(y,2))

# Functions for First Method

'''
We choose a point on a unit circle randomly. 
We return a tuple in the form of (x, y)
'''
def get_random_point():
    degrees = random.random() * math.pi  * 2
    x = 1 * math.sin(degrees) 
    y = 1 * math.cos(degrees)
    return (x,y)

'''
The two points just have to be on the unit circle
'''
def get_chord_method_one():
    point1 = get_random_point()
    point2 = get_random_point()
    return (point1, point2)

def get_length_method_one():
    chord = get_chord_method_one()
    return get_chord_length(chord[0], chord[1])

# Functions for Second Method

'''
This will choose a radius length and then calculate the 
position of the points based off this radius and the unit circle
Note that the default angle here is pi/2 or 90 degrees, meaning that 
all the points chosen will be based off chords in line with the x-axis.
Later we rotate these chords around the circle in order to get randomness
in the x-y plane as well
'''
def get_points_from_radius():
    radius = random.random()
    xAxisDist = math.sqrt(1 - math.pow(radius, 2))
    point1 = (xAxisDist, radius)
    point2 = (-xAxisDist, radius) 
    return (point1, point2)


'''
We use a rotation matrix to rotate the points in the x-y axis.
point1 and point2 should be in the form of (x,y)
'''
def rotate_points(point1, point2):
    angleToRotate = random.random() * math.tau
    
    # Just making it easier to read
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]   
    y2 = point2[1]

    xn1 = x1 * math.cos(angleToRotate) - y1 * math.sin(angleToRotate)
    yn1 = x1 * math.sin(angleToRotate) + y1 * math.cos(angleToRotate)
    
    xn2 = x2 * math.cos(angleToRotate) - y2 * math.sin(angleToRotate)
    yn2 = x2 * math.sin(angleToRotate) + y2 * math.cos(angleToRotate)

    point1 = (xn1, yn1)
    point2 = (xn2, yn2)
    return (point1, point2)

def get_chord_method_two():
    points = get_points_from_radius()
    points = rotate_points(points[0], points[1])
    return points

def get_length_method_two():
    points = get_chord_method_two()
    return get_chord_length(points[0], points[1])

# Functions for Third Method

def add_cartesian_points(point1, point2):
    x = point1[0] + point2[0]
    y = point1[1] + point2[1]
    return (x,y)

def polar_to_cartesian_coordinates(length, angle):
    x = length * math.cos(angle)
    y = length * math.sin(angle)
    return (x, y)

def cartesian_to_polar_coordinates(x, y):
    length = math.sqrt(math.pow(x,2) + math.pow(y,2))
    angle = math.atan2(y,x)
    return (length, angle)
'''
Chooses the midpoint of a chord in the form of (length, angle)
'''
def choose_midpoint():
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    # Check if the point is outside the circle
    while(math.sqrt(math.pow(x,2) + math.pow(y,2)) > 1):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
    midpoint = cartesian_to_polar_coordinates(x, y)
    return midpoint

'''
You input a point in polar coordinates.
This point is the midpoint of the chord you will construct intersecting
the unit circle.
'''
def get_chord_from_midpoint(length, angle):
    midpointCartesian = polar_to_cartesian_coordinates(length, angle)
    halfChordLength = math.sqrt(1 - math.pow(length, 2))
    '''
    After we have the center of the chord we simply find the points of the chord
    by adding the halfChordLength as a polar coordinate with an angle 
    of +pi/2 and -pi/2 for each point respectively.
    ''' 
    halfChordNegative = polar_to_cartesian_coordinates(halfChordLength, angle - (math.pi / 2))
    halfChordPositive = polar_to_cartesian_coordinates(halfChordLength, angle + (math.pi / 2))
    point1 = add_cartesian_points(midpointCartesian, halfChordNegative)
    point2 = add_cartesian_points(midpointCartesian, halfChordPositive)
    return (point1, point2)

def get_chord_method_three():
    midpoint = choose_midpoint()
    chord = get_chord_from_midpoint(midpoint[0], midpoint[1])
    return chord

def get_length_method_three():
    points = get_chord_method_three()
    length = get_chord_length(points[0], points[1])
    return length

def main():
    
    triSideLength = math.sqrt(3)

    times = 100000
    count = 0
    for i in range(times):
        length = get_length_method_three()
        if(length > triSideLength):
            count += 1

    print(count/times)



if __name__ == "__main__":
    main()
    