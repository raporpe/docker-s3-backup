# Backup folders to S3 compatible bucket

This is a little container image for backing up a folder to a object storage service such as AWS S3.

**Required environment variables:**

- ``ACCESS_KEY_ID``: AWS access key id or equivalent Key ID for other providers (Backblaze, Wasabi, etc.)
- ``SECRET_ACCESS_KEY``: AWS secret access key or equivalent Secret Key for other providers (Backblaze, Wasabi, etc.)
- ``BUCKET``: The bucket name in the S3 compatible storage
- ``CRON_SCHEDULE``: the cron schedule to run the backup. Example: 0 0 * * *

**Optional environment variables:**

- ``ENDPOINT_URL``: The endpoint URL for the S3 compatible storage. Example: https://s3.wasabisys.com





