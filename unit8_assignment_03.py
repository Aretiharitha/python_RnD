__author__ = 'Krish'
import unit8_conversion_methods as methods
import cProfile
profiling_cprofile = '''
This is the tool of choice for analyzing large programs (parallel to the debugger). The profiler adds its own overhead
but for relative comparison of time spent, it is very very useful.

References:
1. https://docs.python.org/3/library/profile.html
2. http://pysnippet.blogspot.in/2009/12/profiling-your-python-code.html

In particular, make sure you learn how to use pstats and running cProfile from command line as described in the
2nd reference using a sample program before doing this assignment.

python -m cProfile [-o output_file] [-s sort_order] myscript.py

For this assignment learn to use the cProfile and pstats modules from the command line.
1. run the cprofile and collect a stats file
2. learn to use the stats file separately.
3. bypass the stats creation and directly print the output to console.

compare the cumulative times of these methods and then calculate per call times.
'''


#invoke each of the 4 methods 5 times in a loop for count=10000. Then run this in the profiler and study the output
def profile_profiler():
    funcs = [methods.numbers_string1, methods.numbers_string2, methods.numbers_string3, methods.num_strings4]
    for func in funcs:
        for i in range(1,5):
            cProfile.run(func.__name__ + '(' + str(10**i) + ')')



# compare the times taken per call using this method to what you found in the previous methods.
# when would you use the profiler over other methods, what additional data did you get from the profiler easily
# that would have taken more work in other methods?

# what did you learn about cProfile and pstats?

summary = '''
I can sort by an attribute such as time easily and I can get total time, cumulative time and time per call which would
be nearly impossible to get using other methods. And using cProfile and pstats through command line is easier and
quicker than the other types of profiling.
'''

if __name__ == "__main__":
    profile_profiler()
