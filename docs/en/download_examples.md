# Download examples

bilix can be used as a Python library and provides powerful options beyond the CLI.

## Simple example

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    async with DownloaderBilibili() as d:
        await d.get_series('https://www.bilibili.com/video/BV1jK4y1N7ST?p=5')

if __name__ == '__main__':
    asyncio.run(main())
```

## Combine multiple tasks / control concurrency

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    d = DownloaderBilibili(video_concurrency=5, part_concurrency=10)
    cor1 = d.get_series('https://www.bilibili.com/bangumi/play/ss28277', quality=999)
    cor2 = d.get_up(url_or_mid='436482484', quality=999)
    cor3 = d.get_video('https://www.bilibili.com/bangumi/play/ep477122', quality=999)
    await asyncio.gather(cor1, cor2, cor3)
    await d.aclose()

if __name__ == '__main__':
    asyncio.run(main())
```

## Clip download

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    async with DownloaderBilibili() as d:
        await d.get_video('https://www.bilibili.com/video/BV1kK4y1A7tN', time_range=(0, 7))

if __name__ == '__main__':
    asyncio.run(main())
```

## Multiple sites

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili
from bilix.sites.cctv import DownloaderCctv

async def main():
    async with DownloaderBilibili() as bili_d, DownloaderCctv() as cctv_d:
        await asyncio.gather(
            bili_d.get_video('https://www.bilibili.com/video/BV1cd4y1Z7EG', quality=999),
            cctv_d.get_video('https://tv.cctv.com/2012/05/02/VIDE1355968282695723.shtml', quality=999)
        )

if __name__ == '__main__':
    asyncio.run(main())
```

## Speed limit

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    async with DownloaderBilibili(speed_limit=1e6) as d:
        await d.get_series('https://www.bilibili.com/video/BV1jK4y1N7ST?p=5')

if __name__ == '__main__':
    asyncio.run(main())
```

## Progress bar

```python
from bilix.progress.cli_progress import CLIProgress
CLIProgress.start()
```

Or use the downloader's `progress` object:

```python
async with DownloaderBilibili() as d:
    d.progress.start()
    await d.get_series('url')
```
