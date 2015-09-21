import json
import sys
import operator

def topTenHashTags(tweet_file):
    hashTagToCount = {}
    for line in tweet_file:
        tweet_json=json.loads(line)
        if tweet_json.has_key("entities") and tweet_json["entities"] is not None:
            if tweet_json["entities"]["hashtags"] is not None and len(tweet_json["entities"]["hashtags"]) > 0:
                for hashTagItem in tweet_json["entities"]["hashtags"]:
                    hashTagText=hashTagItem["text"].lower()
                    if hashTagToCount.has_key(hashTagText):
                        hashTagToCount[hashTagText] += 1
                    else:
                        hashTagToCount[hashTagText] = 1
                        
    #for hashtag in hashTagToCount.keys():
    #    print hashtag, " ", hashTagToCount[hashtag]           
        
    sorted_hashtags = sorted(hashTagToCount.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(0, 10):
        item=sorted_hashtags[i]
        print item[0], " ", item[1]

def main ():
    tweet_file = open(sys.argv[1])
    topTenHashTags(tweet_file)

if __name__ == '__main__':
    main()