import tweepy
import json
import matplotlib.pyplot as plt
from tweepy import OAuthHandler
from os import path
from wordcloud import WordCloud
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


def main():
    usrinp = int(input("1. Get data, 2. Crime Word Cloud, :"))
    if usrinp == 1:
        consumer_key = 'fLnf3WIuilQI8XDAy36L4HCXp'
        consumer_secret = 'Qi2rtmYVSm1t6ATC7J4McALCHgXHGLUnWgoHHBvU4q9JQraiCv'
        access_token = '255792021-VQMmhleyYXcLGXXFXcf3cGwkM0FCKOKpwBpxe6fb'
        access_secret = '1RpbrPaaSd92x8dNt0wupVNx0MsyGqSxsfqRmIu44XcSN'
        
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        
        api = tweepy.API(auth)

        portal = ['detikcom', 'kompascom', 'CNNIndonesia', 'Metro_TV', 'Beritasatu', 'liputan6dotcom', 'SINDOnews', ]
        crime_text = ['begal', 'hacker', 'korupsi', 'tipu', 'koruptor', 'tewas', 'leceh', 'seksual', 'curi', 'tembak', 'curi', 'sabu', 'ganja', 'narkoba']

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
        wc_text_file = open('crime_news.txt').readlines()
        factory_stem = StemmerFactory()
        stemmer = factory_stem.create_stemmer()
        
        factory_stop = StopWordRemoverFactory()
        stopword = factory_stop.create_stop_word_remover()
        
        for i in wc_text_file:
            output_stem = stemmer.stem(i)
            output_stop = stopword.remove(output_stem)

            print(output_stop)
        # wc = WordCloud().generate(output_stop)

        # plt.imshow(wc, interpolation='bilinear')
        # plt.axis("off")

        # plt.show()

if __name__ == '__main__':
    main()