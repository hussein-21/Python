# Name: Hussein Alsaidi
# Date: 02/08/2023
# Description: This is part 6 of Homework #2.

letter = str(input('Enter a letter: '))
sentence = str(input('Enter a sentence: '))
print('the length of the sentence is', len(sentence), 'letters')
print("The length of the sentence is",len(sentence) - sentence.count(" "), "characters without spaces")
word_count = len(sentence.split())
print("The are",word_count,"word(s) in the sentence.")
reverse= sentence[::-1]
print("The sentence in complete reverse is", reverse)
count_letter = sentence.count(letter)
print("There is",count_letter,"occurence of",letter,"in the sentence")





