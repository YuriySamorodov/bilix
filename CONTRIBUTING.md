# bilix 开发指南

感谢你对 bilix 的贡献兴趣。在开始之前，你可以阅读下面的一些提示。请注意 bilix 正在快速迭代，若你发现文档与代码有差异，请以 `master` 分支的代码为准。

# 开始之前

在一切开始之前，你需要先 **fork** 本仓库，然后 clone 你的 fork 到本地：

```shell
git clone https://github.com/your_user_name/bilix
```

建议你在独立的 Python 环境中开发和测试，然后使用可编辑安装：

```shell
pip install -e .
```

确认 `bilix` 命令能够正常执行后，就可以开始开发了。🍻

# bilix 结构

在开始修改代码之前，先了解一下 bilix 的目录结构：

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

# 贡献流程

1. 新增功能或修复 bug 时，请先查看仓库现有的测试和样例。
2. 你可以直接修改代码并运行本地测试。
3. 提交前建议执行：

```shell
pip install -e .
pytest
```

# 注意事项

- `bilix -h` 显示完整帮助。
- `bilix -l en -h` 可以查看英文帮助。
- 若你在开发新站点，请参照 `bilix/sites` 下已有站点的实现。
- 任何翻译、文档或帮助信息更新，请同时检查 `bilix/i18n/zh.json` 和 `bilix/i18n/en.json`。
