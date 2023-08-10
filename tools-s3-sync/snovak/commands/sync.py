import boto3
import os
import typer
from snovak.commands.results import SyncCommandResult
from snovak.infrastructure import logger

def execute(bucket: str, local_dir: str) -> None:
    """
    Perform an rsync between an S3 bucket and a local directory.
    """


    command_result = _download_dir(bucket, "", local_dir)
    typer.echo(f"Synchronization from {bucket} to {local_dir} completed.")



def _download_dir( bucket: str, path: str, local: str) -> None:
    """
    Download a directory from S3 to a local path.
    """
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects')
    command_result = SyncCommandResult
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=path):
        common_prefixes = result.get('CommonPrefixes')
        if not common_prefixes:
            continue
        for subdir in common_prefixes:
            download_dir(s3, bucket, subdir.get('Prefix'), os.path.join(local, subdir.get('Prefix')))

        contents = result.get('Contents')
        if not contents:
            continue

        for file_info in contents:
            local_file_path = os.path.join(local, file_info.get('Key'))
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            s3.download_file(bucket, file_info.get('Key'), local_file_path)
            command_result.increment_synced()

    return command_result

