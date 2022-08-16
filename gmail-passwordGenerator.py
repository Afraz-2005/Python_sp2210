import random
num = 0

print('\n\n\t\t1. Generate Gmail addresses')
print('\t\t2. Generate password')

choice = int(input('\n\n\t\tchoice 1 or 2: '))

if choice == 1:
    print('\n\n\t\tG-mail address generator')
    print('\t\t=========================')
    G_amount = int(input("\n\t\tenter the number of G-mail addresses to generate: "))
    G_length = int(input("\n\t\tenter the length of the G-mail addresses: "))
    G_chars = ("qwertyuiopasdfghjklzxcvbnm")
    for gmail in range(G_amount):
        num = num + 1
        gmail = " "
        for x in range(G_length):
            gmail += random.choice(G_chars)
        print('\n\t\t', str(num) + '. ' + gmail + '@gmail.com', '\n\n')

elif choice == 2:
    print('\n\n\t\tPassword generator')
    print('\t\t==================')

    amount = int(input("\n\t\tenter the number of passwords to generate: "))
    length = int(input("\t\tenter the legth of the passwords: "))

    chars = ("!@#$%^&*()_+-=./<>,}{][\|qwertyuiopasdfghjklzxcvbnm~`QWERTYUIOPASDFGHJKLZXCVBNM")

    for passwords in range(amount):
        num = num + 1
        passwords = " "
        for x in range(length):
            passwords += random.choice(chars)
        print('\n\t\t', str(num), '. ' + passwords, '\n\n')
else:
    print('\n\n\t\tinvalid input!\n\t\tplease restart the program again\n\n')