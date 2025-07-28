__author__ = "jschulz"

from .py3compat import string_types


class _NA_DEFAULT_CLASS:
    pass


_NA_DEFAULT = _NA_DEFAULT_CLASS()


def get_by_name(dict_like, name, na="<n/a"):
    res = dict_like
    for part in name.split("."):
        try:
            res = res.get(part, _NA_DEFAULT)
        except:
            return na
        if res is _NA_DEFAULT:
            return na
    return res


def filter_for_debug(msg, names=None):
    if names is None:
        names = ["msg_type", "content.data"]

    # example...
    {
        "parent_header": {
            "username": "username",
            "version": "5.0",
            "msg_type": "execute_request",
            "msg_id": "4383f7f6-0b2f-4ad8-80c8-4f790e3bf389",
            "session": "6925e9c2-29f1-44a6-9af1-8b375bc996cc",
            "date": datetime.datetime(2015, 2, 26, 1, 44, 45, 925000),
        },
        "msg_type": "execute_reply",
        "msg_id": "8b22db97-9106-40cb-9e23-eda214bfa499",
        "content": {
            "status": "ok",
            "execution_count": 2,
            "user_expressions": {},
            "payload": [],
        },
        "header": {
            "username": "username",
            "version": "5.0",
            "msg_type": "execute_reply",
            "msg_id": "8b22db97-9106-40cb-9e23-eda214bfa499",
            "session": "45cc1a4f-dd43-4067-838d-412e2e16bb7d",
            "date": datetime.datetime(2015, 2, 26, 1, 44, 45, 936000),
        },
        "buffers": [],
        "metadata": {
            "dependencies_met": True,
            "engine": "6364f52f-1366-4e5c-999e-326736541ff1",
            "status": "ok",
            "started": "2015-02-26T01:44:45.926000",
        },
    }
    ret = {}
    for name in names:
        ret[name] = get_by_name(msg, name)
    return ret


def _plain_text(content):
    data = content.get("data")
    if data is not None:
        return data.get("text/plain", "")
    else:
        return ""


def _code(content):
    return content.get("code", "")


def is_iterable(obj):
    "return true if *obj* is iterable"
    try:
        iter(obj)
    except TypeError:
        return False
    return True


def is_string(obj):
    return isinstance(obj, string_types)


import re

from traitlets import TraitType


class CRegExpMultiline(TraitType):
    """A casting compiled regular expression trait.

    Accepts both strings and compiled regular expressions. The resulting
    attribute will be a compiled regular expression."""

    info_text = "a regular expression"

    def validate(self, obj, value):
        try:
            return re.compile(value, re.MULTILINE)
        except:
            self.error(obj, value)
