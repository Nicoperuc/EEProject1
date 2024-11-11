# EEProject1
 
This project benchmarks the performance of various sorting algorithms provided for the course "Experimentation and Evaluation." The goal is to analyze and compare the efficiency of these algorithms by measuring their execution time across different input configurations and array sizes. The benchmarking is done using the Java Microbenchmark Harness (JMH) library to ensure accurate and consistent results.

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

- **Java 17** or later.
- **Maven** (for building the project and managing dependencies).

### Building the Project

Build the prject using Maven: `mvn clean package` or `mvn clean install`.

## Running The Test

To run  the test you can run the `main` function in each test class individually in an IDE like IntelliJ, or by using the following commands in the terminal:
- `java -cp target/benchmark.jar testing.TestBubbleSortUntilNoChange`
- `java -cp target/benchmark.jar testing.TestBubbleSortWhileNeeded`
- `java -cp target/benchmark.jar testing.TestQuickSortGPT`
- `java -cp target/benchmark.jar testing.TestSelectionSortGPT`

