import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    tweet_list = build_tweet_list(tweet_file)
    scores_dic = build_scores_dictionary(sent_file)
    
    new_term_scores = {} # list of scores recorded for this new terms
    
    # iterate all tweets
    for index in range(len(tweet_list)):
        if tweet_list[index].has_key("text"):
            tweet_words = tweet_list[index]["text"].split()
            sent_score = 0
            new_terms_in_tweet = []  # new terms in this tweet 

            # iterate this tweet twice, first time to get the scores of included terms
            for word in tweet_words:

                if word.encode('utf-8') in scores_dic.keys():
                    sent_score = sent_score + scores_dic[word]
                else:    
                    # initialize list for this word if it is not found in any tweet before
                    if word not in new_term_scores:
                        new_term_scores[word] = []
                    # record new terms in tweet, one can appear multiple times    
                    new_terms_in_tweet.append(word)

            # second time to add the scores for non-included terms
            for word in new_terms_in_tweet:
                new_term_scores[word].append(sent_score)
                
    # now calculate and output scores of each new term       
    for word in new_term_scores.keys():

        total_score = 0
        for score in new_term_scores[word]:
            #total_score += score
            if score > 0 :
                total_score += 1
            elif score < 0: 
                total_score -= 1
                  
        term_score = float(total_score)/len(new_term_scores[word])
        
        term_score = "%.3f" %term_score
        print word.encode('utf-8') + " " + term_score                 
                
def build_scores_dictionary(sent_file):
    "Build the score dictionary"
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def build_tweet_list(twit_file):  
    "Build the tweet dictionary"

    twitter_list = []
    for line in twit_file:
        twitter_list.append(json.loads(line))
    return twitter_list
    
if __name__ == '__main__':
    main()
