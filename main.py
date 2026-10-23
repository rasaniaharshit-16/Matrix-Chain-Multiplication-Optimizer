
from matrix_chain import matrix_chain_order, optimal_order


def main():
    print("=" * 45)
    print(" MATRIX CHAIN MULTIPLICATION OPTIMIZER")
    print("=" * 45)

    try:
        n = int(input("Enter number of matrices: "))

        if n < 1:
            raise ValueError("Number of matrices must be positive.")

        print(f"Enter {n + 1} dimensions:")
        p = list(map(int, input().split()))

        if len(p) != n + 1:
            raise ValueError(f"Exactly {n + 1} dimensions required.")

        dp, split = matrix_chain_order(p)

        print("\n--- OPTIMIZATION RESULT ---")

        for i in range(n):
            print(f"A{i+1}: {p[i]} x {p[i+1]}")

        print("\nMinimum Multiplication Cost:", dp[0][n-1])

        print(
            "Optimal Parenthesization:",
            optimal_order(split, 0, n-1)
        )

        print("\nCost Table:")
        for row in dp:
            print(row)

        print("\nTime Complexity: O(n^3)")
        print("Space Complexity: O(n^2)")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
