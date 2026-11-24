#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for list in range(1,50, 3):
    print(list)
#To iterate over the indices of a sequence, you can combine range() and len() as follows:
names = ["Alice", "Bob", "Charlie", "David", "Eve"]    
for i in range(len(names)):
     print(f"Index: {i}, Name: {names[i]}")


#break statement is used to exit a loop prematurely when a certain condition is met. It allows you to terminate the loop and continue with the next statement after the loop.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')     