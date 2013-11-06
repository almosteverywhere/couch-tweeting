#!/usr/bin/python
import twitter
import argparse

api = twitter.Api(consumer_key='xmDTWUuqFSwbNEHRjwB9w',

    consumer_secret='YqYWz0ibhjQcjT3HQvq4OoiVLA5oeYM5tnSAiDJhA', access_token_key='1553700698-Z2jb0LAIKERaiv5nmTxg515ZAKEwBffHvl0f3Mb', 
    access_token_secret='V4zS5zdKgcKwSghWKuDJBtaY84a9Un7fBTNwn1hUsotFz') 

def parse_args():
    parser = argparse.ArgumentParser(description="Post something to twitter!")
    parser.add_argument('status', metavar='status',
                        help='What do you want to say?')
    
    opts = parser.parse_args()
    if not (opts.status):
        parser.error("You have to specify a message to post!")
    return opts

def main():
    opts = parse_args()
    message = api.PostUpdate(opts.status)
    print message
    

if __name__ == '__main__':
    main()






# ok we just want to authorize every time and post tweets. 
# so what we need is to get args and just 