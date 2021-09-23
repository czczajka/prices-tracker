import csv
import random
from datetime import timedelta
from schemas import csvCreate


def create_file(data: csvCreate):
    header = ['date', 'price']
    delta = timedelta(days=30)

    with open(f'csv-db/{data.name}.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        while data.start_date <= data.end_date:
            record = [data.start_date, round(random.uniform(data.min_price, data.max_price), 2)]

            # write the data
            writer.writerow(record)

            data.start_date += delta
