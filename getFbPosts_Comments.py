#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:43:19 2017

@author: yapxiuren

Description: This script gets the comments of the post and runs a sentiment analysis on each,
and creates a dataframe with:
    length of comment
    comment
    magnitude
    score
    date
"""
import numpy as np
import pandas as pd
import requests
from google.cloud import language, exceptions

# create a Google Cloud Natural Languague API Python client
client = language.Client()

#%%
# a function which takes a block of text and returns its sentiment and magnitude
def detect_sentiment(text):
    """Detects sentiment in the text."""

    # Instantiates a plain text document.
    document = client.document_from_text(text)

    sentiment = document.analyze_sentiment().sentiment

    return sentiment.score, sentiment.magnitude
    
#%%

def sentiment_score_mag(line):
    # use a try-except block since we occasionally get language not supported errors
    try:
        score, mag = detect_sentiment(line)
    except exceptions.BadRequest:
        # skip the comment if we get an error
        return

    # increment the total count
    return score, mag
    
#%%    
graph_api_version = 'v2.9'
access_token = 'EAACEdEose0cBAMppwdE6j0TmbLOst9OeghQKmVekxwPlyVqtU5qjaKOPNA1hDZBMMmQbssPM3L3bwWHV8fuPMGD5BAJsXZBXZCvg5XksKXKNiQbI9pw8jZBuVmZC2oFY03rQieQyW9f78fWJfhjCEX81qzCujHExyXCKN8EU8eQVxIBG2PFIwVTs1MI00ZBvAZD'

# LHL's Facebook user id
user_id = '125845680811480'
# theAtlantic's Facebook user id
#user_id = '29259828486'

# the id of LHL's response post at https://www.facebook.com/leehsienloong/posts/1505690826160285
post_id = '1505690826160285'
# id of the Lola's post
#post_id = '10155411459998487'

# the graph API endpoint for comments on LHL's post
url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(graph_api_version, user_id, post_id)

comments = []
times = []
comment_lengths = []
scores = []
mags = []
current_count = 0

r = requests.get(url, params={'access_token': access_token})
while True:
    data = r.json()

    # catch errors returned by the Graph API
    if 'error' in data:
        raise Exception(data['error']['message'])

    # append the text of each comment into the comments list
    for comment in data['data']:
        # remove line breaks in each comment
        text = comment['message'].replace('\n', ' ')
        time_text = comment['created_time'].replace('\n', ' ')
        comments.append(text)
        times.append(time_text)
        comment_lengths.append(len(text))
        
        try:
            score, mag = detect_sentiment(text)
        except exceptions.BadRequest:
            score, mag = "NA"
        
        scores.append(score)
        mags.append(mag)

    print('got {} comments'.format(len(data['data'])))
    current_count += len(data['data'])
    print('total: {}'.format(current_count))
    
#    break
    # check if there are more comments
    if 'paging' in data and 'next' in data['paging']:
        r = requests.get(data['paging']['next'])
    else:
        break
#%%
## save the comments to a file
#with open('LHLComments.txt', 'w', encoding='utf-8') as f:
#    for comment in comments:
#        f.write(comment + '\n')
#
#with open('LHLTimes.txt', 'w', encoding='utf-8') as f:
#    for time in times:
#        f.write(time + '\n')
        
#%%
data = {'comments' : comments,
'times' : times,
'comment_lengths' : comment_lengths,
'scores' : scores,
'mags' : mags
}
        
dataFrame = pd.DataFrame(data)

#%%
#for i in range(5):
#    dataFrame.loc[i,'scores'] = sentiment_score_mag(dataFrame['comments'][i])

#%%