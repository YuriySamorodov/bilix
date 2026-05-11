# 进阶使用

请使用 `bilix -h` 查看更多参数提示，包括方法名简写、画质选择、并发控制、下载速度和语言设置。

## 方法名简写

如果你觉得 `get_series`、`get_video` 等方法名太长，可以使用它们的简写：

```shell
bilix s 'url'
bilix v 'url'
bilix up 'url'
bilix cate '分区名'
bilix fav '收藏夹url'
bilix col '合集url'
```

更多方法请查看 `bilix -h`。

## 语言支持

bilix 支持中文和英文帮助与日志输出：

```shell
bilix -h
bilix -l en -h
bilix --locale en -h
```

## 登录

如果你是大会员，可以通过两种方式登录：

* 直接填写 cookie：

  在 `--cookie` 参数中填写浏览器缓存的 `SESSDATA`。

* 从浏览器载入 cookie：

  使用 `-fb --from-browser` 参数读取浏览器中的 cookie，例如 `-fb chrome`。

## 画质、音质和编码选择

使用 `--quality` 或 `-q` 参数选择画质：

* 默认相对选择：`-q 0` 表示最高画质，数字越大画质越低。
* 绝对选择：可以使用 `-q 1080p`、`-q 4K` 或部分名称匹配。

如果你需要指定编码，可以使用 `--codec`：

```shell
bilix v 'url' --codec hev1
bilix v 'url' --codec hev1:fLaC
```

`--codec` 支持画质编码与音频编码用 `:` 分隔。

## 断点续传

中断任务后重新执行命令，已完成的文件会跳过，未完成的文件会继续下载。

如果你改变了 `-q`、`--codec`、`--part-con` 或 `--time-range`，建议清理临时文件后重新执行命令，以避免残留不完整文件。

## 多 URL 支持

所有方法支持一次提供多个 URL：

```shell
bilix v 'url1' 'url2' 'url3'
bilix up 'up_url1' 'up_url2'
```

并发控制仍然正常工作。
