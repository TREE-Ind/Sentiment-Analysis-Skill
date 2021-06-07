from mycroft import MycroftSkill, intent_file_handler


class SentimentAnalysis(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('analysis.sentiment.intent')
    def handle_analysis_sentiment(self, message):
        self.speak_dialog('analysis.sentiment')


def create_skill():
    return SentimentAnalysis()

