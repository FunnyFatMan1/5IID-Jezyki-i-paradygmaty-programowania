def analyze_data(data):
    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    strings = list(filter(lambda x: isinstance(x, str), data))
    tuples = list(filter(lambda x: isinstance(x, tuple), data))

    max_number = max(numbers) if numbers else None
    longest_string = max(strings, key=len) if strings else None
    largest_tuple = max(tuples, key=len) if tuples else None

    return max_number, longest_string, largest_tuple
