#!/usr/bin/python
import twitter
import argparse

api = twitter.Api(consumer_key='YOURKEY',

    consumer_secret='YOURSECRET', access_token_key='YOURKEY', 
    access_token_secret='YOURSECRET') 

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
