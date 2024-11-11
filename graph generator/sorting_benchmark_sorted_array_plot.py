import matplotlib.pyplot as plt


algorithms = ['BubbleSortUntilNoChange', 'BubbleSortWhileNeeded', 'QuickSortGPT', 'SelectionSortGPT']
array_sizes = [10, 1000, 10000]


times_sorted_array = {
    'BubbleSortUntilNoChange': [0.014, 0.652, 14.124],
    'BubbleSortWhileNeeded': [0.011, 0.660, 13.795],
    'QuickSortGPT': [0.246, 105.739, 100106.372],
    'SelectionSortGPT': [0.047, 125.766, 23012.228]
}

plt.figure(figsize=(10, 6))
for algorithm in algorithms:
    plt.plot(array_sizes, times_sorted_array[algorithm], marker='o', label=algorithm)

plt.xlabel('Array Size')
plt.ylabel('Time (µs per operation)')
plt.title('Sorting Algorithm Performance Comparison on a Sorted Array')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True, which="both", ls="--")

plt.show()
