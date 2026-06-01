# More

## Feedback

If you find any bugs or issues, please open an [Issue](https://github.com/HFrost0/bilix/issues).

If you have new ideas or feature requests, join the [Discussion](https://github.com/HFrost0/bilix/discussions).

If this project helps you, please give a [Star](https://github.com/HFrost0/bilix/stargazers)🌟

## Contributing

❤️ Contributions are welcome! See [CONTRIBUTING.md](https://github.com/HFrost0/bilix/blob/master/CONTRIBUTING.md)

## Available features

- `get_series`, `get_video`, `get_up`, `get_cate`, `get_favour`, `get_collect`, `info`.
- `--subtitle`, `--dm`, `--image` for attachments.
- `--time-range` for segment downloads.
- `--language` / `--locale` / `-l` for Chinese and English help/log output.

## Logging

- bilix creates a `logs` directory in the current working directory at runtime.
- Logs are saved daily as `YYYY-MM-DD.log`, one file per day.
- Each audit entry records the date, file or request URL, file size, and status.
- Errors also include exception details and traceback output, which helps debug HTTP failures, retry exhaustion, and interrupted downloads.
- Use the `--log-dir` CLI option to set the logs directory. If a relative path is provided it will be created under the download output directory specified by `-d/--dir`. Default: `logs`.

## Known issue

If two video files have exactly the same name, task conflicts may occur without an error.
