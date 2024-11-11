# EEProject1
 
This project benchmarks the performance of various sorting algorithms provided for the course "Experimentation and Evaluation." The goal is to analyze and compare the "efficiency"(run time) of four algorithms by measuring their execution time across different input configurations and array sizes. The benchmarking is done using the Java Microbenchmark Harness (JMH) library to ensure accurate and consistent results.

## Project Structure

- **src/main/java/algorithms**: Contains the sorting algorithm implementations:
  - `BubbleSortUntilNoChange`
  - `BubbleSortWhileNeeded`
  - `QuickSortGPT`
  - `SelectionSortGPT`
  
- **src/main/java/testing**: Contains the test classes for each sorting algorithm:
  - `TestBubbleSortUntilNoChange`
  - `TestBubbleSortWhileNeeded`
  - `TestQuickSortGPT`
  - `TestSelectionSortGPT`
  - `OptionBuilder`: A helper class for setting up JMH options.

## Getting Started
### Prerequisites

- **Java 17** 
- **Maven** 

### Building the Project

Building the project using Maven: `mvn clean package` or `mvn clean install`.

## Running The Test

To run the test you can run the `main` function in each test class individually in an IDE (ex : IntelliJ), or by using the following commands in the terminal:
- `java -cp target/benchmark.jar testing.TestBubbleSortUntilNoChange`
- `java -cp target/benchmark.jar testing.TestBubbleSortWhileNeeded`
- `java -cp target/benchmark.jar testing.TestQuickSortGPT`
- `java -cp target/benchmark.jar testing.TestSelectionSortGPT`

