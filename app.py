import yt_dlp

url = "https://www.youtube.com/watch?v=v2V6nV_kWOU"

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Melhor qualidade disponível
    'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo de saída
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download Concluído!")