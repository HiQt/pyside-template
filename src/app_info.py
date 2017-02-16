from collections import namedtuple


_AppInfo = namedtuple("AppInfo", [
    "APP_NAME", "APP_AUTHOR", "APP_VERSION"
])


_VerInfo = namedtuple("VerInfo", [
    "MAJOR", "MINOR", "REVISION"
])


APP_INFO = _AppInfo(
    APP_NAME="Some App",
    APP_AUTHOR="Some Author",
    APP_VERSION=_VerInfo(
        MAJOR=1,
        MINOR=2,
        REVISION=3
    )
)
