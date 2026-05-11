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
    text = lambda key: help_text(key, language)
    console.print(f"\n[bold]bilix {__version__}", justify="center")
    console.print(text("help.title"), justify="center")
    console.print(text("help.usage"), justify="left")
    table = Table.grid(padding=1, pad_edge=False)
    table.add_column("Parameter", no_wrap=True, justify="left", style="bold")
    table.add_column("Description")

    table.add_row(
        "[cyan]<method>",
        text("help.method")
    )
    table.add_row(
        "[cyan]<key>[/cyan]",
        text("help.key")
    )
    console.print(table)
    table = Table(highlight=True, box=None, show_header=False)
    table.add_column("OPTIONS", no_wrap=True, justify="left", style="bold")
    table.add_column("type", no_wrap=True, justify="left", style="bold")
    table.add_column("Description", )
    table.add_row(
        "-d --dir",
        '[dark_cyan]str',
        text("help.option.dir")
    )
    table.add_row(
        "-q --quality",
        '[dark_cyan]int | str',
        text("help.option.quality")
    )
    table.add_row(
        "-vc --video-con",
        '[dark_cyan]int',
        text("help.option.video_concurrency"),
    )
    table.add_row(
        "-pc --part-con",
        '[dark_cyan]int',
        text("help.option.part_concurrency"),
    )
    table.add_row(
        '--cookie',
        '[dark_cyan]str',
        text("help.option.cookie")
    )
    table.add_row(
        "-fb --from-browser", '[dark_cyan]str',
        text("help.option.from_browser"),
    )
    table.add_row(
        '--days',
        '[dark_cyan]int',
        text("help.option.days")
    )
    table.add_row(
        "-n --num",
        '[dark_cyan]int',
        text("help.option.num"),
    )
    table.add_row(
        "--order",
        '[dark_cyan]str',
        text("help.option.order"),
    )
    table.add_row(
        "--keyword",
        '[dark_cyan]str',
        text("help.option.keyword"),
    )
    table.add_row(
        "-ns --no-series", '',
        text("help.option.no_series"),
    )
    table.add_row(
        "-nh --no-hierarchy", '',
        text("help.option.no_hierarchy")
    )
    table.add_row(
        "--image", '',
        text("help.option.image")
    )
    table.add_row(
        "--subtitle", '',
        text("help.option.subtitle"),
    )
    table.add_row(
        "--dm", '',
        text("help.option.dm"),
    )
    table.add_row(
        "-oa --only-audio", '',
        text("help.option.only_audio"),
    )
    table.add_row(
        "-p", '[dark_cyan]int, int',
        text("help.option.p"),
    )
    table.add_row(
        "--codec", '[dark_cyan]str',
        text("help.option.codec"),
    )
    table.add_row(
        "-sl --speed-limit", '[dark_cyan]str',
        text("help.option.speed_limit"),
    )
    table.add_row(
        "-sr --stream-retry", '[dark_cyan]int',
        text("help.option.stream_retry"),
    )
    table.add_row(
        "-tr --time-range", '[dark_cyan]str',
        text("help.option.time_range"),
    )
    table.add_row("-h --help", '', text("help.option.help"))
    table.add_row("-v --version", '', text("help.option.version"))
    table.add_row("--debug", '', text("help.option.debug"))
    table.add_row("--language, --locale, -l", '[dark_cyan]str', text("help.option.language"))
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
