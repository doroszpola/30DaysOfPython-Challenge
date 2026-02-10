# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

########################
# reading
########################

f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)

line = f.readline()
print(line)

f.close()

f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()


#############################
# automatic closing of files by using 'with'
#############################

with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


########################
# writing/updating
########################

with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')


######################
# delete files
######################

# import os
# os.remove('./files/example.txt')

# import os
# if os.path.exists('./files/example.txt'):
#     os.remove('./files/example.txt')
# else:
#     print('The file does not exist')



#######################
# file types
#######################


# dictionary
person_dct= {
    "name":"Pola",
    "country":"Poland",
    "city":"Łódź",
    "skills":["Java","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Pola', 'country': 'Poland', 'city': 'Łódź', 'skills': ['Java', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Pola",
    "country":"Poland",
    "city":"Łódź",
    "skills":["Java","Python"]
}'''


# changing JSON to a dictionary

import json
# JSON
person_json = '''{
    "name":"Pola",
    "country":"Poland",
    "city":"Łódź",
    "skills":["Java","Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

#changing dictionary to a JSON

person_dct= {
    "name":"Pola",
    "country":"Poland",
    "city":"Lodz",
    "skills":["Java","Python"]
}

person_json = json.dumps(person_dct, indent=4) # indent is here for aesthetic purposes XD
print(type(person_json))
print(person_json)


# saving as a JSON file

import json
# python dictionary
person = {
    "name":"Pola",
    "country":"Poland",
    "city":"Lodz",
    "skills":["Java","Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


# CSV

import csv

with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter= ',')
    line_count = 0 

    for row in csv_reader:
        if line_count==0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print( f'\t{row[0]} is a student. She lives in {row[2]}, and her skill is {row[3]}')
            line_count += 1
    print(f'Number of lines: {line_count}')

# reading excel files

# import xlrd

# excel_book = xlrd.open_workbook('sample.xlsx')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)


#XML

import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)



###################################
# exercise
###################################


with open('./files/countries_data.json', 'r', encoding='utf-8') as j:
    countries_data = json.load(j)

#print(countries_data)

def top_10_populated_countries(data):

    top_10 = sorted(data, key=lambda x: x['population'], reverse = True)[:10] #sortowanie według lambdy czyli populacji

    for country in top_10:
        print(country['name'], country['population'])

top_10_populated_countries(countries_data)



def top_languages(data,amount):
    spoken_languages = {}
    for country in data:
        for language in country['languages']:
            if language not in spoken_languages:
                spoken_languages[language] = 1
            else:
                spoken_languages[language] += 1

    top_10_spoken_languages = dict(sorted(spoken_languages.items(), key=lambda item: item[1], reverse=True )[:amount])
    print(top_10_spoken_languages)

top_languages(countries_data,3)


######################################################

# emails

import re
from collections import Counter

with open('./files/email_exchanges.txt', 'r') as e:
     email_file = e.read()

email_list = re.findall(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+', email_file, re.I)

print(email_list)


#most common words

def find_most_common_words(filepath, how_many):
    with open(filepath, 'r') as file:
        read_file = file.read()
    words = re.findall(r'\b[A-Za-z]+\b',read_file)  #start at word boundary collect all A-Z, a-z, 0-9, _ characters and end on another boundary
    counts = Counter(words).most_common(how_many)

    return counts

print(find_most_common_words('./files/email_exchanges.txt', 5))


# text similarity

import string

stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def clean_text(text):
    clean_text = re.sub(f"[{re.escape(string.punctuation + string.digits)}]", "", text)
    clean_text = clean_text.lower()
    return text

def remove_support_words(text, support_words):
    text = text.split()
    filtered_text = [word for word in text if word not in support_words]
    final_text = "".join(filtered_text)
    return final_text 

def check_text_similarity(text1, text2):
    
    text1 = set(text1.split())
    text2 = set(text2.split())    

    intersection = text1.intersection(text2)
    union = text1.union(text2)

    if not union:  # if there is no words
        return 0.0 

    return len(intersection)/len(union) # 1 means identical 0 means completely different


with open('./files/michelle_obama_speech.txt', 'r') as michelle:
    michelle_speech = michelle.read()

with open('./files/melina_trump_speech.txt', 'r') as melina:
    melina_speech = melina.read()

clean_text(michelle_speech)
clean_text(melina_speech)

remove_support_words(michelle_speech,stop_words)
remove_support_words(melina_speech,stop_words)

print(check_text_similarity(michelle_speech,melina_speech))


# counting lines


with open('./files/hacker_news.csv', encoding = 'utf-8') as h:
    hacker_news = csv.reader(h, delimiter= ',')
    

    line_counter = 0

    for row in hacker_news:
        if bool(re.findall(r'\b[Pp]ython\b', str(row))):
            line_counter +=1

    print(line_counter)

