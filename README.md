# compare_sort

For this project, you will import the **time** and **random** modules.  You will also install the **matplotlib** package and import from it the **pyplot** module.  You will also import the wraps() function from the functools module for use in your decorator.

Use the **time** module to write a decorator function named sort_timer that times how many seconds it takes the decorated function to run.  Since sort functions don't need to return anything, have the decorator's wrapper function return that elapsed time.

To get the current time, call time.perf_counter().  Subtracting the begin time from the end time will give you the elapsed time in seconds.

Write a function called **compare_sorts** that takes the two decorated sort functions as parameters.  It should randomly generate a list of 1000 numbers and then make a separate copy of that list.

Next it should time how long it takes bubble sort to sort one of those copies (using the decorated bubble sort), and then time how long it takes insertion sort to sort the other copy (using the decorated insertion sort).  This gets us the first data point for each algorithm.  The function should now repeat this for lists of size 2000, 3000, and so on, up to 10000.  For each list size, the function should randomly generate a list of that size and time how long it takes each algorithm to sort it.  The random numbers should all be integers in the range 1 <= r <= 10000.  Once the function has the 10 time data points for each algorithm, it will generate a graph comparing them.

To generate random numbers, you will need to import the **random** module. 

To generate a graph, you will need to install the **matplotlib** package and import **pyplot** from it.  

Your file must be named: **sort_timer.py**
