import sys

def main():
    data = sys.stdin.read().strip().split()
    idx = 0

    K = int(data[idx])
    idx += 1

    value = {}
    for _ in range(K):
        ch = data[idx]
        w = int(data[idx + 1])
        value[ch] = w
        idx += 2

    A = data[idx]
    B = data[idx + 1]

    n = len(A)
    m = len(B)

    i = 0
    j = 0
    answer = []