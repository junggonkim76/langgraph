"""Simple multiplication table example in Python.

This script prints the classic 2–9 multiplication table known as “구구단” in Korean.
"""

def print_gugudan(start: int = 2, end: int = 9) -> None:
    """Print multiplication tables from `start` to `end`."""
    for i in range(start, end + 1):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        print()  # Blank line between tables


if __name__ == "__main__":
    print_gugudan()
