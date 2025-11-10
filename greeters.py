# def greet_user(username):
#   print(f"Hello, {username}!")
  
# greet_user('wang qian')

def get_formatted_name(first, last):
  full_name = f"{first} {last}"
  return full_name.title()

while True:
  print("\nPlease tell me your name:")
  print("(enter 'q' at any time to quit)")
  
  f_name = input("First name: ")
  if f_name == 'q':
    break
  l_name = input("Last name: ")
  if l_name == 'q':
    break
  formatted_name = get_formatted_name(f_name, l_name)
  print(f"\nHello, {formatted_name}!")
  
  