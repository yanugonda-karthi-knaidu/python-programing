import json

def contains_complex_object(json_str):
    try:
        # Parse the JSON string
        parsed_data = json.loads(json_str)
        
        # Function to check for complex objects
        def is_complex(obj):
            if isinstance(obj, (dict, list)):
                return True
            return False

        # Recursive function to walk through the object
        def check_complexity(obj):
            if is_complex(obj):
                return True
            elif isinstance(obj, dict):
                return any(check_complexity(value) for value in obj.values())
            elif isinstance(obj, list):
                return any(check_complexity(item) for item in obj)
            return False

        # Check if the parsed object is complex
        return check_complexity(parsed_data)

    except json.JSONDecodeError:
        print("Invalid JSON string")
        return False


# Example usage
json_str_1 = '{"name": "John", "age": 30, "address": {"city": "New York", "zip": 10001}}'
json_str_2 = '{"name": "Alice", "age": 25, "city": "London"}'

print(contains_complex_object(json_str_1))  # True (contains a nested object)
print(contains_complex_object(json_str_2))  
