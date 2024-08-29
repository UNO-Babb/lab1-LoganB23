#MadLib.py
#Name: Logan Baardson
#Date: 8/27
#Assignment: Mad lib

def main():
  print("Madlib")
  #Ask user for words
  friend = input("enter the name of one of your friends ")
  animal = input("enter an animal ")
  location = input("enter the name of a city ")
  animal2 = input("enter an animal ")
  weapon = input("enter a type of weapon ")
  verb = input("enter a verb ")
  #Print the story with the user supplied words.
  print("One fine Sunday afternoon, your good friend", friend, "was walking his pet", animal)
  print("around", location, ". Suddenly, out of nowhere, a big, fat, angry,", animal2, "charged at", friend,"!")
  print(friend, "was absolutely terrified! Thankfully, the pet", animal, "was armed with a", weapon, "which made the", animal2, verb)
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
