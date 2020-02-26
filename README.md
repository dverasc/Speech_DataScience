# SpeechWordCloud_DataScience

This project was mainly me playing around with the WordCloud library. I found a text file with a bunch of Trump speeches together but I ran into a couple issues from the begining. It was a .txt file and pandas only opens csv files so I had to play around with Excel several times to get it into a csv format. During this process, I realized Excel had cell limits for characters so I wouldnt be able to put all the speeches into one cell in a comma format. 

This meant I had to split each speech into a separate CSV file which involved cutting and pasting from notepad to an Excel sheet, using TextJoin to put all the words together in one cell and then finding all the spaces and replacing them with commas. There were 10+ speeches in the original txt file so I stopped at the 3rd speech since it was the funniest (it was about his hands).


The word counter file takes in the txt file with all the speeches together, splits and tokenizes the words, and then counts the amount of time the words designated in the list occur (see the variable "word_list"). It then creates a dataframe with the word in one column and the frequency in the other.


The Bernie file is similar to the Trump word cloud in terms of the code and the overall purpose, but the data came from a Kaggle dataset of all the Democratic debate speeches from all the candidates. I filtered out all the transcripts to only show the Bernie ones and then followed a similar concatenate process in a new csv sheet to put all of bernie's moments in one cell. From looking at the word cloud, one can see that overall his message during the debate has centered around defeating Donald Trump (which makes sense intuitively)
