#!/usr/bin/env sh

if [[ -z "${CRON_SCHEDULE}" ]]; then
  echo "CRON_SCHEDULE env variable is not set!"
  exit 1
fi

echo "${CRON_SCHEDULE} python3 /usr/src/backup.py" > /etc/crontabs/root

while true; do sleep 10000; done