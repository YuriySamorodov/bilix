from __future__ import annotations

import json
from functools import lru_cache
from typing import Literal
import importlib.resources as resources

Language = Literal['zh', 'en']
DEFAULT_LANGUAGE: Language = 'zh'
SUPPORTED_LANGUAGES = ('zh', 'en')
ALIASES = {'cn': 'zh'}

_current_language: str | None = None


def _normalize_language(language: str | None) -> str | None:
    if language is None:
        return None
    language = str(language).lower()
    language = ALIASES.get(language, language)
    return language if language in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE


@lru_cache(maxsize=None)
def _load_translations(language: str) -> dict[str, str]:
    try:
        with resources.open_text(__package__, f"{language}.json", encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def set_language(language: str | None) -> None:
    global _current_language
    _current_language = _normalize_language(language)


def get_language() -> Language:
    return _normalize_language(_current_language) or DEFAULT_LANGUAGE


def get_explicit_language() -> str | None:
    return _normalize_language(_current_language)


def t(key: str, /, **kwargs) -> str:
    language = get_language()
    translations = _load_translations(language)
    template = translations.get(key, key)
    return template.format(**kwargs)


def help_text(zh: str, en: str, language: str | None = None) -> str:
    if language is None:
        return f"{zh}\n{en}"
    return zh if _normalize_language(language) == 'zh' else en


def bilingual(zh: str, en: str, language: str | None = None) -> str:
    return help_text(zh, en, language)
