import random

def generate_cache_trace(filename, num_accesses, num_unique_items):
    with open(filename, 'w') as file:
        for _ in range(num_accesses):
            # Generate a random access request
            access_request = str(random.randint(1, num_unique_items))
            file.write(access_request + '\n')

# Parameters
filename = 'cache_trace.txt'
num_accesses = 1000  # Total number of cache access requests
num_unique_items = 100  # Number of unique items that can be requested

generate_cache_trace(filename, num_accesses, num_unique_items)