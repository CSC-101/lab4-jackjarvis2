import math
import data  # Assuming 'data' contains the Point class

# Part 1
def first_element(nested_list: list[list[int]]) -> list[int]:
    """
    Purpose:
    Extract the first element from each nested list within a given list of lists.
    Ignores any nested empty lists.

    Input:
    A list of lists of integers (list[list[int]]).

    Output:
    A list of integers containing the first elements of the non-empty nested lists.
    """
    return [sublist[0] for sublist in nested_list if sublist]  # Filter and map

def run_tests_part1():
    # Test case 1
    assert first_element([[1, 2], [3, 4], [], [5]]) == [1, 3, 5], "Test case 1 failed"
    # Test case 2
    assert first_element([[], [10, 20], [], [30]]) == [10, 30], "Test case 2 failed"

# Part 2
def x_coordinates(points: list[data.Point]) -> list[int]:
    """
    Purpose:
    Extract the x-coordinates from a list of Point objects.

    Input:
    A list of Point objects (list[Point]).

    Output:
    A list of integers representing the x-coordinates of the points.
    """
    return [point.x for point in points]

def run_tests_part2():
    p1 = data.Point(1, 2)
    p2 = data.Point(3, 4)
    assert x_coordinates([p1, p2]) == [1, 3], "Test case for x_coordinates failed"

# Part 3
def are_in_positive_quadrant(points: list[data.Point]) -> list[data.Point]:
    """
    Purpose:
    Determine which points are in the positive quadrant (x > 0 and y > 0).

    Input:
    A list of Point objects (list[Point]).

    Output:
    A list of Point objects that are in the positive quadrant.
    """
    return [point for point in points if point.x > 0 and point.y > 0]

def run_tests_part3():
    p1 = data.Point(1, 2)
    p2 = data.Point(-1, -1)
    p3 = data.Point(3, 4)
    assert are_in_positive_quadrant([p1, p2, p3]) == [p1, p3], "Test case for are_in_positive_quadrant failed"

# Part 4
def distance(point1: data.Point, point2: data.Point) -> float:
    """
    Purpose:
    Calculate the Euclidean distance between two points.

    Input:
    Two Point objects.

    Output:
    A float representing the distance between the two points.
    """
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

def run_tests_part4():
    p1 = data.Point(1, 1)
    p2 = data.Point(4, 5)
    assert distance(p1, p2) == 5.0, "Test case for distance failed"

# Part 5
def manhattan_distance(point1: data.Point, point2: data.Point) -> float:
    """
    Purpose:
    Calculate the Manhattan distance between two points.

    Input:
    Two Point objects.

    Output:
    A float representing the Manhattan distance between the two points.
    """
    return abs(point2.x - point1.x) + abs(point2.y - point1.y)

def run_tests_part5():
    p1 = data.Point(1, 2)
    p2 = data.Point(4, 6)
    assert manhattan_distance(p1, p2) == 7, "Test case for manhattan_distance failed"

# Part 6
def distance_all(point1: data.Point, point2: data.Point) -> float:
    """
    Purpose:
    Calculate the distance between two points (duplicate of the distance function).

    Input:
    Two Point objects.

    Output:
    A float representing the distance between the two points.
    """
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

# Run all tests
if __name__ == "__main__":
    run_tests_part1()
    run_tests_part2()
    run_tests_part3()
    run_tests_part4()
    run_tests_part5()
    print("All tests passed!")
