
from typing import Optional

import typer

from snovak import __app_name__, __version__
import snovak.commands.sync
import snovak.infrastructure.config as config
import snovak.infrastructure.logger as logger

app = typer.Typer()

__all__ = ["app", "main"]

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        logger.log_message(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def sync(bucket: str, local_dir: str) -> None:
    """
    Perform an rsync between an S3 bucket and a local directory.
    """
    logger.log_message(f"Sync command called with bucket: {bucket} and local_dir: {local_dir}")
    snovak.commands.sync.execute(bucket, local_dir)