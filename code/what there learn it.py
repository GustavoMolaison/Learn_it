import pickle
with open('recordarme_file', 'rb') as file:
    recordarme = pickle.load(file)
dont_log = False
with open('dont_log_file', 'rb') as file:
    dont_log = pickle.load(file)
username_and_password = {}
with open('usernames_and_passwords', 'rb') as file:
    username_and_password = pickle.load(file)

print(recordarme)
print(username_and_password)
print(dont_log)
