import sys
import json
import types
import operator

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  state_scores = {}
  scores_dic = build_scores_dictionary(sent_file)

  for line in tweet_file:
    tweet_sentiment = 0
    tweet_json = json.loads(line)
    if 'text' in tweet_json:
      #print tweet_json['text']
      terms = tweet_json['text'].lower().split()
      for term in terms:
	    if scores_dic.has_key(term):
		  tweet_sentiment = tweet_sentiment + scores_dic[term]
		  
      #print tweet_sentiment
      # check if place is available			
      if 'place' in tweet_json and type(tweet_json['place']) is not types.NoneType:
        # check if full name of the place is available
		if 'full_name' in tweet_json['place'] and type(tweet_json['place']['full_name']) is not types.NoneType:
		  # check if the country code of the place is available
		  if 'country_code' in tweet_json['place'] and type(tweet_json['place']['country']) is not types.NoneType:
		    # check if it is in the US
			if tweet_json['place']['country'] == 'United States':
			  full_name = tweet_json['place']['full_name'].encode('utf-8')
			  full_name_terms = full_name.split()
			  # statue is always at last
			  state = full_name_terms[-1]
			  # assume state is a two letter identifier
			  if len(state) == 2:
			    if scores_dic.has_key(state):
			      state_scores[state] = state_scores[state] + tweet_sentiment
			    else:
			      state_scores[state] = tweet_sentiment				
						
  #for state in state_scores.keys():
  #  print state, " ", state_scores[state]
    						
  sorted_states = sorted(state_scores.items(), key=operator.itemgetter(1))
  print sorted_states[-1][0]	
										
def build_scores_dictionary(sent_file):
    "Build the score dictionary"
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores
    
if __name__ == '__main__':
	main()