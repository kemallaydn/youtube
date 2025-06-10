import yt_dlp

def youtube_to_mp3(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': False,
            'noplaylist': True,  # Sadece videoyu indir, playlist’i yok say
            'nocheckcertificate': True,  # SSL doğrulamasını devre dışı bırak
                        'merge_output_format': 'mp3'  # Videonun MP3 formatına dönüştürülmesini sağlar

        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{url} indiriliyor...")
            ydl.download([url])
            print("İndirme tamamlandı!")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    video_url = input("İndirmek istediğiniz YouTube videosunun URL'sini girin: ")
    youtube_to_mp3(video_url)