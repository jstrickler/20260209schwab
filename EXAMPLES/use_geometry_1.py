import geometry  # geometry is a module object (finds geometry.py)

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

f = geometry.Foo()

# module search path
# 1. current folder
# 2. folders in PYTHONPATH environment variable
# 3. <installation folder>/lib


