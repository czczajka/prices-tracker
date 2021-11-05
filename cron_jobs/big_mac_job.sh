#!/usr/bin/env bash

echo -n `date +"%Y-%m-%d,"` >>  /app/data/big_mac_data.txt
python /app/scripts/big_mac_parser.py >> /app/data/big_mac_data.txt

echo -n `date +"%Y-%m-%d,"` >>  /app/data/coca_cola_data.txt
python /app/scripts/coca_cola_parser.py >> /app/data/coca_cola_data.txt

curl https://price-trend.herokuapp.com/g_plots
