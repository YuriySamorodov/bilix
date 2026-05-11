# Advanced guide

Use `bilix -h` to see more options such as short aliases, quality selection, concurrency control, speed limit, and language settings.

## Short aliases

If `get_series` and `get_video` feel too long, use their short forms:

```shell
bilix s 'url'
bilix v 'url'
bilix up 'url'
bilix cate 'category'
bilix fav 'favorite_url'
bilix col 'collection_url'
```

## Language support

bilix supports both Chinese and English help and log output:

```shell
bilix -h
bilix -l en -h
bilix --locale en -h
```

## Login

If you are a premium member, use one of the following:

* Cookie mode:

  Provide the browser `SESSDATA` cookie in `--cookie`.

* Browser import:

  Use `-fb --from-browser` to import browser cookies, for example `-fb chrome`.

## Quality, audio, and codec

Use `--quality` or `-q` to choose quality:

* Relative selection: `-q 0` is the highest available quality, larger numbers choose lower quality.
* Absolute selection: use strings such as `-q 1080p`, `-q 4K`, or partial names.

To specify codec, use `--codec`:

```shell
bilix v 'url' --codec hev1
bilix v 'url' --codec hev1:fLaC
```

The `--codec` parameter accepts `:` to separate video codec and audio codec.

## Resume support

If a task is interrupted with Ctrl+C, rerun the same command to resume. Completed files are skipped, and unfinished files continue downloading.

If you change `-q`, `--codec`, `--part-con`, or `--time-range`, it is recommended to clear temporary files before rerunning to avoid partial leftovers.

## Multiple URLs

All methods support passing multiple URLs:

```shell
bilix v 'url1' 'url2' 'url3'
bilix up 'up_url1' 'up_url2'
```

Concurrency control still works normally.
