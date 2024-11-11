import matplotlib.pyplot as plt

algorithms = ['BubbleSortUntilNoChange', 'BubbleSortWhileNeeded', 'QuickSortGPT', 'SelectionSortGPT']
array_sizes = [10, 1000, 10000]


times = {
    'BubbleSortUntilNoChange': [0.089, 3055.678, 32674.919],
    'BubbleSortWhileNeeded': [0.087, 2440.950, 20767.172],
    'QuickSortGPT': [0.045, 23.563, 813.886],
    'SelectionSortGPT': [0.046, 1966.325, 20737.871]
}

plt.figure(figsize=(10, 6))
for algorithm in algorithms:
    plt.plot(array_sizes, times[algorithm], marker='o', label=algorithm)

plt.xlabel('Array Size')
plt.ylabel('Time (µs per operation)')
plt.title('Sorting Algorithm Performance Comparison on a Random Array')  
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True, which="both", ls="--")

plt.show()
