from pytube import YouTube
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
print(yt.title)
# print(yt.streams.filter(file_extension='mp4'))

# [<Stream: itag="18" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="22" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="avc1.640028" progressive="False" type="video">, <Stream: itag="399" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="av01.0.08M.08" progressive="False" type="video">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.4d401f" progressive="False" type="video">, <Stream: itag="398" mime_type="video/mp4" res="720p" fps="24fps" vcodec="av01.0.05M.08" progressive="False" type="video">, <Stream: itag="135" mime_type="video/mp4" res="480p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="397" mime_type="video/mp4" res="480p" fps="24fps" vcodec="av01.0.04M.08" progressive="False" type="video">, <Stream: itag="134" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="396" mime_type="video/mp4" res="360p" fps="24fps" vcodec="av01.0.01M.08" progressive="False" type="video">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="24fps" vcodec="avc1.4d4015" progressive="False" type="video">, <Stream: itag="395" mime_type="video/mp4" res="240p" fps="24fps" vcodec="av01.0.00M.08" progressive="False" type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="24fps" vcodec="avc1.4d400c" progressive="False" type="video">, <Stream: itag="394" mime_type="video/mp4" res="144p" fps="24fps" vcodec="av01.0.00M.08" progressive="False" type="video">, <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">]

stream = yt.streams.get_by_itag(160)
print("download started")
stream.download()
print("download ended")