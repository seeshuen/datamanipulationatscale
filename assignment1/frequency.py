import sys
import json

def main():
  tweet_file = open(sys.argv[1])
  term_counts = {}
  total_count = 0

  for line in tweet_file:
    tweet_json = json.loads(line)
    if 'text' in tweet_json:
      tweet_text = tweet_json['text'].lower().encode('utf-8')
      tweet_terms = tweet_text.split()
      for term in tweet_terms:
        if term_counts.has_key(term):
          term_counts[term] =  term_counts[term] + 1;
        else:
          term_counts[term] = 1
        total_count = total_count + 1

  for word in term_counts.keys():
    print word, " ", float(term_counts[word])/total_count



if __name__ == '__main__':
  main()