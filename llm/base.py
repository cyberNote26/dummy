import abc

class LowBitLLM(abc.ABC):
    @abc.abstractmethod
    def generate(self, *args, **kwargs):
        """Generate output based on input arguments."""
        pass

    def collect_performance_metrics(self):
        """Collect and return performance metrics of the LLM."""
        # Logic to collect metrics can be implemented here
        return {
            'metric_1': 0,
            'metric_2': 0,
        }