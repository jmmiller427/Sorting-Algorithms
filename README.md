# Sorting-Algorithms
Different algorithms to properly sort a list of numbers. 
This program uses 4 separate sorting algorithms to sort a list of positive integers. The four separate algorithms are selection sort, insertion sort, quick sort (random or specific pivot) and finally mergesort. It also will keep a count of how many times each algorithm runs to sort the full list. 

# USAGE

In the terminal, under the folder where the file can be found, the program can be ran with:

```
python sort.py
```

## Testing

When ran the output should look as follows:

```
Press 1 for selection sort.
Press 2 for insertion sort.
Press 3 for quicksort with random pivot.
Press 4 for quicksort with first index as pivot.
Press 5 for mergesort.
```

```
Your selection: 1

Please input positive numbers (Enter to quit): 2
Please input positive numbers (Enter to quit): 5
Please input positive numbers (Enter to quit): 2
Please input positive numbers (Enter to quit): 8
Please input positive numbers (Enter to quit): 6
Please input positive numbers (Enter to quit): 9
Please input positive numbers (Enter to quit): 3
Please input positive numbers (Enter to quit): 6
Please input positive numbers (Enter to quit): 
[2, 2, 3, 5, 6, 6, 8, 9]
Count =  36
```

```
Your selection: 2

Please input positive numbers (Enter to quit): 2
Please input positive numbers (Enter to quit): 5
Please input positive numbers (Enter to quit): 1
Please input positive numbers (Enter to quit): 5
Please input positive numbers (Enter to quit): 9
Please input positive numbers (Enter to quit): 8
Please input positive numbers (Enter to quit): 4
Please input positive numbers (Enter to quit): 3
Please input positive numbers (Enter to quit): 
[1, 2, 3, 4, 5, 5, 8, 9]
Count =  7
```

```
Your selection: 3

Please input positive numbers (Enter to quit): 2
Please input positive numbers (Enter to quit): 7
Please input positive numbers (Enter to quit): 8
Please input positive numbers (Enter to quit): 3
Please input positive numbers (Enter to quit): 1
Please input positive numbers (Enter to quit): 8
Please input positive numbers (Enter to quit): 0
Please input positive numbers (Enter to quit): 3
Please input positive numbers (Enter to quit): 
[0, 1, 2, 3, 3, 7, 8, 8]
Count =  7
```

```
Your selection: 4

Please input positive numbers (Enter to quit): 3
Please input positive numbers (Enter to quit): 6
Please input positive numbers (Enter to quit): 1
Please input positive numbers (Enter to quit): 7
Please input positive numbers (Enter to quit): 9
Please input positive numbers (Enter to quit): 3
Please input positive numbers (Enter to quit): 6
Please input positive numbers (Enter to quit): 2
Please input positive numbers (Enter to quit): 
[1, 2, 3, 3, 6, 6, 7, 9]
Count =  7
```

```
Your selection: 5

Please input positive numbers (Enter to quit): 4
Please input positive numbers (Enter to quit): 6
Please input positive numbers (Enter to quit): 1
Please input positive numbers (Enter to quit): 8
Please input positive numbers (Enter to quit): 4
Please input positive numbers (Enter to quit): 3
Please input positive numbers (Enter to quit): 9
Please input positive numbers (Enter to quit): 2
Please input positive numbers (Enter to quit): 
[1, 2, 3, 4, 4, 6, 8, 9]
Count =  17
```
