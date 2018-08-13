#!/usr/bin/env python3
# Lesson 03, String formatting lab

# Task One
in_tuple = ( 2, 123.4567, 10000, 12345.67)
print("file_{:03d}: {:.2f}, {:.2e}, {:.2e}".format(*in_tuple))

# Task Two
print(f"file_{in_tuple[0]:03}: {in_tuple[1]:.2f}, {in_tuple[2]:.2e}, {in_tuple[3]:.2e}")

