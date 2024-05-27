"""Common utilities"""

import re


def camel2snake(name: str) -> str:
    """Convert camel_case string to snakeCase"""
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("__([A-Z])", r"_\1", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


def snake2camel(name: str) -> str:
    """Convert snakeCase string to camel_case"""
    parts = name.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])
