import random, string, os, time, requests, sys
from colorama import Fore

# Colour Variables
lb = Fore.LIGHTBLUE_EX
y = Fore.LIGHTYELLOW_EX
r = Fore.RESET
cy = Fore.LIGHTCYAN_EX
lg = Fore.LIGHTGREEN_EX
lw = Fore.LIGHTWHITE_EX
g = Fore.GREEN

def cls():
    os.system('cls')

# Letter and number string generated
def letter_num(length: int):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Letter, number and special character string generated
def letter_num_char(length: int):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

# Phrase string gen
def phrase():
    r = requests.get('https://random-word-api.herokuapp.com/word?number=1&swear=0')
    return r.json()[0]

# Amount of passwords needed to be generated
def amount_pass():
    try:
        option = int(input('How many passwords do you want to generate? > '))
        return option
    except:
        print('That\'s not a number.')
        time.sleep(2.5)
        menu()
        
# Main menu
def menu():
    cls()
    print(f'''
    {lb} _____         _____ _____  {y}  _____ ______ _   _ 
    {lb}|  __ \ /\    / ____/ ____| {y} / ____|  ____| \ | |
    {lb}| |__) /  \  | (___| (___   {y}| |  __| |__  |  \| |
    {lb}|  ___/ /\ \  \___ \\\___ \ {y} | | |_ |  __| | . ` |
    {lb}| |  / ____ \ ____) |___) | {y}| |__| | |____| |\  |
    {lb}|_| /_/    \_\_____/_____/  {y} \_____|______|_| \_|                                             
    {r}
    Choose password type:

    [{cy}1{r}] Phrase + Numbers & Special Characters - {lg}Most Secure{r}                                           
    [{cy}2{r}] Letters + Numbers & Special Characters - {lg}Extremely Secure{r}
    [{cy}3{r}] Letters + Numbers - {g}Very Secure{r}
    [{cy}4{r}] Exit{r}
    '''.center(os.get_terminal_size().columns))
    try:
        choice = int(input('> '))
    except ValueError:
        print('That\'s not a number.')
        time.sleep(2.5)
        menu()
    if choice == 1:
        amount = amount_pass()
        for i in range(amount):
            print(phrase() + str(random.randint(10, 255)) + ''.join(random.choices(string.punctuation, k=random.randint(2, 4))))
        time.sleep(2.5)
        input(F'\n{lw}Press any key to return to the main menu.{r}')
        menu()
    elif choice == 2:
        amount = amount_pass()
        for i in range(amount):
            print(letter_num_char(random.randint(12, 24)))
        time.sleep(2.5)
        input(F'\n{lw}Press any key to return to the main menu.{r}')
        menu()
    elif choice == 3:
        amount = amount_pass()
        for i in range(amount):
            print(letter_num(random.randint(12, 24)))
        time.sleep(2.5)
        input(F'\n{lw}Press any key to return to the main menu.{r}')
        menu()
    elif choice == 4:
        sys.exit(0)
    else:
        print('Not a valid option')
        time.sleep(2)
        menu()
menu()
