# 异步基础

bilix 的下载接口是基于 Python 异步的，适合高并发网络请求场景。

在 Python 中，`async def` 定义的函数会返回一个协程对象，需要交给事件循环执行：

```python
import asyncio

async def hello():
    print('hello world')

asyncio.run(hello())
```

bilix 的下载方法也是异步的，可以这样使用：

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    async with DownloaderBilibili() as d:
        await d.get_video('url')

asyncio.run(main())
```

如果你需要显示进度条，可以使用 `CLIProgress.start()` 或通过下载器内部的 `progress` 对象：

```python
from bilix.progress.cli_progress import CLIProgress
CLIProgress.start()
```
