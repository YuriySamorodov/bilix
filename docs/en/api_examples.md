# API examples

bilix provides site API modules that can be used directly and are fully asynchronous.

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

You can refer to `api.py` and `api_test.py` in other site folders when adding support for a new site.
