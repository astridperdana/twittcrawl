import tweepy
import json
from tweepy import OAuthHandler


def main():
    consumer_key = 'fLnf3WIuilQI8XDAy36L4HCXp'
    consumer_secret = 'Qi2rtmYVSm1t6ATC7J4McALCHgXHGLUnWgoHHBvU4q9JQraiCv'
    access_token = '255792021-VQMmhleyYXcLGXXFXcf3cGwkM0FCKOKpwBpxe6fb'
    access_secret = '1RpbrPaaSd92x8dNt0wupVNx0MsyGqSxsfqRmIu44XcSN'
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    api = tweepy.API(auth)

    portal = ['detikcom', 'kompascom', 'CNNIndonesia', 'Metro_TV', 'Beritasatu', 'liputan6dotcom', 'SINDOnews', ]

    text_file = open('tweet.json', 'w')

    for i in portal:
        stuff = api.user_timeline(screen_name = i, count = 100, include_rts = True)

        for j in stuff:
            # Process a single status            
            text_file.write(json.dumps(j._json))
            text_file.write("\n")
    
    text_file.close()        


if __name__ == '__main__':
    main()