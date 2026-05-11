# bilix

[![GitHub license](https://img.shields.io/github/license/HFrost0/bilix?style=flat-square)](https://github.com/HFrost0/bilix/blob/master/LICENSE)
![PyPI](https://img.shields.io/pypi/v/bilix?style=flat-square&color=blue)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/HFrost0/bilix)
![PyPI - Downloads](https://img.shields.io/pypi/dm/bilix?label=pypi%20downloads&style=flat-square)

⚡️ Lightning-fast asynchronous downloader for Bilibili and more.

## Features

- Async native download engine with high concurrency and speed control.
- Full CLI and Python API support for series, videos, up hosts, categories, favorites, collections, and info lookups.
- Built-in Chinese/English help and log localization via `--language`, `--locale`, or `-l`.
- Extensible site plugin architecture under `bilix/sites`.
- Download attachments such as subtitles, cover images, and danmaku.

## Install

```shell
pip install bilix
```

For development or local editing:

```shell
pip install -e .
```

On macOS, `bilix` may also be available via Homebrew:

```shell
brew install bilix
```

## Usage Example

### CLI

```shell
bilix v 'https://www.bilibili.com/video/BV1xx411q7xx'
bilix -l en -h
```

`v` is a short alias for `get_video`.

### Python

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    async with DownloaderBilibili() as d:
        await d.get_video('https://www.bilibili.com/video/BV1xx411q7xx')

asyncio.run(main())
```

## Help & Language

Use `bilix -h` to show the CLI help text. Use `-l en` or `--language en` to display help and logs in English.

## Community

If you find any bugs or issues, feel free to raise an [Issue](https://github.com/HFrost0/bilix/issues).

If you have ideas or feature requests, join the [Discussion](https://github.com/HFrost0/bilix/discussions).

If you find this project useful, please give it a [Star](https://github.com/HFrost0/bilix/stargazers)🌟

## Contribute

❤️ Welcome! Details can be found in [CONTRIBUTING_EN.md](CONTRIBUTING_EN.md)
