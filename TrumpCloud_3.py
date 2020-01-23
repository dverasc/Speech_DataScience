from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

#df = pd.read_table(r"C:\Users\dveras\Documents\trump-speeches\transformed.csv")
df = pd.read_table(r"C:\Users\dveras\Documents\trump-speeches\speeches1.csv")
df1 = pd.read_table(r"C:\Users\dveras\Documents\trump-speeches\speech2.csv")
df2 = pd.read_table(r"C:\Users\dveras\Documents\trump-speeches\speech3.csv")
#print(df)
#file_content=open(r"C:\Users\dveras\Documents\trump-speeches\speeches1.txt").read()
#text_file = open(r"C:\Users\dveras\Documents\trump-speeches\speeches.txt", "r")
#lines = text_file.readlines()
#print(len(lines))
#text_file.close()
                 
print("Success")

######1st Speech########
comment_words = ''
stopwords = set(STOPWORDS)

for val in df:
    val = str(val)
    
    tokens = val.split()
    
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        
    for words in tokens:
        comment_words = comment_words + words + ' '
        
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 

######2ndspeech#########
comment_words = ''
stopwords = set(STOPWORDS)

for val in df1:
    val = str(val)
    
    tokens = val.split()
    
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        
    for words in tokens:
        comment_words = comment_words + words + ' '
        
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 

#######3rdSpeech########
comment_words = ''
stopwords = set(STOPWORDS)

for val in df2:
    val = str(val)
    
    tokens = val.split()
    
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        
    for words in tokens:
        comment_words = comment_words + words + ' '
        
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 
