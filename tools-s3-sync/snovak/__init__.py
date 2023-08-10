"""Top-level package for our super cool TOOL """
# src/__init__.py 
__app_name__ = "tools-s3-sync"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    AWS_ERROR,
    OTHER_ERROR
) = range(5)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    AWS_ERROR: "aws error",
    OTHER_ERROR: "other error"
}