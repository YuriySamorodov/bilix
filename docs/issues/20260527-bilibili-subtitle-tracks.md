# 20260527 Bilibili subtitle tracks

## Problem

Running the Bilibili video download command with `--subtitle` on a track-rich video only produced a single `.srt` file at first, even though the page exposed multiple subtitle tracks. In the observed case, the video `BV1ra5Z6qExK` exposed six subtitle tracks in the authenticated player response, but the CLI path did not reliably save all of them. The generated subtitle file also appeared wrong in at least one run, because it contained unrelated text/data instead of a valid subtitle transcript.

## Root Cause

Two issues were involved:

- `get_subtitle_info()` called `https://api.bilibili.com/x/player/v2` without the extra `fnval=4048` query parameter, which caused Bilibili to return an incomplete subtitle track list for this video.
- The downloader always wrote an empty `SESSDATA` cookie even when the user only selected `--from-browser chrome`, which could alter the authenticated Bilibili response.

## Resolution

- Added `fnval=4048` to the subtitle API request in `bilix/sites/bilibili/api.py`.
- Restricted subtitle extraction to the actual subtitle arrays returned by Bilibili.
- Avoided setting `SESSDATA` unless the user explicitly provided session data.

Developer note: `fnval=4048` is not a cosmetic toggle. On Bilibili player endpoints it asks for a richer playback response, and for this subtitle flow it was the difference between a minimal subtitle payload and the full subtitle track list. Without it, the endpoint could collapse the response down to a single track or otherwise omit tracks that were visible in the page player.

In practice, that meant the CLI had enough information to fetch the video, but not enough subtitle metadata to mirror what the user could see in the browser. The subtitle downloader then had no way to create separate files for each language/version because the API response itself was incomplete.

The `SESSDATA` note matters here because browser-cookie authentication already provides a valid user session. Writing an empty or placeholder `SESSDATA` cookie on top of that session can change how Bilibili interprets the request, which makes debugging the subtitle payload harder and can hide the real API behavior behind an artificial cookie state.

## Validation

The live command was re-run with Chrome cookies against:

`https://www.bilibili.com/video/BV1ra5Z6qExK/?vd_source=13bf320f7520f7bd69c461696de6c40b`

Result:

- six subtitle tracks were returned by the API helper
- six separate `.srt` files were written
- filenames were distinct for each language track: `中文`, `English`, `日本語`, `Español`, `العربية`, `Português`

The touched Python files also passed `py_compile`.
