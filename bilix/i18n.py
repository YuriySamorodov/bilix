from __future__ import annotations

from typing import Literal

Language = Literal['zh', 'en']
DEFAULT_LANGUAGE: Language = 'zh'
SUPPORTED_LANGUAGES = ('zh', 'en')
ALIASES = {'cn': 'zh'}

_current_language: str | None = None

MESSAGES = {
    'cli.dir.created': {
        'zh': '目录 {path} 不存在，已自动创建',
        'en': 'Directory {path} cannot be found, auto created',
    },
    'cli.user.interrupt': {
        'zh': '[cyan]提示：用户中断，重复执行命令可继续下载',
        'en': '[cyan]Hint: interrupted by user, rerun the command to resume downloads',
    },
    'log.http.unknown_exception': {
        'zh': '{method} {exception} 未知异常 url: {url}',
        'en': '{method} {exception} unknown exception url: {url}',
    },
    'log.http.retry_exceeded': {
        'zh': '{method} 超过重复次数 {url_or_urls}',
        'en': '{method} exceeded retry count {url_or_urls}',
    },
    'log.exists': {
        'zh': '[green]已存在[/green] {name}',
        'en': '[green]Exists[/green] {name}',
    },
    'log.completed': {
        'zh': '[cyan]已完成[/cyan] {name}',
        'en': '[cyan]Completed[/cyan] {name}',
    },
    'log.stream.retry_exceeded': {
        'zh': 'STREAM 超过重复次数 {name}',
        'en': 'STREAM exceeded retry count {name}',
    },
    'log.bilibili.quality_unavailable': {
        'zh': '{task_name} 清晰度<{quality}> 编码<{codec}>不可用，请检查输入是否正确或是否需要大会员',
        'en': '{task_name} quality<{quality}> codec<{codec}> unavailable, please check your input or premium requirements',
    },
    'log.bilibili.dash_fallback': {
        'zh': '{task_name} 未解析到dash资源，转入durl mp4/flv下载（不需要会员的电影/番剧预览，不支持dash的视频）',
        'en': '{task_name} failed to parse DASH resources, falling back to durl mp4/flv downloads (preview for non-premium video, does not support DASH-only videos)',
    },
    'log.bilibili.premium_or_region_unsupported': {
        'zh': '{task_name} 需要大会员或该地区不支持',
        'en': '{task_name} requires premium access or is not supported in this region',
    },
    'cli.debug.enabled': {
        'zh': 'Debug 开启，更多信息将显示',
        'en': 'Debug enabled, more information will be shown',
    },
}


def set_language(language: str | None) -> None:
    global _current_language
    if language is None:
        _current_language = None
        return
    language = str(language).lower()
    language = ALIASES.get(language, language)
    if language not in SUPPORTED_LANGUAGES:
        language = DEFAULT_LANGUAGE
    _current_language = language


def get_language() -> Language:
    return _current_language if _current_language is not None else DEFAULT_LANGUAGE


def get_explicit_language() -> str | None:
    return _current_language


def t(key: str, /, **kwargs) -> str:
    message = MESSAGES.get(key, {})
    language = get_language()
    template = message.get(language, message.get(DEFAULT_LANGUAGE, key))
    return template.format(**kwargs)


def bilingual(zh: str, en: str) -> str:
    return f"{zh}\n{en}"


def help_text(zh: str, en: str, language: str | None = None) -> str:
    if language is None:
        return bilingual(zh, en)
    if language == 'zh':
        return zh
    return en
