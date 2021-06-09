from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus import Message
from textblob import TextBlob


class SentimentAnalysis(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.add_event('recognizer_loop:utterance', self.handle_sentiment)
        
        self.add_event('speak', self.handle_ai_sentiment)
    
    def handle_sentiment(self, message):
        senti = str(message.data.get('utterances'))
        #senti = message.data.get('utterance')
        senti = TextBlob(senti)
        senti = senti.sentiment.polarity
        print(senti)
        self.bus.emit(Message("sentiment",{"data": senti} ))
        
    def handle_ai_sentiment(self, message):
        senti = str(message.data.get('utterance'))
        senti = TextBlob(senti)
        senti = senti.sentiment.polarity
        self.bus.emit(Message("sentiment",{"data": senti} ))
        


def create_skill():
    return SentimentAnalysis()

