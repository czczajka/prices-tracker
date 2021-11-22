#!/usr/bin/env bash

name_var=big_mac
date_var=$(echo -n `date +"%Y-%m-%d"`)
price_var=$(python scripts/big_mac_parser.py)
echo $price_var

curl -X 'POST' \
  'https://price-trend.herokuapp.com/add_entry/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "item_name": "'"$name_var"'",
    "date": "'"$date_var"'",
    "price": "'$price_var'"
  }'

name_var=cheesburger
date_var=$(echo -n `date +"%Y-%m-%d"`)
price_var=$(python scripts/cheesburger_parser.py)
echo $price_var

curl -X 'POST' \
  'https://price-trend.herokuapp.com/add_entry/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "item_name": "'"$name_var"'",
    "date": "'"$date_var"'",
    "price": "'$price_var'"
  }'

name_var=dolar_amerykanski
date_var=$(echo -n `date +"%Y-%m-%d"`)
price_var=$(python scripts/dolar_amerykanski_parser.py)
echo $price_var

curl -X 'POST' \
  'https://price-trend.herokuapp.com/add_entry/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "item_name": "'"$name_var"'",
    "date": "'"$date_var"'",
    "price": "'$price_var'"
  }'

curl https://price-trend.herokuapp.com/g_plots/
