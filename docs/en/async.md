# Async basics

bilix download methods are asynchronous and designed for high-concurrency network work.

In Python, `async def` functions return coroutine objects that must be executed by an event loop:

```python
import asyncio

async def hello():
    print('hello world')

asyncio.run(hello())
```

bilix methods are also asynchronous:

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    async with DownloaderBilibili() as d:
        await d.get_video('url')

asyncio.run(main())
```

To show progress in Python, use `CLIProgress.start()` or the downloader's `progress` object:

```python
from bilix.progress.cli_progress import CLIProgress
CLIProgress.start()
```
