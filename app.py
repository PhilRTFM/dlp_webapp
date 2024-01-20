from flask import Flask, render_template, request, jsonify
import yt_dlp as youtube_dl
import os
import threading

app = Flask(__name__)
download_progress = 0

def my_hook(d):
    global download_progress
    if d['status'] == 'downloading':
        download_progress = int(d['downloaded_bytes'] / d['total_bytes'] * 100)

def download_video(link, output_directory):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(link, download=True)

def async_download(video_link, output_directory):
    threading.Thread(target=download_video, args=(video_link, output_directory)).start()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global download_progress
        download_progress = 0
        video_link = request.form.get('videolink')
        async_download(video_link, 'downloaded_videos')
        return render_template('success.html')
    return render_template('index.html')

@app.route('/progress')
def progress():
    return jsonify(progress=download_progress)

if __name__ == '__main__':
    app.run(debug=True)
