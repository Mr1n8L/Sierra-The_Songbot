How to run:
open terminal one:
python chatbot_training.py
---> Run chatbot_training.py: Run chatbot_training.py to preprocess the 
data, train the model, and save the necessary objects

open terminal two:
python chat.py
---> Run chat.py: Finally, run chat.py to start the chat interface


if genre_response == "pop":
                    print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "How about 'Shape of You' by Ed Sheeran?")
                elif genre_response == "rock":
                    print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "Maybe 'Stairway to Heaven' by Led Zeppelin?")
                elif genre_response == "hindi":
                    print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "Maybe 'Tu Hi Mera' by Pritam Chakraborty?")
                elif genre_response == "bollywood":
                    print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "Maybe 'jhumka Gira Re' by Dilpreet Dhillon")