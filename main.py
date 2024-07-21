import os, time

listOfEmails = []


def prettyPrint():
  os.system("clear")
  print()
  print("LIST OF EMAILS")
  print()
  for index in range(len(listOfEmails)):
    print(f" {index}: {listOfEmails[index]}")
    
def spam():
  os.system("clear")
  print("SPAM LETTERS")
  print()
  for i in range(0, 10):
    print(f"""Dear {listOfEmails[i]},
          It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

          Love and hugs,
          Ian Spammington III)""")
    time.sleep(2)
    os.system("clear")

while True:
  
  print("SPAMMER INC")
  print(" 1. Add\n 2. Remove\n 3. View list\n 4. Get Spamming\n")
  print()
  menu = input("Which option would you like to choose? > ")
  os.system("clear")
  
  if menu == "1":
    email = input("Email> ")
    listOfEmails.append(email)
    os.system("clear")
  elif menu == "2":
    email = input("Email > ")
    if email in listOfEmails:
      listOfEmails.remove(email)
      os.system("clear")
  elif menu == "3":
    prettyPrint()
    time.sleep(2)
    os.system("clear")
  elif menu == "4":
    spam()
    
    
    
    