import pandas as pd
import math

def word_probability(word, sentiment):
    global posible_senitments, word_review, sentiment_counter, words_per_sentiment

    if word not in word_review:
        word_count = 0
    else:
        word_count = word_review[word][sentiment]

    total_words = words_per_sentiment[sentiment]
    vocabulary_size = len(word_review)

    return (word_count + 1) / (total_words + vocabulary_size )

print("Loading...")

str_text = "text"
str_sentiment = "airline_sentiment"
posible_senitments = ["positive", "neutral", "negative"]
chars_to_remove = ['.', ',', '!', '?']
training_data_procentage = 0.85
word_review = {}
sentiment_counter = {}
sentiment_probability = {}
words_per_sentiment = {}

data = pd.read_csv("Reviews.csv")
data = data[[str_text, str_sentiment]]


training_data_index = int(len(data) * training_data_procentage)


# training




for index, row in data.loc[:training_data_index].iterrows():
    sentiment = row[str_sentiment]  
    text = row[str_text]

    if sentiment not in sentiment_counter:
        sentiment_counter[sentiment] = 0
    sentiment_counter[sentiment] += 1
    
    if sentiment not in words_per_sentiment:
        words_per_sentiment[sentiment] = 0

    text = text.lower()
    for ch in chars_to_remove:
        text = text.replace(ch, '')
    words = text.split()

    words_per_sentiment[sentiment] += len(words)


for sentiment in posible_senitments:
    sentiment_probability[sentiment] = sentiment_counter[sentiment] / training_data_index

for index, row in data.loc[:training_data_index].iterrows():
    text = row[str_text]
    sentiment = row[str_sentiment]  

    text = text.lower()
    for ch in chars_to_remove:
        text = text.replace(ch, '')
    words = text.split()
    
    for word in words:
        if word not in word_review:
            word_review[word] = {}

            for sentiment_option in posible_senitments:
                word_review[word][sentiment_option] = 0
        
        word_review[word][sentiment] += 1



# testing

good_guesses = 0
total_guesses = len(data) - training_data_index
  
for index, row in data.loc[training_data_index:].iterrows():
    text = row[str_text]
    actual_sentiment = row[str_sentiment]  

    text = text.lower()
    for ch in chars_to_remove:
        text = text.replace(ch, '')
    words = text.split()

    sentiment_likelihood = {}

    for sentiment in posible_senitments:
        sentiment_likelihood[sentiment] = math.log(sentiment_probability[sentiment])

        for word in words:
            sentiment_likelihood[sentiment] += math.log(word_probability(word, sentiment))
 
    probability = -math.inf
    verdict = None

    for sentiment in posible_senitments:
        if sentiment_likelihood[sentiment] > probability:
            probability = sentiment_likelihood[sentiment]
            verdict = sentiment

    # if verdict == "positive":
    #     print(text)   

    if verdict == actual_sentiment:
        good_guesses += 1


# print(data)
  
acuracy = good_guesses / total_guesses

print("acuracy is", acuracy)



# user input

print("try your input:")
try_custom = 1

if try_custom:
    # review = input()
    text = "the flying assistent was very cold, i was very frightened and she just told me to calm down. That didn't help, 1/5 starts"      # add input here

    text = text.lower()
    for ch in chars_to_remove:
        text = text.replace(ch, '')
    words = text.split()

    sentiment_likelihood = {}

    for sentiment in posible_senitments:
        sentiment_likelihood[sentiment] = math.log(sentiment_probability[sentiment])

        for word in words:
            sentiment_likelihood[sentiment] += math.log(word_probability(word, sentiment))
 
    probability = -math.inf
    verdict = None

    for sentiment in posible_senitments:
        if sentiment_likelihood[sentiment] > probability:
            probability = sentiment_likelihood[sentiment]
            verdict = sentiment

    print("I belive your review is a", verdict, "review")