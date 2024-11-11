import pandas as pd
import matplotlib.pyplot as plt

# load data
data = pd.read_csv('new_benchmark_data.csv')


array_sizes = [10, 1000, 10000, 100000]
data_filtered = data[data['ArraySize'].isin(array_sizes)]

#  titles
configurations = ['RandomArray', 'ReverseArray', 'SortedArray']
config_titles = {
    'RandomArray': 'Execution Time by Array Size for Pattern: Random',
    'ReverseArray': 'Execution Time by Array Size for Pattern: Reverse',
    'SortedArray': 'Execution Time by Array Size for Pattern: Sorted'
}


for config in configurations:
    plt.figure(figsize=(10, 6))
    
    config_data = data_filtered[data_filtered['Benchmark'].str.contains(config)]
    
    for algorithm in config_data['Benchmark'].unique():
        algorithm_data = config_data[config_data['Benchmark'] == algorithm]
        plt.plot(
            algorithm_data['ArraySize'],
            algorithm_data['Score'],
            marker='o',
            label=algorithm.split('.')[0]  
        )
    
    
    plt.title(config_titles[config])
    plt.ylabel('Execution Time (us/op)')
    plt.xlabel('Array Size')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

   
    plt.savefig(f'Line_Plot_{config}.png')

  
    plt.show()
