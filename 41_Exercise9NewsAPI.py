import requests
from win32com.client import Dispatch


def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    api_key = "" #Your newsapi.org api key
    country = "in" #Your country code
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"

    news = requests.get(url).json()
    articles = news["articles"]

    my_articles = []
    numbers = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight", "Ninth", "Tenth"]
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news += f"{numbers[i]} news is : {my_articles[i]} \n"

    print(my_news)
    speak(my_news)