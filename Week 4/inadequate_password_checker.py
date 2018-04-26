def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
    'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = (input("enter username:"))
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")
main()
