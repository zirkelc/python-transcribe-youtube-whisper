
import whisper
from pytube import YouTube, Channel
import pandas as pd


def main(args):
    video_url = args.video

    audio_file = YouTube(video_url).streams.filter(
        only_audio=True).first().download(filename="audio.mp4")

    whisper_model = whisper.load_model("tiny")
    transcription = whisper_model.transcribe(audio_file)

    df = pd.DataFrame(data=transcription['segments'], columns=[
        'start', 'end', 'text'])

    print(df)


if __name__ == "__main__":

    from argparse import ArgumentParser
    from pathlib import Path

    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--video', type=str, required=True,
                        help="YouTube video URL")
    args = parser.parse_args()
    main(args)
