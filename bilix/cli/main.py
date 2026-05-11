import asyncio
import typing
from pathlib import Path
import click
import rich
from rich.panel import Panel
from rich.table import Table

from .. import __version__
from ..log import logger
from .assign import assign
from ..progress.cli_progress import CLIProgress
from ..utils import parse_bytes_str, s2t
from ..exception import HandleError
from ..i18n import bilingual, get_explicit_language, help_text, set_language, t


def handle_help(ctx: click.Context, param: typing.Union[click.Option, click.Parameter], value: typing.Any, ) -> None:
    if not value or ctx.resilient_parsing:
        return
    language = get_explicit_language()
    print_help(language=language)
    ctx.exit()


def handle_language(ctx: click.Context, param: typing.Union[click.Option, click.Parameter], value: typing.Any, ) -> typing.Any:
    if not value or ctx.resilient_parsing:
        return value
    set_language(value)
    return value


def handle_version(ctx: click.Context, param: typing.Union[click.Option, click.Parameter], value: typing.Any, ) -> None:
    if not value or ctx.resilient_parsing:
        return
    print(f"Version {__version__}")
    ctx.exit()


def handle_debug(ctx: click.Context, param: typing.Union[click.Option, click.Parameter], value: typing.Any, ):
    if not value or ctx.resilient_parsing:
        return
    from rich.traceback import install
    install()
    logger.setLevel('DEBUG')
    logger.debug(t('cli.debug.enabled'))


def print_help(language=None):
    console = rich.console.Console()
    text = lambda zh, en: help_text(zh, en, language)
    console.print(f"\n[bold]bilix {__version__}", justify="center")
    console.print(text(
        "⚡️快如闪电的bilibili下载工具，基于Python现代Async特性，高速批量下载整部动漫，电视剧，up投稿等",
        "⚡️A fast bilibili downloader built with modern Python async features for bulk download of anime, TV shows, uploads, and more."
    ), justify="center")
    console.print(text(
        "使用方法： bilix [cyan]<method> <key1, key2...> [OPTIONS][/cyan] ",
        "Usage: bilix [cyan]<method> <key1, key2...> [OPTIONS][/cyan] "
    ), justify="left")
    table = Table.grid(padding=1, pad_edge=False)
    table.add_column("Parameter", no_wrap=True, justify="left", style="bold")
    table.add_column("Description")

    table.add_row(
        "[cyan]<method>",
        text(
            'get_series 或 s：   获取整个系列的视频（包括多p投稿，动漫，电视剧，电影，纪录片），也可以下载单个视频\n'
            'get_video 或 v：    获取特定的单个视频，在用户不希望下载系列其他视频的时候可以使用\n'
            'get_up 或 up：      获取某个up的所有投稿视频，支持数量选择，关键词搜索，排序\n'
            'get_cate 或 cate：  获取分区视频，支持数量选择，关键词搜索，排序\n'
            'get_favour 或 fav： 获取收藏夹内视频，支持数量选择，关键词搜索\n'
            'get_collect 或 col：获取合集或视频列表内视频\n'
            'info：              打印url所属资源的详细信息（例如点赞数，画质，编码格式等）',
            'get_series or s:   download whole series videos (including multi-part uploads, anime, series, movies, documentaries), or single videos\n'
            'get_video or v:    download a specific video when you do not want other videos in the series\n'
            'get_up or up:      download all uploads from a user, supports count limits, keyword search, and sorting\n'
            'get_cate or cate:  download partition videos, supports count limits, keyword search, and sorting\n'
            'get_favour or fav: download videos from favorites, supports count limits, keyword search\n'
            'get_collect or col:download videos from a collection or playlist\n'
            'info:              print detailed resource information (e.g. likes, quality, codec)'
        )
    )
    table.add_row(
        "[cyan]<key>[/cyan]",
        text(
            '如使用get_video/get_series，填写视频的url\n'
            '如使用get_up，填写b站用户空间页url或用户id\n'
            '如使用get_cate，填写分区名称\n'
            '如使用get_favour，填写收藏夹页url或收藏夹id\n'
            '如使用get_collect，填写合集或者视频列表详情页url\n'
            '如使用info，填写任意资源url',
            'For get_video/get_series, provide the video URL\n'
            'For get_up, provide a Bilibili user page URL or user ID\n'
            'For get_cate, provide a category name\n'
            'For get_favour, provide a favorites page URL or favorites ID\n'
            'For get_collect, provide a collection or playlist URL\n'
            'For info, provide any resource URL'
        )
    )
    console.print(table)
    table = Table(highlight=True, box=None, show_header=False)
    table.add_column("OPTIONS", no_wrap=True, justify="left", style="bold")
    table.add_column("type", no_wrap=True, justify="left", style="bold")
    table.add_column("Description", )
    table.add_row(
        "-d --dir",
        '[dark_cyan]str',
        text(
            "文件的下载目录，默认当前路径下的videos文件夹下，不存在会自动创建",
            "Download directory. Defaults to ./videos and will be created if missing"
        )
    )
    table.add_row(
        "-q --quality",
        '[dark_cyan]int | str',
        text(
            "视频画面质量，默认0为最高画质，越大画质越低，超出范围时自动选最低画质，或者直接使用字符串指定'1080p'等名称",
            "Video quality. Default 0 is highest, larger values are lower quality. Use strings like '1080p'"
        )
    )
    table.add_row(
        "-vc --video-con",
        '[dark_cyan]int',
        text(
            "控制最大同时下载的视频数量，理论上网络带宽越高可以设的越高，默认3",
            "Maximum concurrent downloads. Default 3"
        ),
    )
    table.add_row(
        "-pc --part-con",
        '[dark_cyan]int',
        text(
            "控制每个媒体的分段并发数，默认10",
            "Maximum segment concurrency per media. Default 10"
        ),
    )
    table.add_row(
        '--cookie',
        '[dark_cyan]str',
        text(
            '有条件的用户可以提供大会员的SESSDATA来下载会员视频',
            'Premium users may provide SESSDATA to download member-only videos'
        )
    )
    table.add_row(
        "-fb --from-browser", '[dark_cyan]str',
        text(
            '从哪个浏览器中导入cookies，例如safari，chrome，edge...默认无',
            'Import cookies from a browser like safari, chrome, edge... default none'
        ),
    )
    table.add_row(
        '--days',
        '[dark_cyan]int',
        text(
            '过去days天中的结果，默认为7，仅get_up, get_cate时生效',
            'Results from the past number of days. Default 7. Only effective for get_up and get_cate'
        )
    )
    table.add_row(
        "-n --num",
        '[dark_cyan]int',
        text(
            "下载前多少个投稿，仅get_up，get_cate，get_favor时生效",
            "Number of uploads to download. Only effective for get_up, get_cate, get_favor"
        ),
    )
    table.add_row(
        "--order",
        '[dark_cyan]str',
        text(
            '何种排序，pubdate发布时间（默认）， click播放数，scores评论数，stow收藏数，coin硬币数，dm弹幕数, 仅get_up, get_cate时生效',
            'Sort order: pubdate (default), click, scores, stow, coin, dm. Only effective for get_up, get_cate'
        ),
    )
    table.add_row(
        "--keyword",
        '[dark_cyan]str',
        text(
            '搜索关键词， 仅get_up, get_cate，get_favor时生效',
            'Search keyword. Only effective for get_up, get_cate, get_favor'
        ),
    )
    table.add_row(
        "-ns --no-series", '',
        text(
            '只下载搜索结果每个视频的第一p，仅get_up，get_cate，get_favour时生效',
            'Download only the first part of search results. Only effective for get_up, get_cate, get_favour'
        ),
    )
    table.add_row(
        "-nh --no-hierarchy", '',
        text(
            '不使用层次目录，所有视频统一保存在下载目录下',
            'Do not use hierarchical directories; save all videos under the download directory'
        )
    )
    table.add_row(
        "--image", '',
        text(
            '下载视频封面',
            'Download cover image'
        )
    )
    table.add_row(
        "--subtitle", '',
        text(
            '下载srt字幕',
            'Download SRT subtitles'
        ),
    )
    table.add_row(
        "--dm", '',
        text(
            '下载弹幕',
            'Download danmaku comments'
        ),
    )
    table.add_row(
        "-oa --only-audio", '',
        text(
            '仅下载音频，下载的音质固定为最高音质',
            'Download audio only, quality fixed to highest'
        ),
    )
    table.add_row(
        "-p", '[dark_cyan]int, int',
        text(
            '下载集数范围，例如-p 1 3 只下载P1至P3，仅get_series时生效',
            'Download episode range, e.g. -p 1 3 downloads P1 to P3. Only effective for get_series'
        ),
    )
    table.add_row(
        "--codec", '[dark_cyan]str',
        text(
            '视频及音频编码（可使用info查看后填写，使用:分隔），可使用完整名称（例如avc1.640032，fLaC）或部分名称（例如avc，hev）',
            'Video/audio codec (use info to inspect first). Use full names like avc1.640032 or fLaC, or partial names like avc, hev'
        ),
    )
    table.add_row(
        "-sl --speed-limit", '[dark_cyan]str',
        text(
            '最大下载速度，默认无限制。例如：-sl 1.5MB',
            'Maximum download speed. Default unlimited. Example: -sl 1.5MB'
        ),
    )
    table.add_row(
        "-sr --stream-retry", '[dark_cyan]int',
        text(
            '下载过程中发生网络错误后最大重试数，默认5',
            'Maximum retries for network errors during download. Default 5'
        ),
    )
    table.add_row(
        "-tr --time-range", '[dark_cyan]str',
        text(
            r'下载视频的时间范围，格式如 h:m:s-h:m:s 或 s-s，默认无，仅get_video时生效',
            r'Download time range format h:m:s-h:m:s or s-s. Default none. Only effective for get_video'
        ),
    )
    table.add_row("-h --help", '', text('帮助信息', 'Show help'))
    table.add_row("-v --version", '', text('版本信息', 'Show version'))
    table.add_row("--debug", '', text('显示debug信息', 'Show debug information'))
    table.add_row("--language, --locale, -l", '[dark_cyan]str', text('语言设置，支持zh（默认）和en', 'Language setting, supports zh (default) and en'))
    console.print(Panel(table, border_style="dim", title="Options", title_align="left"))


class BasedQualityType(click.ParamType):
    name = "quality"

    def convert(self, value, param, ctx):
        try:
            value = int(value)
        except ValueError:
            return value  # str
        if value in {1080, 720, 480, 360}:
            return str(value)
        else:
            return value  # relative choice like 0, 1, 2, 999...


class BasedSpeedLimit(click.ParamType):
    name = "speed_limit"

    def convert(self, value, param, ctx):
        if value is not None:
            return parse_bytes_str(value)


class BasedTimeRange(click.ParamType):
    name = "time_range"

    def convert(self, value, param, ctx):
        start_time, end_time = map(s2t, value.split('-'))
        return start_time, end_time


@click.command(add_help_option=False)
@click.argument("method", type=str)
@click.argument("keys", type=str, nargs=-1, required=True)
@click.option(
    "-d",
    "--dir",
    "path",
    type=Path,
    default='videos',
)
@click.option(
    '-q',
    '--quality',
    'quality',
    type=BasedQualityType(),
    default=0,  # default relatively choice
)
@click.option(
    '-vc',
    '--video-con',
    'video_concurrency',
    type=int,
    default=3,
)
@click.option(
    '-pc',
    "--part-con",
    "part_concurrency",
    type=int,
    default=10,
)
@click.option(
    '--cookie',
    'cookie',
    type=str,
)
@click.option(
    '--days',
    'days',
    type=int,
    default=7,
)
@click.option(
    '-n',
    '--num',
    type=int,
    default=10,
)
@click.option(
    '--order',
    'order',
    type=str,
    default='pubdate',
)
@click.option(
    '--keyword',
    'keyword',
    type=str
)
@click.option(
    '-ns',
    '--no-series',
    'series',
    is_flag=True,
    default=True,
)
@click.option(
    '-nh',
    '--no-hierarchy',
    'hierarchy',
    is_flag=True,
    default=True,
)
@click.option(
    '--image',
    'image',
    is_flag=True,
    default=False,
)
@click.option(
    '--subtitle',
    'subtitle',
    is_flag=True,
    default=False,
)
@click.option(
    '--dm',
    'dm',
    is_flag=True,
    default=False,
)
@click.option(
    '-oa',
    '--only-audio',
    'only_audio',
    is_flag=True,
    default=False,
)
@click.option(
    '-p',
    'p_range',
    type=(int, int),
)
@click.option(
    '--codec',
    'codec',
    type=str,
    default=''
)
@click.option(
    '--speed-limit',
    '-sl',
    'speed_limit',
    type=BasedSpeedLimit(),
    default=None,
)
@click.option(
    '--stream-retry',
    '-sr',
    'stream_retry',
    type=int,
    default=5
)
@click.option(
    '--from-browser',
    '-fb',
    'browser',
    type=str,
)
@click.option(
    '--language',
    '--locale',
    '-l',
    'language',
    type=click.Choice(['zh', 'cn', 'en'], case_sensitive=False),
    default=None,
    show_default=False,
    is_eager=True,
    expose_value=True,
    callback=handle_language,
    help='Language for CLI output and log messages. Default is Chinese.',
)
@click.option(
    '--time-range',
    '-tr',
    'time_range',
    type=BasedTimeRange(),
    default=None,
)
@click.option(
    '-h',
    "--help",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    callback=handle_help,
)
@click.option(
    '-v',
    "--version",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    callback=handle_version,
)
@click.option(
    "--debug",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    callback=handle_debug,
)
def main(**kwargs):
    if kwargs.get('language') is not None:
        set_language(kwargs.get('language'))
    loop = asyncio.new_event_loop()  # avoid deprecated warning in 3.11
    asyncio.set_event_loop(loop)
    logger.debug(f'CLI KEY METHOD and OPTIONS: {kwargs}')
    try:
        # CLIProgress.switch_theme(gs="cyan", bs="dark_cyan")
        CLIProgress.start()  # start progress
        if not kwargs['path'].exists():
            kwargs['path'].mkdir(parents=True)
            logger.info(t('cli.dir.created', path=kwargs['path']))
        executor, cor = assign(kwargs)
        loop.run_until_complete(cor)
    except HandleError as e:  # method no match
        logger.error(e)
    except KeyboardInterrupt:
        logger.info(t('cli.user.interrupt'))
    finally:
        CLIProgress.stop()  # stop rich progress to ensure cursor is repositioned
