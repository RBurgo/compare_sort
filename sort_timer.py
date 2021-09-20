# Author: Richard Burgo
# Description: creates a decorator function to time the bubble and insertion sorts and then graphs them

import time
import random
from matplotlib import pyplot
from functools import wraps


def sort_timer(func):
    """
    times how long it takes for a function to run
    :param func: the function to be timed
    :return: returns the wrapped (decorated) function
    """
    @wraps(func)
    def wrapper(*args):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        return end - start

    return wrapper


@sort_timer
def bubble_sort(unordered_list):
    """
    Sorts list in ascending order.
    """
    iteration_count = len(unordered_list) - 1
    # outer loop to keep track of going through entire list
    for i in range(len(unordered_list) - 1):

        # inner loop which will decrease it's time
        for j in range(iteration_count):

            # putting the largest value to the end
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp

        iteration_count -= 1


@sort_timer
def insertion_sort(list_to_sort):
    """
    Sorts a list in ascending order.
    """
    # using an outer loop to walk to the list that needs to be sorted.
    for index in range(1, len(list_to_sort)):
        # storing the value until the correct index to store it at is found
        value_to_insert = list_to_sort[index]
        search_index = index

        while search_index > 0 and list_to_sort[search_index-1] > value_to_insert:
            # moving larger values to the right
            list_to_sort[search_index] = list_to_sort[search_index - 1]
            search_index -= 1

        # search index is now the correct position to insert the value
        list_to_sort[search_index] = value_to_insert


def compare_sorts(func_1, func_2):
    """
    Times the run time of two functions and compares them on a graph
    :param func_1: sort method 1
    :param func_2: sort method 2
    :return:
    """
    func_1_y_coord = []
    func_2_y_coord = []
    x_coord = []
    n = 1
    x = 1000

    while True:
        x_coord.append(x)
        random_list_1 = []

        # generating a list with random numbers
        random_list_1 = [random.randint(1, 10000) for i in range(1, x+1)]

        # making a copy of the same numbers to compare
        random_list_2 = list(random_list_1)

        # calling the decorated function
        func_1_y_coord.append(func_1(random_list_1))
        func_2_y_coord.append(func_2(random_list_2))
        n += 1
        x = n * 1000

        if n == 11:
            break

    # graphing the results
    pyplot.plot(x_coord, func_1_y_coord, 'ro--', linewidth=2)
    pyplot.plot(x_coord, func_2_y_coord, 'go--', linewidth=2)
    pyplot.xlabel("Total numbers sorted")
    pyplot.ylabel("Time")
    pyplot.legend([func_1.__name__, func_2.__name__])
    pyplot.show()

    return


def main():
    compare_sorts(bubble_sort, insertion_sort)


if __name__ == "__main__":
    main()
