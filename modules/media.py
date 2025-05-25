import pywhatkit
def play_youtube_video(command: str):
    """
    Play a YouTube video by its name.
    
    Args:
        video_name (str): The name of the video to play.
    """
    try:
       song = command.replace("play", "").strip()
       pywhatkit.playonyt(song)
       return f"Playing {song} on YouTube."
    except Exception as e:
        print(f"An error occurred while trying to play the video: {e}")
        
        
def search_google(command: str):
    """
    Search Google for a query.
    
    Args:
        query (str): The search query.
    """
    try:
        query = command.replace("search", "").strip()
        pywhatkit.search(query)
        return f"Searching Google for {query}."
    except Exception as e:
        print(f"An error occurred while trying to search Google: {e}")