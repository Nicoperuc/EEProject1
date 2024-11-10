package testing;


import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import org.openjdk.jmh.runner.options.VerboseMode;
import java.util.concurrent.TimeUnit;
public class OptionBuilder {

    public static Runner getRunner(String class_name) {
        var opt = new OptionsBuilder()
                .include(class_name)
                .verbosity(VerboseMode.NORMAL)
                .forks(1)
                .timeUnit(TimeUnit.MICROSECONDS)
                .mode(Mode.AverageTime)
                .measurementIterations(5)
                .warmupIterations(5)
                .build();
        return new Runner(opt);
    }
}
