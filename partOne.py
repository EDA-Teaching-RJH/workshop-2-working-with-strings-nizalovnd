def main():
    slow = input("Input ")
    myFunction(slow)

def myFunction(text):
  word_list = text.split(" ")
  new_string = "a".join(word_list)
  print(new_string)
main()
