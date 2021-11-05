#!/usr/bin/env bash

echo -n `date +"\%Y-\%m-\%d,"` >>  big_mac_data.txt
python ../scripts/big_mac_parser.py >> big_mac_data.txt
curl http://127.0.0.1:8000/g_plots
