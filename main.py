from TikTokAPI import TikTokAPI


class TikTokDL:
    def __init__(self, video_id, save_path):
        self.video_id = video_id
        self.save_path = save_path


print("Please read the README.md file if you dont know about s_v_web_id and tt_webid")
s_v_web_id = input("Enter the s_v_web_id")
tt_webid = input("Enter the tt_webid")

cookie = {
    "s_v_web_id": s_v_web_id,
    "tt_webid": tt_webid
}

api = TikTokAPI(cookie=cookie)

tikTokDl = TikTokDL(
    video_id=input("Enter the video_id"),
    save_path=input("Enter the save_path (default /tiktokdl/downloads")
)

if tikTokDl.save_path == "":
    tikTokDl.save_path = "/downloads"

api.downloadVideoByIdNoWatermark(tikTokDl.video_id, tikTokDl.save_path)
