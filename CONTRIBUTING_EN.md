# Development guide of bilix

Thank you for your interest in contributing to bilix. Before you start, please read the notes below. bilix is rapidly iterating, so if the documentation is outdated, refer to the code on the `master` branch.

# Before starting

First, **fork** this repository and clone your fork:

```shell
git clone https://github.com/your_user_name/bilix
```

After cloning, develop in an isolated Python environment and install the package in editable mode:

```shell
pip install -e .
```

Try whether the `bilix` command works. If it does, you are ready to develop locally. 🍻

# Structure of bilix

Before making changes, understand the main structure of bilix:

```text
bilix
├── __init__.py
├── __main__.py
├── _process.py
├── cli
│   ├── assign.py
│   └── main.py
├── download
│   ├── base_downloader.py
│   ├── base_downloader_m3u8.py
│   ├── base_downloader_part.py
│   └── utils.py
├── exception.py
├── log.py
├── progress
│   ├── abc.py
│   ├── cli_progress.py
│   └── ws_progress.py
├── serve
│   ├── __init__.py
│   ├── app.py
│   ├── auth.py
│   ├── serve.py
│   └── user.py
├── i18n
│   ├── __init__.py
│   ├── zh.json
│   └── en.json
├── sites
└── utils.py
```

# Basic workflow

1. Make sure your code is covered by tests and the existing examples.
2. Run local tests when possible.
3. Before submitting, use:

```shell
pip install -e .
pytest
```

# Notes

- Use `bilix -h` to see full command help.
- Use `bilix -l en -h` to show English help and logs.
- When you add or update feature text, keep both `bilix/i18n/zh.json` and `bilix/i18n/en.json` in sync.
- New site support should follow the existing pattern in `bilix/sites`.
