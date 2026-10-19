class Counter:
    """A simple counter that tracks a running total."""

    def __init__(self, start=0):
        self.start = start
        # BUG: forgot to initialize self.count = start

    def increment(self, amount=1):
        self.count += amount  # AttributeError: 'Counter' object has no attribute 'count'

    def get_value(self):
        return self.count
