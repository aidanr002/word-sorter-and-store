words_unsorted = []
f = open('words.txt','r')
opened_file = f
for word in opened_file:
    word = word.strip()
    words_unsorted.append(word)
f.close()
print (words_unsorted)
user = input('Enter new word: ')
while user != 'exit':
    if user =='sort':
        words_unsorted.sort()
        for words in words_unsorted:
            print (words)
    else:
        words_unsorted.append(user)
    user = input('Enter new word: ')
f = open('words.txt', 'w') #Opens the file to write- will over ride all other information in the file.
words_unsorted.sort()
for words in words_unsorted:
    print(word, file=f)
f.close() #Closes file
