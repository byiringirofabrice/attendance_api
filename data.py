def multiplication_table(number):


  for i in range(1, 13):
  
    product = number * i
    print(f"{number} x {i} = {product}")


while True:
  try:
    num = int(input("Enter a number (or 'x' to quit): "))
    break
  except ValueError:
    print("Invalid input. Please enter an integer.")

if num != 'x':
  multiplication_table(num)
