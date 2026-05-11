# 下载案例

bilix 可以作为 Python 库调用，并提供更细粒度的参数控制和组合下载能力。

## 从最简单的开始

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    async with DownloaderBilibili() as d:
        await d.get_series('https://www.bilibili.com/video/BV1jK4y1N7ST?p=5')

if __name__ == '__main__':
    asyncio.run(main())
```

## 组合多任务 / 控制并发

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

## 下载切片

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    async with DownloaderBilibili() as d:
        await d.get_video('https://www.bilibili.com/video/BV1kK4y1A7tN', time_range=(0, 7))

if __name__ == '__main__':
    asyncio.run(main())
```

## 同时下载多个站点

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili
from bilix.sites.cctv import DownloaderCctv

async def main():
    async with DownloaderBilibili() as d_bl, DownloaderCctv() as d_tv:
        await asyncio.gather(
            d_bl.get_video('https://www.bilibili.com/video/BV1cd4y1Z7EG', quality=999),
            d_tv.get_video('https://tv.cctv.com/2012/05/02/VIDE1355968282695723.shtml', quality=999)
        )

if __name__ == '__main__':
    asyncio.run(main())
```

## 限制下载速度

```python
import asyncio
from bilix.sites.bilibili import DownloaderBilibili

async def main():
    async with DownloaderBilibili(speed_limit=1e6) as d:
        await d.get_series('https://www.bilibili.com/video/BV1jK4y1N7ST?p=5')

if __name__ == '__main__':
    asyncio.run(main())
```

## 显示进度条

```python
from bilix.progress.cli_progress import CLIProgress

CLIProgress.start()
```

或者通过下载器的 `progress` 对象启动：

```python
async with DownloaderBilibili() as d:
    d.progress.start()
    await d.get_series('url')
```
