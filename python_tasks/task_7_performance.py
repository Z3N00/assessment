# Task: Performance Optimization
# Instructions: You have a list of 10,000 banned emails. 
# Write a function that checks if a user's email is banned in an efficient way.

def is_banned(email, banned_list):
    
    banned_set = set(banned_list)
    return email in banned_set

# Test
banned = ["user1@test.com", "user2@test.com"] # Pretend this is 10k items
print(is_banned("user1@test.com", banned))
