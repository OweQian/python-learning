def greet_users(usernames):
  for username in usernames:
    message = f"Hello, {username.title()}!"
    print(message)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)