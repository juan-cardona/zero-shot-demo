import twint


def twint_to_pandas(columns):
    return twint.output.panda.Tweets_df[columns]


def extract_tweets(topic: str):
    # Configure
    c = twint.Config()
    c.Search = topic
    # Custom output format
    c.Limit = 1
    c.Pandas = True
    twint.run.Search(c)
    df = twint_to_pandas(
        ["date", "username", "tweet", "hashtags", "nlikes"])
    print('here should be rigth')
    return df
