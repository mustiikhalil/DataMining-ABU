import indicoio
import Auth as auth 
import pandas as pd

indicoio.config.api_key = auth.emotionsAPI

def getEmotions(arrayOfEmotions):
    return indicoio.emotion(arrayOfEmotions)


def detect(tweets,tweet_timestamp,ids,batch_Emotion,filename):
    book = pd.DataFrame(columns=['ID','timestamp','anger','joy','sadness','fear','surprise'])
    get_Batch_Data = len(tweets)
    start = 0
    end = get_Batch_Data/batch_Emotion
    diff = end - start
    for i in range(0,batch_Emotion):
        if end > len(tweets):
            break
        to_predict_id = ids[start:end]
        to_predict_timestamp = tweet_timestamp[start:end]
        to_predict = tweets[start:end]
        emotions = getEmotions(to_predict) # takes an array of emotions
        for i in range(0,len(to_predict)):
            book = book.append({'ID': to_predict_id[i],'timestamp': to_predict_timestamp[i],
                                'anger':emotions[i]['anger'],'joy':emotions[i]['joy'],'sadness':emotions[i]['sadness'],
                                'fear':emotions[i]['fear'],'surprise':emotions[i]['surprise']}, ignore_index=True)
        start += diff
        end += diff
    book.to_csv(filename, encoding='utf-8', index=False)

# book = book.append({'ID': tweet.id,'Tweet': " ".join(tweet.text.split()),'Timestamp':timestamp,"date":date}, ignore_index=True)
# book.to_csv(filename, encoding='utf-8', index=False)