# SQA-Lab

A small Python project created for the Software Quality Assurance (SQA) lab. It demonstrates unit testing and static code analysis using SonarQube Cloud.

## Project Structure

```
SQA-Lab/
├── calculator.py         # Calculator functions
├── test_calculator.py    # Unit tests
└── README.md
```

## Features

The `calculator` module provides:

- `add(a, b)`: addition
- `subtract(a, b)`: subtraction
- `multiply(a, b)`: multiplication
- `divide(a, b)`: division (raises `ValueError` on division by zero)
- `power(base, exponent)`: exponentiation
- `is_even(number)`: checks whether a number is even
- `factorial(n)`: factorial of a non-negative integer
- `average(numbers)`: average of a non-empty list

## Requirements

- Python 3.8 or higher

No external libraries are needed.

## Running the Tests

```bash
python -m unittest test_calculator.py -v
```

## Code Quality

This project is analyzed with [SonarQube Cloud](https://sonarcloud.io) for:

- Security
- Reliability
- Maintainability
- Duplications
- Code coverage

## Author

2023csf104-coder
