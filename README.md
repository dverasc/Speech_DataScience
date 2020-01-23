# SpeechWordCloud_DataScience

This project was mainly me playing around with the WordCloud library. I found a text file with a bunch of Trump speeches together but I ran into a couple issues from the begining. It was a .txt file and pandas only opens csv files so I had to play around with Excel several times to get it into a csv format. During this process, I realized Excel had cell limits for characters so I wouldnt be able to put all the speeches into one cell in a comma format. 

This meant I had to split each speech into a separate CSV file which involved cutting and pasting from notepad to an Excel sheet, using TextJoin to put all the words together in one cell and then finding all the spaces and replacing them with commas. There were 10+ speeches in the original txt file so I stopped at the 3rd speech since it was the funniest (it was about his hands).
