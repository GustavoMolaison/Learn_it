import pickle
with open('recordarme_file', 'rb') as file:
    recordarme = pickle.load(file)

with open('dont_log_file', 'rb') as file:
    dont_log = pickle.load(file)

with open('usernames_and_passwords', 'rb') as file:
    username_and_password = pickle.load(file)

with open('clicked_buttons_picklefile_esp', 'rb') as file:
    unknown_word_pickle_esp = pickle.load(file)
with open('clicked_buttons_picklefile_eng', 'rb') as file:
    unknown_word_pickle_eng = pickle.load(file)

print(recordarme)
print(username_and_password)
print(dont_log)
print(unknown_word_pickle_esp)
print(unknown_word_pickle_eng)
