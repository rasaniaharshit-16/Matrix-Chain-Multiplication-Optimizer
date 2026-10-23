DAA Mini Project
# Matrix Chain Multiplication Cost Optimizer

A Python-based mini-project developed for the **Design and Analysis of Algorithms (DAA)** course.

## Introduction

Matrix Chain Multiplication is an optimization problem that determines the most efficient order for multiplying a sequence of matrices.

Different multiplication orders can require different numbers of scalar multiplications.

This project uses Dynamic Programming to calculate the minimum multiplication cost and generate the optimal parenthesization.

## Features

- User-friendly command-line interface
- Dynamic Programming implementation
- Minimum multiplication cost calculation
- Optimal parenthesization
- DP cost table visualization
- Input validation
- Automated test cases

## Technologies Used

- Programming Language: Python 3
- Algorithm: Dynamic Programming
- Development Tool: Visual Studio Code
- Version Control: Git and GitHub

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Execute:

## How to run
1. Open Python IDLE
2. Add File
3. Press F5
4. Execute:

```bash
python main.py
```

5. Enter the number of matrices and their dimensions.

## Example

Input:

```text
4
10 20 30 40 30
```

Output:

```text
Minimum Multiplication Cost: 30000
Optimal Parenthesization: (((A1 x A2) x A3) x A4)
```

## Algorithm Complexity

| Operation | Complexity |
|---|---|
| Time Complexity | O(n³) |
| Space Complexity | O(n²) |

Here, n represents the number of matrices.

## Testing

Run the automated tests using:

```bash
python -m unittest discover
```

## Conclusion

The Matrix Chain Multiplication Cost Optimizer demonstrates how Dynamic Programming reduces repeated calculations and efficiently determines the optimal multiplication order.

This project provides a practical implementation of an important optimization problem studied in Design and Analysis of Algorithms.


