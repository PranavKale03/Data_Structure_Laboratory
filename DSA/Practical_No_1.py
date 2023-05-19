hash_table = [[] for _ in range(10)]
print("# Creation of hash Table")
print(hash_table)
print("Inserting data into hash table")
def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))
insert(hash_table, 15, 'India')
insert(hash_table, 20, 'South Africa')
insert(hash_table, 10, 'Russia')
print(hash_table)
print("\n# Searching Data into hash Table")


def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v
print(search(hash_table, 10))
print(search(hash_table, 20))
print(search(hash_table, 30))
print("\n# Deleting Data into hash Table")

def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))
print(hash_table)
