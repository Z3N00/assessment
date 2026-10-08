# Task: Error Handling & Resilience
# Goal: Calculate a discount safely.

def calculate_discount(price, discount_percent):
  
    
  if not isinstance(price, (int, float)) or isinstance(price, bool):
    return 0
  if not isintance(discount_percent, (int, float)) or isinstance(discount_percent, bool):
    return 0
  if price < 0 or not 0 <= discount_percent <= 100:
    return 0
    
  return (price * discount_percent) / 100
      

# Test Case
print(calculate_discount(100, "10")) # Should return 0 or handle conversion
print(calculate_discount(100, 0))    # Should return 0
