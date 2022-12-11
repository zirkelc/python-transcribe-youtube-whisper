# Transcribe YouTube Videos with Whisper

## Install

Install the Python packages for Whisper, PyTube and Pandas. Whisper requires Python 3.7 or later.

```sh
pip install git+https://github.com/openai/whisper.git 
pip install git+https://github.com/pytube/pytube.git
pip install pandas
```

## Usage
Specify YouTube video URL with `--video` option. The URL must be valid watch URL.

```sh
python3 main.py --video "https://www.youtube.com/watch?v=rQrE4LmQ3GQ"
```

## Jupyter
This code is available as interactive [Jupyter Notebook on Colab](https://colab.research.google.com/drive/1QEffU2A5PaJzfdvmLcd53vZ5emizQcFG?usp=sharing).