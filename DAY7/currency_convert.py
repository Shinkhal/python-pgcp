import csv
import json


def convert_log_file(input_log_path, output_csv_path, output_json_path):

    records = []
    with open(input_log_path, "r", encoding="utf-8") as file:

        for line in file:
            line = line.strip()

            if not line:
                continue
            
            timestamp, user_id, endpoint, status_code = line.split("|")

            record = {
                "timestamp": timestamp.strip(),
                "user_id": user_id.strip(),
                "endpoint": endpoint.strip(),
                "status_code": int(status_code.strip())
            }

            records.append(record)
    fieldnames = [
        "timestamp",
        "user_id",
        "endpoint",
        "status_code"
    ]

    with open(
        output_csv_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )
        writer.writeheader()
        writer.writerows(records)
    with open(output_json_path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)
