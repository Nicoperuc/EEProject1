import matplotlib.pyplot as plt


algorithms = ['BubbleSortUntilNoChange', 'BubbleSortWhileNeeded', 'QuickSortGPT', 'SelectionSortGPT']
array_sizes = [10, 1000, 10000]

times_reverse_array = {
    'BubbleSortUntilNoChange': [0.218, 2205.642, 242263.529],
    'BubbleSortWhileNeeded': [0.185, 1344.578, 143329.158],
    'QuickSortGPT': [0.211, 586.745, 38106.331],
    'SelectionSortGPT': [0.092, 1964.860, 207777.980]
}


plt.figure(figsize=(10, 6))
for algorithm in algorithms:
    plt.plot(array_sizes, times_reverse_array[algorithm], marker='o', label=algorithm)


plt.xlabel('Array Size')
plt.ylabel('Time (µs per operation)')
plt.title('Sorting Algorithm Performance Comparison on a Reverse Sorted Array')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True, which="both", ls="--")


plt.show()
