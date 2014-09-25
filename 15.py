sentence = raw_input("Enter sentence: ").strip()
wordcount = 0
if not sentence == "":
    wordcount += 1
for letter in sentence:
    if letter == " ":
        wordcount += 1
    if letter == ".":
        break
print("There are {} words in the input".format(wordcount))
