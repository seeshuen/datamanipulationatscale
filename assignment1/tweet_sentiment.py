import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores_dic = build_scores_dictionary(sent_file);
    
    # traverse the input file
    for line in tweet_file:
        tweet_json = json.loads(line)
        if 'text' in tweet_json:
            tweet = tweet_json['text'].lower()
            print_tweet_score(tweet, scores_dic)
        
def build_scores_dictionary(sent_file):
    "Build the score dictionary"
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores
    
def print_tweet_score(tweet, scores_dic): 
    words = tweet.split()
    score = 0
    for word in words:
        if word in scores_dic:
            score += scores_dic[word]
    print score
    

if __name__ == '__main__':
    main()
