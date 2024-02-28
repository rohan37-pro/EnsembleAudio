import vlc

def play_audio_stream(url):
    # Create VLC instance
    instance = vlc.Instance("--no-xlib")  # Adjust options based on your environment

    # Create a media player
    player = instance.media_player_new()

    # Create a media object with the streaming URL
    media = instance.media_new(url)

    # Set the media to the player
    player.set_media(media)

    # Play the media
    player.play()

    # Wait for the user to press Ctrl+C to stop
    try:
        while True:
            pass
    except KeyboardInterrupt:
        player.stop()

if __name__ == "__main__":
    # Replace "http://127.0.0.1:8080" with the actual streaming URL
    streaming_url = "http://127.0.0.1:8080/audio_stream"

    play_audio_stream(streaming_url)
