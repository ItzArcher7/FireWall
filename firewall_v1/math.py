class Math:

    @staticmethod
    def average(numbers):
        numbers = list(numbers)
        if not numbers:
            raise ValueError("List cannot be empty")
        return sum(numbers) / len(numbers)

    @staticmethod
    def maximum(numbers):
        return max(numbers)

    @staticmethod
    def minimum(numbers):
        return min(numbers)

    @staticmethod
    def percentage(value, total):
        if total == 0:
            raise ValueError("Total cannot be zero")
        return (value / total) * 100
