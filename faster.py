import webbrowser
import time
import pyautogui
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone

# Set up YouTube API key and build the service
API_KEY = 'AIzaSyASk-w_tFF4MIHoF4eRIvL6I3GJZFWeUMA'  # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_published_after(time_frame):
    """Returns the ISO 8601 formatted date for the given time frame."""
    now = datetime.now(timezone.utc)  # Use timezone-aware UTC datetime
    
    if time_frame == "Last hour":
        return (now - timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    elif time_frame == "Today":
        return (now - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    elif time_frame.lower() == "this week":
        return (now - timedelta(weeks=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    elif time_frame == "This month":
        return (now - timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
    elif time_frame == "This year":
        return (now - timedelta(days=365)).strftime('%Y-%m-%dT%H:%M:%SZ')
    else:
        return None

def search_videos(title, channel_name, published_after):
    """Search for videos based on the given criteria."""
    try:
        search_request = youtube.search().list(
            q=title,
            part='snippet',
            type='video',
            maxResults=10,
            publishedAfter=published_after
        )
        
        # Print debug information
        request_url = search_request.uri
        request_parameters = request_url.split('?')[1]
        print(f"Request URL: {request_url}")
        print(f"Request Parameters: {request_parameters}")
        
        search_response = search_request.execute()
        
        # Print the raw response for debugging
        print(f"Raw API Response: {search_response}")
    
    except Exception as e:
        print(f"An error occurred while searching for videos: {e}")
        return []
    
    filtered_videos = []

    for item in search_response.get('items', []):
        video_title = item['snippet']['title']
        video_channel = item['snippet']['channelTitle']
        video_id = item['id']['videoId']

        # Debug information
        print(f"Video Title: {video_title}, Channel: {video_channel}")
        
        # Filter by channel name (case-insensitive comparison)
        if channel_name.lower() in video_channel.lower():
            filtered_videos.append({
                'title': video_title,
                'channel': video_channel,
                'id': video_id
            })
    
    return filtered_videos

def watch_video(video_id):
    """Open the video in the default web browser."""
    url = f'https://www.youtube.com/watch?v={video_id}'
    webbrowser.open(url)

def read_input_from_file(file_path):
    """Reads input from a text file and returns title, channel name, and time frame."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            title = lines[0].strip()
            channel_name = lines[1].strip()
            time_frame = lines[2].strip()
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None, None, None
    
    return title, channel_name, time_frame

def main():
    file_path = 'output.txt'  # Path to your input file
    
    title, channel_name, time_frame = read_input_from_file(file_path)
    
    if title is None or channel_name is None or time_frame is None:
        print("Failed to read input from file.")
        return
    
    published_after = get_published_after(time_frame)
    
    if published_after is None:
        print("Invalid time frame provided.")
        return
    
    videos = search_videos(title, channel_name, published_after)
    
    if not videos:
        print('No videos found.')
        return
    
    print("\nVideos found:")
    for idx, video in enumerate(videos):
        print(f"{idx + 1}. {video['title']} ({video['channel']})")
    
    video_id = videos[0]['id']
    
    print('Playing the first video...')
    
    video_play_time_limit = 30  # Example: play the video for 30 seconds
    print(f"The video will play for {video_play_time_limit} seconds.")
    
    watch_video(video_id)
    
    # Wait for the specified playback time limit
    time.sleep(video_play_time_limit)
    
    # Close the tab using keyboard shortcut (Ctrl + W)
    print("Playback time limit reached. Closing the browser tab...")
    
    pyautogui.hotkey('ctrl', 'w')  # This simulates pressing Ctrl + W

if __name__ == '__main__':
    main()