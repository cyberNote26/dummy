class BitNetLLM:
    def __init__(self):
        self.context = []  # Initialize context

    def add_to_context(self, input_data):
        """Add input data to context, keeping track of the last few inputs."""
        self.context.append(input_data)
        if len(self.context) > 5:  # Limit context size to last 5 inputs
            self.context.pop(0)

    def infer(self, input_data):
        """Simulate 1-bit weight inference based on input_data and context."""
        # Simulate 1-bit weight inference logic here
        # For simplicity, we'll just return a mock output
        output = 'Simulated output for input: ' + input_data
        return output

    def low_memory_inference(self, input_data):
        """Perform low-memory inference by limiting context usage."""
        # Use a simplified context for low memory usage
        self.add_to_context(input_data)
        return self.infer(input_data)