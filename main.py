
# def count_words(words):
#   word_list = words.split()
#   count =0
#   for word in word_list:
#       count += 1
#   return(count)
# def count_characters(text):
#   text = text.lower()
#   my_dict ={}
#   for char in text:
#     if char not in my_dict:
#       my_dict[char] =1
#     else:
#       my_dict[char] +=1
#   return my_dict
def report(text):
  my_dict = {}
  text=text.lower()
  for char in text:
    if char.isalpha() :
      if char in my_dict:
        my_dict[char] +=1
      else:
        my_dict[char] =1
  char_list =[]
  for char, count in my_dict.items():
    char_list.append({"char":char,"num":count})
  def sort_on(dict):
    return dict["num"]
  char_list.sort(reverse=True,key=sort_on)

  print("--- Begin report of books/frankenstein.txt ---")
  words = text.split()
  word_count =len(words)
  print(f"{word_count} words found in the document\n")
  for item in char_list:
    print(f"The '{item['char']}' character was found {item['num']} times")
  print(("--- End report ---"))
with open("books/frankenstein.txt") as f:
  file_contents = f.read()
report(file_contents)