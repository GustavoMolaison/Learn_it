import pickle

'LOGOWANIE'
# recordarme = []
# with open('recordarme_file', 'wb') as file:
#     pickle.dump(recordarme, file)
# dont_log = False
# with open('dont_log_file', 'wb') as file:
#     pickle.dump(dont_log, file)
# username_and_password = {}
# with open('usernames_and_passwords', 'wb') as file:
#     pickle.dump(username_and_password, file)

'GAFIKA'
unknown_word_pickle_esp = None
unknown_word_pickle_eng = None
unknown_button_pickle = None
with open('clicked_buttons_picklefile_esp', 'wb') as file:
    pickle.dump(unknown_word_pickle_esp, file)
with open('clicked_buttons_picklefile_eng', 'wb') as file:
    pickle.dump(unknown_word_pickle_eng, file)

with open('unknown_button_file', 'wb') as file:
    pickle.dump(unknown_button_pickle, file)