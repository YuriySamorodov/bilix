import logging
from datetime import date
from pathlib import Path
from rich.logging import RichHandler


DEFAULT_AUDIT_DIR = Path(__file__).resolve().parent / 'logs'


class DailyFileHandler(logging.Handler):
    def __init__(self, log_dir: Path):
        super().__init__()
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self._stream = None
        self._stream_path = None

    def _get_stream(self, record: logging.LogRecord):
        log_path = self.log_dir / f"{date.fromtimestamp(record.created):%Y-%m-%d}.log"
        if log_path != self._stream_path:
            if self._stream is not None:
                self._stream.close()
            self._stream = log_path.open('a', encoding='utf-8')
            self._stream_path = log_path
        return self._stream

    def emit(self, record: logging.LogRecord):
        try:
            stream = self._get_stream(record)
            stream.write(self.format(record) + '\n')
            stream.flush()
        except Exception:
            self.handleError(record)

    def close(self):
        if self._stream is not None:
            self._stream.close()
            self._stream = None
            self._stream_path = None
        super().close()


class DefaultFieldsFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        if not hasattr(record, 'status'):
            record.status = '-'
        if not hasattr(record, 'url'):
            record.url = '-'
        if not hasattr(record, 'file_size'):
            record.file_size = '-'
        return True


def get_logger():
    bilix_logger = logging.getLogger("bilix")
    # 如果logger已经配置过handler，直接返回logger实例
    if bilix_logger.handlers:
        return bilix_logger
    bilix_logger.setLevel(logging.INFO)
    bilix_logger.propagate = False
    # 创建自定义的RichHandler
    custom_rich_handler = RichHandler(
        show_time=False,
        show_path=False,
        markup=True,
        keywords=RichHandler.KEYWORDS + ['STREAM'],
        rich_tracebacks=True
    )
    # 设置日志格式
    formatter = logging.Formatter("{message}", style="{", datefmt="[%X]")
    custom_rich_handler.setFormatter(formatter)
    # 为logger添加自定义的RichHandler
    bilix_logger.addHandler(custom_rich_handler)
    return bilix_logger


def get_audit_logger(log_dir: Path = None):
    audit_logger = logging.getLogger("bilix.audit")
    requested_dir = Path(log_dir) if log_dir is not None else None
    if audit_logger.handlers:
        if requested_dir is None:
            return audit_logger
        # check if existing DailyFileHandler uses same dir
        for h in audit_logger.handlers:
            if isinstance(h, DailyFileHandler) and h.log_dir == requested_dir:
                return audit_logger
        # otherwise reconfigure handlers to use requested_dir
        for h in list(audit_logger.handlers):
            audit_logger.removeHandler(h)
            try:
                h.close()
            except Exception:
                pass

    audit_logger.setLevel(logging.INFO)
    audit_logger.propagate = False
    handler = DailyFileHandler(requested_dir or DEFAULT_AUDIT_DIR)
    handler.addFilter(DefaultFieldsFilter())
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(status)s | %(url)s | %(file_size)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ))
    audit_logger.addHandler(handler)
    return audit_logger


def log_event(status: str, message: str = "", *, url: str = "-", file_size=None, level=logging.INFO,
              exception: Exception = None):
    audit_logger = get_audit_logger()
    extra = {
        'status': status,
        'url': url,
        'file_size': file_size if file_size is not None else '-',
    }
    if exception is not None:
        audit_logger.error(message, extra=extra, exc_info=(type(exception), exception, exception.__traceback__))
    else:
        audit_logger.log(level, message, extra=extra)


logger = get_logger()
