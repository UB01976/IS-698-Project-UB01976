import json
import boto3
import urllib.parse
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def lambda_handler(event, context):

    logger.info("Received event: %s", json.dumps(event))
    for record in event.get("Records", []):
        try:
            s3_info = record.get("s3", {})
            bucket = s3_info.get("bucket", {}).get("name")
            key = s3_info.get("object", {}).get("key")
            size = s3_info.get("object", {}).get("size")

            if key:
                key = urllib.parse.unquote_plus(key)
            event_time = record.get("eventTime")
            event_name = record.get("eventName")

            if size is None and bucket and key:
                try:
                    head = s3.head_object(Bucket=bucket, Key=key)
                    size = head.get("ContentLength")
                except Exception as e:
                    logger.warning("Could not head_object for %s/%s: %s", bucket, key, str(e))

            logger.info("S3 Upload - bucket: %s, key: %s, size: %s, event: %s, time: %s",
                        bucket, key, size, event_name, event_time)
        except Exception as e:
            logger.exception("Error processing record: %s", str(e))
    return {"status": "ok"}
