import requests, sys
from json import loads

class YoutubeApis():

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.playlist_video_lists = "https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&channelId={0}&order=date&playlistId={1}&key={2}"
        self.video_api = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&channelId={0}&type=video&order=date&key={1}"

    def write_data(self, file_path, api_response):
        with open(file_path, "w") as file_to_write: file_to_write.write(api_response.text)

    def save_all_latest_video(self):
        print(self.video_api.format(self.channel_id, self.api_key))
        api_info = requests.get(self.video_api.format(self.channel_id, self.api_key))
        self.write_data("./data/latest_video.json", api_info)

    def save_all_video_of_playlist(self, playlist_name, playlist_id):
        api_info = requests.get(self.playlist_video_lists.format(self.channel_id, playlist_id, self.api_key))
        self.write_data("./data/{0}_playlist_videos.json".format(playlist_name), api_info)

    def save_data(self):
        # self.save_all_latest_video()
        with open("./data/playlist.json") as playlist_json: playlists = playlist_json.read()
        for playlist_name in loads(playlists).get('playlists').keys():
            playlist_id = loads(playlists).get('playlists').get(playlist_name).get('playlistId')
            self.save_all_video_of_playlist(playlist_name, playlist_id)


if __name__ == "__main__":
    api_key = sys.argv[1]
    youtube_data = YoutubeApis(api_key, "UC6hVs0MVTC5ZbKWdaRSB22A")
    youtube_data.save_data()
