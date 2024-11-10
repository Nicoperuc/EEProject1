package algorithms;


public interface Sorter<T extends Comparable<T>> {
	
	void sort(T[] items);
	
}
