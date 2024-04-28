import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import pickle
import colorama 
colorama.init()
from colorama import Fore, Style, Back
import random

# Load intent data from intents.json
with open("intents.json") as file:
    data = json.load(file)

# Load trained model, tokenizer, and label encoder
model = keras.models.load_model('chatbot_model.h5')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

# Parameters
max_len = 20

def chat():
    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        inp = input()
        if inp.lower() == "quit":
            break

        # Predict intent based on user input
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                            truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        # Check if the intent is for song recommendation
        if tag == 'song_recommendation':
            print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "What is your mood?")
            mood_response = input().lower()

            if mood_response in ["happy", "upset", "excitement", "funny", "cheerful"]:
                # Provide a song recommendation based on mood
                song_recommendations = []
                if mood_response == "happy":
                    song_recommendations.append("How about 'Pehli Dafa' by Atif Aslam?")
                elif mood_response == "upset":
                    song_recommendations.append("Maybe 'Someone Like You' by Adele?")
                elif mood_response == "funny":
                    song_recommendations.append("Maybe 'Saude Bazi' by Pritam")
                elif mood_response == "cheerful":
                    song_recommendations.append("'When the door opens' from 'Love all Play'")
                elif mood_response == "pop":
                    song_recommendations.append("How about a song from one direction?")
                elif mood_response == "kdrama-ost":
                    song_recommendations.append("It's you is a gem")
                elif mood_response == "hindi":
                    song_recommendations.append("Maybe 'Tum Hi Mera' by Pritam?")
                elif mood_response == "bollywood":
                    song_recommendations.append("Maybe 'You are my Sonia' by Sandesh, Sonu")
                    
                # Add more mood-based song recommendations here
                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "\n".join(song_recommendations))

        else:
            # Get responses based on predicted intent
            for intent in data['intents']:
                if intent['tag'] == tag:
                    print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(intent['responses']))

print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
chat()
