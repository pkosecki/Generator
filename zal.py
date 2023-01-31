import sys
import random
import string


password = []   #lista, do której zapisujemy znaki
characters_left = -1
#lowercase_letters = int
print("Program przeznaczony do generowania haseł zgodnych z regułami bezpieczeństwa firmy Microsoft")

def update_characters_left(number_of_characters): #funkcja odpowiadająca za pozostałą liczbę znaków
    
    global characters_left #wykorzystanie zmiennej globalnej, nie lokalnej
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Nieprawidłowa liczba, wybrałeś liczbę znaków:", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Pozostało znaków:", characters_left)


password_length = int(input("Wprowadź liczbę znaków, jaką ma posiadać Twoje hasło: "))

if password_length < 8: #if odpowiadający za minimalną liczbę znaków
    print("Hasło musi mieć minimum 8 znaków, spróbuj jeszcze raz.")
    sys.exit(0)
else:
    characters_left = password_length

#while True:
    #lowercase_letters = input("Ile małych liter ma Twoje hasło? ")
    #try:
        #int(lowercase_letters)
    #except ValueError:
        #print("To nie jest liczba")
    #else:
        #int(lowercase_letters)
        #update_characters_left(lowercase_letters)

lowercase_letters = int(input("Ile małych liter ma Twoje hasło? "))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("Ile duzych liter ma posiadać Twoje hasło? "))
update_characters_left(uppercase_letters)

special_characters = int(input("Ile znaków specjalnych ma posiadać Twoje hasło? "))
update_characters_left(special_characters)

digits = int(input("Ile cyfr ma posiadać Twoje hasło? "))
update_characters_left(digits)

if characters_left > 0: #sprawdzenie czy wszystkie znaki zostały wykorzystane
    print("Nie wszystkie znaki zostały wykorzystane. Hasło zostanie uzupełnione małymi literami.")
    lowercase_letters += characters_left

print()
print("Długość hasła wynosi:", password_length)
print("Ilość małych liter:", lowercase_letters)
print("Ilość dużych liter:", uppercase_letters)
print("Ilość znaków specjalnych:", special_characters)
print("Ilość cyfr", digits)

for x in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Hasło zostało zapisane do pliku.")

with open('password.txt', 'w') as save: #zapisywanie hasła do pliku .txt, plik tworzy się w folderze z projektem
    for line in password:
        save.write(line)

#def toString(password):
    #str1 = ""
   # for ele in password:
        #str1 += ele
    #return str1

#print(listToString(password))


#def save():

   # outfile = open('password.txt', 'w')
    #passw = input(toString)
    #outfile.write(passw)
   # outfile.close()


#save()