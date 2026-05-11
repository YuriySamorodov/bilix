# 快速上手

bilix 提供了简单的命令行使用方式，打开终端开始下载吧。

## 查看帮助

```shell
bilix -h
bilix -l en -h
```

## 批量下载

批量下载整部动漫、电视剧、纪录片、电影、up 投稿等，只要把命令中的 `url` 替换为系列中任意一个视频链接。

```shell
bilix get_series 'url'
```

`get_series` 会自动识别系列中的所有视频并下载；如果系列只有一个视频，同样可以正常下载。

::: info
* 系列（series）可以是多 P 投稿、动漫、电视剧或电影的全部集数。
* 某些带参数的 URL 在终端中要用 `''` 包住，Windows 的 CMD 不支持 `''`，可使用 PowerShell 或 Windows Terminal。
:::

## 单个视频下载

如果你只想下载单个视频，使用 `get_video`：

```shell
bilix get_video 'url'
```

## 下载音频

如果你只想下载音频，可以使用 `--only-audio`：

```shell
bilix get_series 'url' --only-audio
```

## 切片下载

使用 `--time-range` 或 `-tr` 指定时间区间下载片段：

```shell
bilix get_video 'url' -tr 0:16:53-0:17:49
```

时间格式支持 `h:m:s-h:m:s` 或 `s-s`，该参数仅在 `get_video` 中生效。

## 下载特定 UP 主的投稿

```shell
bilix get_up 'https://space.bilibili.com/672328094' --num 100
```

`get_up` 支持 UP 空间页 URL 或 MID。

## 下载分区视频

```shell
bilix get_cate 宅舞 --keyword 超级敏感 --order click --num 20 --days 30
```

`get_cate` 支持分区名、关键词搜索和排序参数。

## 下载收藏夹视频

```shell
bilix get_favour 'https://space.bilibili.com/11499954/favlist?fid=1445680654' --num 20
```

## 下载合集或视频列表

```shell
bilix get_collect 'url'
```

`get_collect` 会根据合集或视频列表详情页 URL 自动识别目标。

## 附件下载

增加 `--subtitle`、`--dm`、`--image` 参数，可以下载字幕、弹幕和封面：

```shell
bilix get_series 'url' --subtitle --dm --image
```
