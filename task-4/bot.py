import os
import telebot
import requests
import json
import csv
from dotenv import load_dotenv, find_dotenv

# TODO: 1.1 Get your environment variables 
from variables import botApiKey, webApiKey

load_dotenv(find_dotenv())
botApiKey = os.getenv('botApiKey')
webApiKey = os.getenv('webApiKey')
bot = telebot.TeleBot(botApiKey)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    botRunning = True
    # TODO: 1.2 Get movie information from the API
    moviename = message.text.replace("/movie ", '')
    # print(moviename)
    response = requests.get("http://www.omdbapi.com/?apikey={your_key}&t={movie_name}".format(your_key = webApiKey, movie_name = moviename))
    apidict = json.loads(response.text)
    if "Error" in apidict.keys():
        bot.reply_to(message, "Movie not found!, Please check the name of the movie provided.")

    # TODO: 1.3 Show the movie information in the chat window
    else:
        movieinfo = "Title: " + apidict["Title"] + "\nRated " + apidict["Rated"] + "\nGenre: " + apidict["Genre"] + "\n" + apidict["Plot"]
        posterinfo = apidict["Poster"]
        bot.reply_to(message, movieinfo)
        try:
            bot.send_photo(message.chat.id, photo = posterinfo)
        except:
            bot.send_message(message.chat.id, text = "The Poster could not be sent due to a broken link ig?\N{sneezing face}")

    # TODO: 2.1 Create a CSV file and dump the movie information in it
    if os.path.exists("movies.csv") == False:
        file = open("tasks/task-4/movies.csv", "w")
        ww = csv.writer(file)
        ww.writerow(apidict.keys())
        file.close()

    with open("movies.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(apidict.values())


@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    sentcsv = open("movies.csv", 'rb')
    bot.send_document(message.chat.id, sentcsv)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.polling()
