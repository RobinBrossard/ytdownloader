import yt_dlp
import os
from urllib.parse import urlparse


def download_videos(url, output_path):
    # 设置下载参数
    ydl_opts = {
        'outtmpl': output_path + '/%(title)s.%(ext)s',  # 设置文件名格式
        'format': 'bestaudio/best',  # 选择最佳音频质量
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # 使用 FFmpeg 提取音频
            'preferredcodec': 'mp3',  # 设置音频编码为 mp3
            'preferredquality': '192',  # 设置音频质量
        }],
    }

    # 创建 YoutubeDL 对象并下载
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def check_input():
    # 提示用户输入url和path
    url = input("请输入YouTube内容的网址：")
    path = input("请输入目录路径（默认为'd:\\temp'）：") or 'd:\\temp'

    # 检查url是否为合法的YouTube网址
    parsed = urlparse(url)
    if parsed.netloc not in ['www.youtube.com', 'youtu.be']:
        return "URL不是YouTube网址，请输入youtube网址"

    # 检查path是否为本地存在的目录
    if not os.path.isdir(path):
        return "路径不存在或不是一个目录"

    return url, path


# 使用函数下载视频
result = check_input()
url = ''
path = ''

if isinstance(result, tuple) and len(result) == 2:
    url, path = result
else:
    print(result)

download_videos(url, path)
