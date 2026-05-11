# 安装
bilix 是一个基于 Python 的异步下载工具，建议使用 Python 3.8 及以上版本。

## 安装 bilix

```shell
pip install bilix
```

如果你想参与开发或修改源码，可使用可编辑安装：

```shell
pip install -e .
```

macOS 用户也可以视情况尝试 Homebrew 安装：

```shell
brew install bilix
```

## 安装 FFmpeg

部分视频处理需要 FFmpeg，例如音视频合并、m3u8 下载和音频提取。

* macOS：

```shell
brew install ffmpeg
```

* Windows：

访问 https://ffmpeg.org/download.html#build-windows 下载并安装，然后配置环境变量。

::: info
安装完成后，请确保终端中可以直接运行 `ffmpeg`。
:::
