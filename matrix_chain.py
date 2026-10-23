
def matrix_chain_order(p):
    n = len(p) - 1

    if n < 1 or any(x <= 0 for x in p):
        raise ValueError("Enter valid positive matrix dimensions.")

    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split


def optimal_order(split, i, j):
    if i == j:
        return f"A{i + 1}"

    k = split[i][j]

    left = optimal_order(split, i, k)
    right = optimal_order(split, k + 1, j)

    return f"({left} x {right})"
