# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    # TODO: Write your logic here safely
    if not isinstance(data, dict):
        return "Unknown"
    specs = data.get("specs")
    if not isinstance(specs, dict):
        return "Unknown"
    model_info = specs.get("model_info")
    if not isinstance(model_info, dict):
        return "unknown"
    
    return model_info.get("year", "unknown")

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))
