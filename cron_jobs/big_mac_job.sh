#!/usr/bin/env bash

echo -n `date +"%Y-%m-%d,"` >>  ../data/big_mac_data.txt
python ../scripts/big_mac_parser.py >> ../data/big_mac_data.txt

echo -n `date +"%Y-%m-%d,"` >>  ../data/coca_cola_data.txt
python ../scripts/coca_cola_parser.py >> ../data/coca_cola_data.txt

curl https://price-trend.herokuapp.com/g_plots
