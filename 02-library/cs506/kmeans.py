from collections import defaultdict
from math import inf
import random
import csv
from cs506 import sim


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    len_pts = len_points
    # list comp for summing and returning point
    avg_point = [sum(point[index] for point in points) / len_pts for index in range(len(points[0]))]
    return avg_point


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    k = max(assignments) + 1
    # list comp for clusters
    clusters = [[val for index, val in enumerate(dataset) if assignments[index] == index_k] for index_k in range(k)]
    # centers for clusters
    return_centers = [point_avg(cluster) for cluster in clusters]
    return return_centers


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    # using sim.euclidean_dist
    euclid_dist = sim.euclidean_dist(a, b)
    return euclid_dist


def distance_squared(a, b):
    d_squared = distance(a, b) ** 2
    return d_squared


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    len_dataset = len(dataset)
    list_of_indices = list(range(len_dataset))
    # apply random.shuffle to the indices to return random k points
    random.shuffle(list_of_indices)
    return [dataset[index] for index in list_of_indices[:k]]


def cost_function(clustering):
    # creating dictionary for centers
    centers = {center: point_avg(clustering[center]) for center in clustering.keys()}
    # using dictionary to access values and sum them for the cost function
    cost_function_return = sum( sum(distance_squared(index, centers[center]) for index in clustering[center]) for center in clustering.keys() )
    return cost_function_return


def return_min_distance(centroids, point):
    """ 
    function that finds the minimum distance
    between a point and all centroids to determine
    which centroid it should be clusterd to in 
    generate_k_pp
    """
    min_distance = min(distance(point, centroid) for centroid in centroids)
    return min_distance


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    list_centroids = [dataset[random.randint(0, len(dataset) - 1)]]
    # for loop to loop through k times 
    for ind in range(k):
        # creating an lc to hold the distances
        list_distances = [return_min_distance(list_centroids, point) for point in dataset]
        maximum_distance = max(list_distances)
        # finding index of the max distance
        index_max_dist = list_distances.index(maximum_distance)
        # appending the array with the max distance to centroids
        list_centroids.append(dataset[maximum_distance])
    return list_centroids


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
