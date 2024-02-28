from flask import Flask, Response
import subprocess

app = Flask(__name__)

def generate_audio():
    # Start the audio streaming pipeline (parec, ffmpeg)
    audio_pipeline = subprocess.Popen(
        ["parec", "--device=alsa_output.pci-0000_05_00.6.analog-stereo.monitor", "--format=s16le", "--rate=44100", "--channels=2"],
        stdout=subprocess.PIPE
    )

    ffmpeg_process = subprocess.Popen(
        ["ffmpeg", "-f", "s16le", "-ar", "44100", "-ac", "2", "-i", "pipe:0", "-f", "wav", "-"],
        stdin=audio_pipeline.stdout,
        stdout=subprocess.PIPE
    )

    return ffmpeg_process.stdout

@app.route('/audio_stream')
def audio_stream():
    return Response(generate_audio(), mimetype='audio/wav')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
