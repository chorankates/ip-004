# compute the are of a triangle
def triangle_area(base, height):
  area = (1.0/ 2) * base * height
  return area


print triangle_area(3, 8)
print triangle_area(2, 5)


# converts fahrenheit to celsius
def fahrenheit2celsius (f):
  celsius = (5.0 / 9) * (f - 32)
  return celsius

print fahrenheit2celsius(32)
print fahrenheit2celsius(212)

# convert fahrenheit to kelvin
def fahrenheit2kelvin (f):
  celsius = fahrenheit2celsius(f)
  kelvin  = celsius + 273.15
  return kelvin

print fahrenheit2kelvin(32)
print fahrenheit2kelvin(212)

# prints hello, world!
def hello():
  print 'Hello, world!'

hello()

h = hello()
print h # 'None', not 'nil'
