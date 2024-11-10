package testing;

import algorithms.BubbleSortUntilNoChange;
import algorithms.Sorter;
import org.openjdk.jmh.annotations.*;

import java.util.Arrays;
import java.util.Collections;
import java.util.Random;
import java.util.concurrent.TimeUnit;

import org.openjdk.jmh.runner.RunnerException;
import testing.OptionBuilder;
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Benchmark)

public class TestBubbleSortUntilNoChange {

    private Integer[] array;
    private Integer[] randomArray;
    private Integer[] sortedArray;
    private Integer[] reverseArray;

    private final Sorter<Integer> sorter = new BubbleSortUntilNoChange<>();

    @Param({"10", "1000", "10000", "100000"})
    private int arraySize;

    @Setup(Level.Trial)
    public void setUp() {
        randomArray = generateRandomArray(arraySize);
        sortedArray = Arrays.copyOf(randomArray, arraySize);
        Arrays.sort(sortedArray);
        reverseArray = Arrays.copyOf(sortedArray, arraySize);
        Collections.reverse(Arrays.asList(reverseArray));
    }

    @Setup(Level.Invocation)
    public void setUpInvocation() {
        array = Arrays.copyOf(randomArray, arraySize);
    }

    @Benchmark
    public void benchmarkSortRandomArray() {
        sorter.sort(array);
    }

    @Benchmark
    public void benchmarkSortSortedArray() {
        array = Arrays.copyOf(sortedArray, arraySize);
        sorter.sort(array);
    }

    @Benchmark
    public void benchmarkSortReverseArray() {
        array = Arrays.copyOf(reverseArray, arraySize);
        sorter.sort(array);
    }

    private Integer[] generateRandomArray(int size) {
        Random random = new Random();
        Integer[] array = new Integer[size];
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(1000);
        }
        return array;
    }

    public static void main(String[] args) throws RunnerException {
        OptionBuilder.getRunner(TestBubbleSortUntilNoChange.class.getName()).run();

    }
}
