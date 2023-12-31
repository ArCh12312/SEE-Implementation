from collections import OrderedDict
import time
import hashlib

# Function to simulate LRU cache using hash map
def simulate_fifo_cache(cache_size, trace_file):
    cache = OrderedDict()
    seen = {}
    hits = 0
    miss = 0

    with open(trace_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()  # Remove whitespace and newline characters
        address = line.split()[1] # Extract the memory address
        line_hash = hashlib.sha256(address.encode()).hexdigest()  # Create a hash of the line

        if line_hash in cache:
            hits += 1
            continue
        miss += 1
        if len(cache) < cache_size:
            cache[line_hash] = line  # Insert the new item
            seen[line_hash] = True
            continue
        if line_hash not in seen:
            seen[line_hash] = True
            continue
        cache.popitem(last=False)  # Remove the oldest item
        cache[line_hash] = line  # Insert the new item

    return hits, miss

# Cache sizes and trace files
cache_sizes = [32, 64, 128, 256, 512, 1024, 2048, 4096]
files = ['./traces/trace1.trace', './traces/trace2.trace', './traces/trace3.trace', './traces/trace4.trace']

# Run simulation for each cache size and file
for cache_size in cache_sizes:
    for file in files:
        start_time = time.time()
        hits, miss = simulate_fifo_cache(cache_size, file)
        end_time = time.time()
        print(f'Cache Size: {cache_size}, File: {file}, Hits: {hits}, Miss: {miss}, Execution Time: {end_time - start_time} seconds')
