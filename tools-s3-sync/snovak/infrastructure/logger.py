import snovak.config

import boto3

log_client = boto3.client('logs')

def log_message(message: str) -> None:
    """
    Log a message to CloudWatch Logs.
    """

    log_group_name = snovak.config.get_string('LOG_GROUP_NAME')
    log_stream_name = snovak.config.get_string('LOG_STREAM_NAME')

    log_client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[{
            'timestamp': int(round(time.time() * 1000)),
            'message': message
        }]
    )