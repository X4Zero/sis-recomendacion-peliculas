import pandas as pd

#https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
df = pd.read_csv('lang.txt',sep='\t')
df_languages = df.iloc[:,[1,2,3,]] 
df_languages.to_csv('languages.csv',index=False)