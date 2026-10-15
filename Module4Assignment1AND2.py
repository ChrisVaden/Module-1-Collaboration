import re

# 17.4 
mammoth = """
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go,
To the great Provincial show,
To be admired by many a beau,
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
"""

# 17.5 
words_c = re.findall(r'\b[cC]\w*', mammoth)
print("17.5 Words beginning with c:", words_c)

# 17.6 
four_letter_c = re.findall(r'\b[cC][a-zA-Z]{3}\b', mammoth)
print("17.6 Four-letter words beginning with c:", four_letter_c)

# 17.7 
words_r = re.findall(r'\b\w+r\b', mammoth)
print("17.7 Words that end with r:", words_r)

# 17.8 
three_vowels = re.findall(r'\b\w*[aeiouAEIOU]{3}\w*\b', mammoth)
print("17.8 Words with three vowels in a row:", three_vowels)

# 20.1 
current_files = os.listdir('.')
print("20.1 Files in current directory:")
print(current_files)
print("-" * 40)

# 20.2 
parent_files = os.listdir('..')
print("20.2 Files in parent directory:")
print(parent_files)
print("-" * 40)

# 20.3 
test1 = "This is a test of the emergency text system"
with open('test.txt', 'wt') as fout:
    fout.write(test1)
print("20.3 Successfully wrote text1 to 'test.txt'.")
print("-" * 40)

# 20.4 
with open('test.txt', 'rt') as fin:
    test2 = fin.read()

are_they_same = (test1 == test2)
print("20.4 Are test1 and test2 the same?", are_they_same)
print(f"test1: {test1}")
print(f"test2: {test2}")