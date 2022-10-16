# Backup folder to S3 compatible bucket

This Docker image requires the following environment variables:

- ``ACCESS_KEY_ID``: AWS access key id or equivalent Key ID for other providers (Backblaze, Wasabi, etc.)
- ``SECRET_ACCESS_KEY``: AWS secret access key or equivalent Secret Key for other providers (Backblaze, Wasabi, etc.)
- ``BUCKET``: The bucket name in the S3 compatible storage
- ``CRON_SCHEDULE``: the cron schedule to run the backup. Example: 0 0 * * *

A custom S3-compatible API endpoint can be specified with the ENDPOINT environment variable.





