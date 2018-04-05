import tweepy
from kafka import SimpleProducer, KafkaClient
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

access_token = "255792021-VQMmhleyYXcLGXXFXcf3cGwkM0FCKOKpwBpxe6fb"
access_token_secret =  "1RpbrPaaSd92x8dNt0wupVNx0MsyGqSxsfqRmIu44XcSN"
consumer_key =  "fLnf3WIuilQI8XDAy36L4HCXp"
consumer_secret =  "Qi2rtmYVSm1t6ATC7J4McALCHgXHGLUnWgoHHBvU4q9JQraiCv"

class StdOutListener(tweepy.StreamListener):
    def on_status(self, status):
        crime_text = ['begal', 'hacker', 'korupsi', 'tipu', 'koruptor', 'tewas', 'leceh', 'seksual', 'curi', 'tembak', 'curi', 'sabu', 'ganja', 'narkoba', 'rt']

        factory_stem = StemmerFactory()
        stemmer = factory_stem.create_stemmer()
        
        factory_stop = StopWordRemoverFactory()
        stopword = factory_stop.create_stop_word_remover()
        

        output_stem = stemmer.stem(status.text)
        output_stop = stopword.remove(output_stem)

        producer.send_messages("news", output_stop.encode('utf-8'))
        if any(ext in output_stop for ext in crime_text):
            producer.send_messages("newscrime", output_stop.encode('utf-8'))
        print (output_stop)
        return True
    def on_error(self, status_code):
        print (status_code)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

stream_listener = StdOutListener()
stream = tweepy.Stream(api.auth, listener = stream_listener)
stream.filter(track=["detikcom", "kompascom", "CNNIndonesia", "Metro_TV", "Beritasatu", "liputan6dotcom", "SINDOnews", ])