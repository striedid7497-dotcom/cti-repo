import math

r = float(input("what is the radius of the circle? "))
d = 2 * r
c = 2 * math.pi * r
a = math.pi * (r ** 2)

print()
print(f"diameter of circle is {d:.1f}")
print(f"circumference of circle is {c:.2f}")
print(f"area of circle is {a:.3f}")