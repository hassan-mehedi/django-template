"""
This file contains a definition for Content-Security-Policy headers.

Read more about it:
https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Content-Security-Policy

We are using `django-csp` to provide these headers.
Docs: https://github.com/mozilla/django-csp
"""

# CSP SRC Class
class CspSrc:
    """CSP Source Class"""
    SELF = "'self'"
    NONE = "'none'"

# These values might and will be redefined in `development.py` env:
CSP_SCRIPT_SRC: tuple[str, ...] = (CspSrc.SELF,)
CSP_IMG_SRC: tuple[str, ...] = (CspSrc.SELF,)
CSP_FONT_SRC: tuple[str, ...] = (CspSrc.SELF,)
CSP_STYLE_SRC: tuple[str, ...] = (CspSrc.SELF,)
CSP_DEFAULT_SRC: tuple[str, ...] = (CspSrc.NONE,)
CSP_CONNECT_SRC: tuple[str, ...] = ()
