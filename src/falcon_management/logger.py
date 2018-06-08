TERMINAL_FAIL = '\033[91m'
TERMINAL_SUCCESS = '\033[92m'
TERMINAL_WARNING = '\033[93m'
TERMINAL_INFO = '\033[94m'
TERMINAL_END = '\033[0m'


def log(text, color):
    print(color + text + TERMINAL_END)


def info(text):
    log(text, TERMINAL_INFO)


def warn(text):
    log(text, TERMINAL_WARNING)


def error(text):
    log(text, TERMINAL_FAIL)


def success(text):
    log(text, TERMINAL_SUCCESS)
