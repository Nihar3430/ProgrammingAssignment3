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

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
            if A[i] == B[j]:
                dp[i][j] = max(dp[i][j], value[A[i]] + dp[i + 1][j + 1])

    i = 0
    j = 0
    answer = []


    while i < n and j < m:
        if A[i] == B[j] and dp[i][j] == value[A[i]] + dp[i + 1][j + 1]:
            answer.append(A[i])
            i += 1
            j += 1
        elif dp[i][j] == dp[i + 1][j]:
            i += 1
        else:
            j += 1

    """printingg result"""
    print(dp[0][0])
    print("".join(answer))

if __name__ == "__main__":
    main()