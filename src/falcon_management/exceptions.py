# coding=utf-8


class NoCommandSpecified(Exception):
    """
    An error specifying that a management command was not found
    """


class CommandNotFound(Exception):
    """
    An error specifying that a management command was not found
    """


class CommandFailed(Exception):
    """
    An error specifying that the task was unsuccessful
    """
