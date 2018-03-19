import tweepy
import json
import matplotlib.pyplot as plt
from tweepy import OAuthHandler
from os import path
from wordcloud import WordCloud


def main():
    usrinp = int(input("1. Get data, 2. Crime Word Cloud, :"))
    if usrinp == 1:
        consumer_key = 'isi ini'
        consumer_secret = 'isi ini'
        access_token = 'isi ini'
        access_secret = 'isi ini'
        
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        
        api = tweepy.API(auth)

        portal = ['detikcom', 'kompascom', 'CNNIndonesia', 'Metro_TV', 'Beritasatu', 'liputan6dotcom', 'SINDOnews', ]
        crime_text = ['begal', 'hacker', 'korupsi', 'penipuan', 'koruptor', 'komplotan', 'tewas', 'pelecehan', 'digrebek', 'curi', 'ditembak', 'pencuri', 'lapor', 'sabu', 'ganja', 'narkoba']

        text_file = open('tweets.txt', 'w')

        for i in portal:
            stuff = api.user_timeline(screen_name = i, count = 10000, include_rts = True)

            for j in stuff:
                # Process a single status            
                # text_file.write(json.dumps(j._json))
                word = j.text.lower()
                if any(ext in word for ext in crime_text):
                    text_file.write(j.text)
                    text_file.write("\n")
        text_file.close()

    elif usrinp == 2:        
        # wc_text_file = open('tweets.txt').readlines()
        wc_text_file = open('crime_news.txt').read()
        wc = WordCloud().generate(wc_text_file)

        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")

        plt.show()

if __name__ == '__main__':
    main()
