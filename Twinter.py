import twint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def run_twint(term):
    analyzer = SentimentIntensityAnalyzer()
    c = twint.Config()
    c.Search = term
    c.Limit = 2   # Sets of 20
    c.Lang = 'en'
    c.Show_hashtags = True
    c.Links = 'exclude'
    c.Media = False
    c.Videos = False
    c.Images = False
    c.Format = "{tweet} {hashtags}"
    c.Hide_output = True
    c.Store_object = True
    twint.run.Search(c)

    sample = ""
    for tweet in twint.run.output.tweets_list:
        sample += f'> {tweet.username.upper()}:\n{tweet.tweet} \n\n'

    score = int(analyzer.polarity_scores(sample)['compound'] * 100)
    twint.run.output.tweets_list.clear()

    return [score, sample]
