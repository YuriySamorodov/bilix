Traceback (most recent call last):
  File "/usr/local/Caskroom/miniconda/base/envs/bilix314/bin/bilix", line 6, in <module>
    sys.exit(main())
             ~~~~^^
  File "/usr/local/Caskroom/miniconda/base/envs/bilix314/lib/python3.14/site-packages/click/core.py", line 1524, in __call__
    return self.main(*args, **kwargs)
           ~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/usr/local/Caskroom/miniconda/base/envs/bilix314/lib/python3.14/site-packages/click/core.py", line 1445, in main
    rv = self.invoke(ctx)
  File "/usr/local/Caskroom/miniconda/base/envs/bilix314/lib/python3.14/site-packages/click/core.py", line 1308, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/Caskroom/miniconda/base/envs/bilix314/lib/python3.14/site-packages/click/core.py", line 877, in invoke
    return callback(*args, **kwargs)
  File "/Users/yuriy.samorodov/src/github.com/YuriySamorodov/bilix/bilix/cli/main.py", line 391, in main
    loop.run_until_complete(cor)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^
  File "/usr/local/Caskroom/miniconda/base/envs/bilix314/lib/python3.14/asyncio/base_events.py", line 719, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/Users/yuriy.samorodov/src/github.com/YuriySamorodov/bilix/bilix/sites/bilibili/downloader.py", line 433, in get_video
    path_lst, _ = await asyncio.gather(asyncio.gather(*media_cors), asyncio.gather(*add_cors))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/yuriy.samorodov/src/github.com/YuriySamorodov/bilix/bilix/download/base_downloader.py", line 76, in wrapper
    return await func(*new_args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/yuriy.samorodov/src/github.com/YuriySamorodov/bilix/bilix/download/base_downloader_part.py", line 194, in get_file
    file_list = await asyncio.gather(*cors)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/yuriy.samorodov/src/github.com/YuriySamorodov/bilix/bilix/download/base_downloader_part.py", line 233, in _get_file_part
    raise Exception(t('log.stream.retry_exceeded', name=part_path.name))
Exception: STREAM 超过重复次数 长安全新启源Q05  行车记录仪 内存卡更换教程 不介意自己更换  最好 找修理厂更换#新长安新安全 #长安启源Q05#星河创造营-v.27225639-30250709

╭─    ~/auto/Changan/QiYuan/Q05/reviews/bilibili.com/3546920402291048/BV1dDVW6YEUP ··········· 1 ✘  took 1m 2s   Changan   at 21:24:04  ─╮
╰─ bilix get_video https://www.bilibili.com/video/BV1dDVW6YEUP/\?vd_source\=13bf320f7520f7bd69c461696de6c40b -d .  --subtitle --image  --from-browser chrome
INFO     已存在 长安全新启源Q05  行车记录仪 内存卡更换教程 不介意自己更换  最好 找修理厂更换#新长安新安全 #长安启源Q05#星河创造营.jpg
INFO     已完成 长安全新启源Q05  行车记录仪 内存卡更换教程 不介意自己更换  最好 找修理厂更换#新长安新安全 #长安启源Q05#星河创造营-中文.srt
INFO     已完成 长安全新启源Q05  行车记录仪 内存卡更换教程 不介意自己更换  最好 找修理厂更换#新长安新安全 #长安启源Q05#星河创造营.mp4