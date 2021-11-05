#!/usr/bin/env bash

echo -n `date +"%Y-%m-%d,"` >>  /app/cron_jobs/data/big_mac_data.txt
python /app/cron_jobs/scripts/big_mac_parser.py >> /app/cron_jobs/data/big_mac_data.txt

echo -n `date +"%Y-%m-%d,"` >>  /app/cron_jobs/data/coca_cola_data.txt
python /app/cron_jobs/scripts/coca_cola_parser.py >> /app/cron_jobs/data/coca_cola_data.txt

curl https://price-trend.herokuapp.com/g_plots
