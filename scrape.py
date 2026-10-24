from googleapiclient.discovery import build
import pandas as pd

# 1. Yahan apni API Key paste karein
API_KEY = "AIzaSyAWFRcxNeMLYO4la-IIF5iQ8Rh5aF2t_Yc"

# 2. Yahan Mitti Da Baway Episode 1 ki Video ID dalein
VIDEO_IDS = ["P4zyZAl30To"] 

youtube = build('youtube', 'v3', developerKey=API_KEY)
all_comments = []

for video_id in VIDEO_IDS:
    print(f"Fetching comments for video: {video_id}")
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            textFormat="plainText"
        )
        response = request.execute()
        
        # Yeh loop chalta rahega jab tak comments aate rahenge
        while response:
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                all_comments.append({'video_id': video_id, 'comment': comment})
            
            if 'nextPageToken' in response:
                request = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=100,
                    pageToken=response['nextPageToken'],
                    textFormat="plainText"
                )
                response = request.execute()
            else:
                break
    except Exception as e:
        print(f"Error: {e}")

df = pd.DataFrame(all_comments)
# Yeh file aapke folder mein ban jayegi
df.to_csv('raw_comments.csv', index=False)
print(f"Total comments fetched: {len(df)}")