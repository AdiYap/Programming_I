
"""Ask the user for their username. If the username is in the list of authorised users, print “Access
granted”, otherwise print “Access denied”."""


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']

name_prompt = str(input("Please enter your username: "))
if name_prompt in usernames:
    print("Access Granted")
else:
    print("Access Denied")