import os
import sys

if __package__ is None or __package__ == "":
    package_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(package_dir)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from math_packages.basic_operations import add, subtract
    from math_packages.advanced_operations import power, square_root
else:
    from .basic_operations import add, subtract
    from .advanced_operations import power, square_root



sum_result = add(10, 20)
sub_result = subtract(20, 10)
pow_result = power(2, 4)
sqrt_result = square_root(16)

print(f"Sum: {sum_result}, Difference: {sub_result}, Power: {pow_result}, Square Root: {sqrt_result}")
