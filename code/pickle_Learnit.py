import pickle

'LOGOWANIE'
recordarme = []
with open('recordarme_file', 'wb') as file:
    pickle.dump(recordarme, file)
dont_log = False
with open('dont_log_file', 'wb') as file:
    pickle.dump(dont_log, file)
username_and_password = {}
with open('usernames_and_passwords', 'wb') as file:
    pickle.dump(username_and_password, file)