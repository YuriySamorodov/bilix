# Quickstart

bilix provides a simple command-line interface, so open your terminal and start downloading.

## Help and language

```shell
bilix -h
bilix -l en -h
```

## Batch download

Download an entire anime series, TV show, movie, UP submission, or collection by replacing `url` with any video link in that series.

```shell
bilix get_series 'url'
```

`get_series` can automatically detect and download all videos in a series. If the content only contains a single video, it still works.

::: info
* A series can be a multi-part upload, an anime, a TV show, or a full movie.
* Some URLs with query parameters must be wrapped in single quotes (`''`) in the terminal.
  Windows CMD does not support `''`; use PowerShell or Windows Terminal instead.
:::

## Single video download

If you want only one video, use `get_video`:

```shell
bilix get_video 'url'
```

## Audio download

If you only want audio, use `--only-audio`:

```shell
bilix get_series 'url' --only-audio
```

## Clip download

Use `--time-range` or `-tr` to download a specific segment:

```shell
bilix get_video 'url' -tr 0:16:53-0:17:49
```

The format supports `h:m:s-h:m:s` or `s-s`. This option only works with `get_video`.

## Download from an uploader

```shell
bilix get_up 'https://space.bilibili.com/672328094' --num 100
```

`get_up` accepts a Bilibili space URL or the uploader's MID.

## Download by category

```shell
bilix get_cate 宅舞 --keyword 超级敏感 --order click --num 20 --days 30
```

`get_cate` supports sub-category names, keyword search, sort options, and count limits.

## Download favorites

```shell
bilix get_favour 'https://space.bilibili.com/11499954/favlist?fid=1445680654' --num 20
```

## Download collection or playlist

```shell
bilix get_collect 'url'
```

`get_collect` detects collection and playlist detail page URLs and downloads their videos.

## Download subtitles, danmaku, cover images

Add `--subtitle`, `--dm`, or `--image` to download additional files:

```shell
bilix get_series 'url' --subtitle --dm --image
```
