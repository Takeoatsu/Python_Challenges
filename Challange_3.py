def online_count(users):
    count = 0
    for key in users:
        if users[key] == "online":
            count += 1
    return count

users = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(users))