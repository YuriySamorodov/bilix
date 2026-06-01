# 更多

## 欢迎反馈

如果你发现任何 bug 或问题，欢迎提 [Issue](https://github.com/HFrost0/bilix/issues)。

如果你有新想法或功能请求，欢迎加入 [Discussion](https://github.com/HFrost0/bilix/discussions)。

如果你觉得该项目有帮助，可以给作者一个小小的 [Star](https://github.com/HFrost0/bilix/stargazers)🌟

## 参与贡献

❤️ 非常欢迎～详情可见 [contributing](https://github.com/HFrost0/bilix/blob/master/CONTRIBUTING.md)

## 现在可用的功能

- 支持 `get_series`, `get_video`, `get_up`, `get_cate`, `get_favour`, `get_collect`, `info` 等方法。
- 支持 `--subtitle`、`--dm`、`--image` 附件下载。
- 支持 `--time-range` 视频切片下载。
- 支持 `--language` / `--locale` / `-l` 语言切换，帮助和日志支持中英文。

## 日志功能

- 运行时会在当前工作目录下创建 `logs` 目录。
- 日志按天保存为 `YYYY-MM-DD.log`，每天一个文件。
- 每条审计日志都会记录日期、下载或请求 URL、文件大小和状态。
- 出现错误时会同时记录异常信息和 traceback，便于排查 HTTP 失败、重试耗尽和下载中断。

## 已知 bug 🤡

当两个视频名字完全一样时，任务可能发生冲突但不会报错。