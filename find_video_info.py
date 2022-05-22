import requests, sys

class YoutubeApis():

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.playlist_api = "https://youtube.googleapis.com/youtube/v3/playlists?part=snippet&maxResults=50&channelId={0}&key={1}"
        self.playlist_video_lists = "https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&channelId={0}&order=date&playlistId={1}&key={2}"
        self.video_api = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&channelId={0}&type=video&order=date&key={1}"

    def save_all_playlists(self):
        api_info = requests.get(self.playlist_api.format(self.channel_id, self.api_key))

    def save_all_latest_video(self):
        latest_video = requests.get(self.video_api.format(self.channel_id, self.api_key))

    def save_all_video_of_playlist(self, playlist):
        latest_video = requests.get(self.video_api.format(self.channel_id, self.api_key))

if __name__ == "__main__":
    api_key = sys.argv[1]
    prep_variables = YoutubeApis("", "UC6hVs0MVTC5ZbKWdaRSB22A")