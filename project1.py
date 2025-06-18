def validate_data(data):
   
    invalid_entries = []
    
   
    for entry in data:
        # Check if 'age' key exists and is an integer
        if "age" not in entry or not isinstance(entry["age"], int):
            invalid_entries.append(entry)
    
    return invalid_entries


data = [
    {"name": "Alice", "age": 30},        # Valid
    {"name": "Bob", "age": "25"},        # Invalid (age is a string)
    {"name": "Charlie"},                 # Invalid (age is missing)
    {"name": "Diana", "age": 40},        # Valid
    {"name": "Eve", "age": None},        # Invalid (age is None)
]


invalid = validate_data(data)

print("Invalid entries:")
for item in invalid:
    print(item)
