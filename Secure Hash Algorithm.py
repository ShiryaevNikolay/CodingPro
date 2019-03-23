from random import shuffle

example_table = range(0, 256)
shuffle(example_table)


def hash8(message, table):
    hash = len(message) % 256
    for i in message:
        hash = table[(hash + ord(i)) % 256]
    return hash