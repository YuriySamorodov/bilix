# Installation

bilix is a Python asynchronous downloader. It supports Python 3.8 and above.

## Install bilix

```shell
pip install bilix
```

For development and source editing, install in editable mode:

```shell
pip install -e .
```

macOS users can also try Homebrew:

```shell
brew install bilix
```

## Install FFmpeg

Some downloads require FFmpeg for audio/video merging, m3u8 downloads, and media processing.

* macOS:

```shell
brew install ffmpeg
```

* Windows:

Download a build from https://ffmpeg.org/download.html\#build-windows and add `ffmpeg` to your PATH.

::: info
Make sure you can run `ffmpeg` from the command line after installation.
:::
