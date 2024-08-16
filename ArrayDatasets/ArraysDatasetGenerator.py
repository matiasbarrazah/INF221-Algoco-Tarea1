import random
import json

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def generate_partially_sorted_list(size, sorted_fraction=0.5):
    l = generate_random_list(size)
    sorted_size = int(size * sorted_fraction)
    l[:sorted_size] = sorted(l[:sorted_size])
    return l

def generate_sorted_list(size, reverse=False):
    l = generate_random_list(size)
    l.sort(reverse=reverse)
    return l

def generate_almost_sorted_list(size, swaps=10):
    l = generate_sorted_list(size)
    for _ in range(swaps):
        i, j = random.sample(range(size), 2)
        l[i], l[j] = l[j], l[i]
    return l


with open('random_list.json', 'w') as f:
    json.dump(generate_random_list(1000), f)

with open('partially_sorted_list.json', 'w') as f:
    json.dump(generate_partially_sorted_list(1000, 0.75), f)

with open('almost_sorted_list.json', 'w') as f:
    json.dump(generate_almost_sorted_list(1000, 10), f)

with open('sorted_list.json', 'w') as f:
    json.dump(generate_sorted_list(1000), f)

with open('reverse_sorted_list.json', 'w') as f:
    json.dump(generate_sorted_list(1000, reverse=True), f)