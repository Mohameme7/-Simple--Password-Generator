import random, string, os, time, aiohttp, asyncio
from colorama import Fore
from tkinter.filedialog import asksaveasfile

lb = Fore.LIGHTBLUE_EX
ly = Fore.LIGHTYELLOW_EX
y = Fore.YELLOW
r = Fore.RESET
cy = Fore.LIGHTCYAN_EX
lg = Fore.LIGHTGREEN_EX
lw = Fore.LIGHTWHITE_EX
g = Fore.GREEN
async def letter_num():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(12, 24)))

async def letter_num_char():
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(12, 24)))

async def phrase_num_char():
    password = ''
    async with aiohttp.ClientSession() as session:

         request = await session.get('https://random-word-api.herokuapp.com/word?number=1&length=6')
         phrase = (await request.json())[0]
         
         for char in phrase:
          password += char + str(random.randint(10, 99)) + ''.join(
          random.choices(string.punctuation, k=random.randint(3, 5)))
    return password



async def amount_pass():
    try:
        option = int(input('How many passwords do you want to generate? > '))

        return option
    except:
        print('That\'s not a number.')
        await asyncio.sleep(2.5)
        await menu()




async def menu():

    os.system('cls')
    print(f'''
    {lb} _____         _____ _____  {ly}  _____ ______ _   _ 
    {lb}|  __ \ /\    / ____/ ____| {ly} / ____|  ____| \ | |
    {lb}| |__) /  \  | (___| (___   {ly}| |  __| |__  |  \| |
    {lb}|  ___/ /\ \  \___ \\\___ \ {ly} | | |_ |  __| | . ` |
    {lb}| |  / ____ \ ____) |___) | {ly}| |__| | |____| |\  |
    {lb}|_| /_/    \_\_____/_____/  {ly} \_____|______|_| \_|                                             
    {r}
    Choose password type:
    [{cy}1{r}] Phrase + Numbers & Special Characters - {lg}Most Secure{r}                                           
    [{cy}2{r}] Letters + Numbers & Special Characters - {g}Extremely Secure{r}
    [{cy}3{r}] Letters + Numbers - {y}Secure{r}
    '''.center(os.get_terminal_size().columns))

    try:
        choice = int(input('> '))

        if not choice in [1, 2, 3]:
            print('Not a valid option')
            await asyncio.sleep(2)
            await menu()
        tasks = []
        for i in range(await amount_pass()):
           options = {
               1:  phrase_num_char,
               2:  letter_num_char,
               3:  letter_num
           }
           task = asyncio.create_task(options[choice]())
           tasks.append( task)
        async def gather():
            passwords = await asyncio.gather(*tasks)
            return passwords
        passwords = await gather()
        numofpasses = 0
        for e in passwords:
            numofpasses += 1
            print(f'[{y}{numofpasses}{r}] {e}')



        await asyncio.sleep(1)
        savequest = input(f"[{cy}?{r}] Would You Like to save the passwords generated? ")
        if savequest.lower() in ['yes', 'y']:
            file = asksaveasfile(initialfile = 'Untitled.txt',
            defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if file:
             file.write('\n'.join(passwords))
             file.close()

        input(F'\n{lw}Press enter to return to the main menu.{r}')
        await menu()
    except:
        print('Not a valid option')
        await asyncio.sleep(2)
        await menu()
if __name__ == "__main__":
    asyncio.run(menu())

