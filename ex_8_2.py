'''Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. 
A call to print_triangular_numbers(5) would produce the following output:

1       1
2       3
3       6
4       10
5       15
'''

def print_triangular_numbers(n):
    for i in range(n):
        tn = ((i+1) * ((i+1) + 1))/2
        print((i+1),'\t',int(tn))

print_triangular_numbers(5)