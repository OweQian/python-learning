users = {
  'aeinstein': {
    "first_name": "Albert",
    "last_name": "Einstein",
    "location": "Princeton",
  },
  'mcurie': {
    'first_name': "Marie",
    'last_name': "Curie",
    'location': "Paris",
  }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")