# API 案例

bilix 提供了各个站点的 API 模块，支持异步请求并返回视频信息。

```python
import asyncio
from bilix.sites.bilibili import api
from httpx import AsyncClient

async def main():
    client = AsyncClient(**api.dft_client_settings)
    data = await api.get_video_info(client, 'https://www.bilibili.com/bangumi/play/ep90849')
    print(data)
    await client.aclose()

asyncio.run(main())
```

你可以参考其他站点目录下的 `api.py` 和 `api_test.py` 来扩展新的站点。
