#MadLib.py
#Name: Logan Baardson
#Date: 8/27
#Assignment: Mad lib

def main():
  print("Madlib")
  #Ask user for words
  friend = input("enter the name of one of your friends ")
  animal = input("enter an animal ")
  noun = input("enter a noun ")
  animal2 = input("enter an animal ")
  adjective = input("enter an adjective ")
  verb = input("enter a verb ")
  #Print the story with the user supplied words.
  print("one fine Sunday afternoon, your good friend", friend, "was walking his pet", animal)
  print("around a", noun, ". Suddenly, out of nowhere, a big, fat, angry,", animal2, "charged at", friend,"!")
  print(friend, "was absolutely terrified! Thankfully, the", animal, "was very", adjective, "which made the", animal2, verb)
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
