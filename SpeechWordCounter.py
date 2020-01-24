import pandas as pd
file = open(r"C:\Users\dveras\Documents\trump-speeches\speeches.txt", encoding='utf8')
book = file.read()

def tokenize():
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None
    
def map_book(tokens):
    hash_map = {}
    
    if tokens is not None:
        for element in tokens:
            word = element.replace(",","")
            word = word.replace(".","")
            
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1
                
        return hash_map
    else:
        return None
    
    
words = tokenize()
word_list = ['clinton','hands','president','obama','great']
#count_list = [map[word_list[0]]]
                  
print(count_list)
##df = pd.DataFrame(word_list)


map = map_book(words)

data = {'Word':[word_list[0],word_list[1],word_list[2],word_list[3],word_list[4]], 'Count': [map[word_list[0]],map[word_list[1]],map[word_list[2]],map[word_list[3]],map[word_list[4]] ] }

df = pd.DataFrame(data)
df

#for word in word_list:
 #   print('Word: [' + word + '] Frequency: ' + str(map[word]))
