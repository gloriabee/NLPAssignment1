
import re
import nltk
from textblob import TextBlob
from tabulate import tabulate

# Download punkt and punkt_tab resources
nltk.download('punkt')
nltk.download('punkt_tab')

nltk.data.path.append('E:/NLP/nltk_data')

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')
except LookupError as e:
    print(f"Resource not found: {e}")

#load text from a file
def load_text(file_path):
    with open(file_path) as file:
        return file.read()
    
#clean text by converting into lowercase and removing non-alphabetic characters.
def clean_text(text):
    text=text.lower() #convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters and digits
    return text

#tokenize into sentence and words
def tokenize(text):
    blob=TextBlob(text)
    return blob.words

#find the top 10 frequent words and count
def get_top_10_words(words,n=10):
    freq=nltk.FreqDist(words)
    return freq.most_common(n)

#format table of top 10 words
def format_top_words_table(top_words):
    headers=["Rank","Word","Count"]
    table_data=[[i+1,word,count] for i, (word,count) in enumerate(top_words)]
    return tabulate(table_data,headers=headers,tablefmt="pretty")

#save with file
def save_to_file(filename,content):
    with open(filename,'w') as file:
        if isinstance(content,list):
            file.write('\n'.join(content))  # Join list elements with newlines
        else:
            file.write(content)

def main():
    #speicify the input file path
    input_file='./alice29.txt'

    #load text
    text=load_text(input_file)

    #clean the text
    cleaned_text=clean_text(text)
    save_to_file('cleaned.txt',cleaned_text)

    #tokenize words
    words=tokenize(cleaned_text)
    save_to_file('words.txt',words)

    #get top 10 frequent words
    top_words=get_top_10_words(words,n=10)
    top_words_content=format_top_words_table(top_words)
    save_to_file('top10words.txt',top_words_content)


    
if __name__ == "__main__":
    main()
