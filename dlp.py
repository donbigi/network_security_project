import csv
from google.cloud import dlp_v2  # Import directly without alias

def anonymize_data(
    project: str,
    input_csv_file: str,
    output_csv_file: str,
    sensitive_fields: list
) -> None:
    """
    Uses Google DLP to anonymize sensitive fields (IP addresses, emails) in a CSV file.
    """
    # Instantiate the DLP client using the imported module name
    dlp_client = dlp_v2.DlpServiceClient()
    parent = f"projects/{project}/locations/global"

    # Read CSV file
    with open(input_csv_file, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Extract headers
        rows = list(reader)     # Extract data

    # Identify sensitive column indexes
    field_indexes = [headers.index(field) for field in sensitive_fields if field in headers]

    # Convert CSV rows to DLP-compatible format
    def map_rows(row):
        return {"values": [{"string_value": value} for value in row]}
    csv_rows = list(map(map_rows, rows))
    
    # Create a table item for DLP processing
    table_item = {
        "table": {
            "headers": [{"name": h} for h in headers],
            "rows": csv_rows
        }
    }

    # Define the de-identification configuration using info_type_transformations
    deidentify_config = {
        "record_transformations": {
            "field_transformations": [
                {
                    "fields": [{"name": headers[i]} for i in field_indexes],
                    "info_type_transformations": {
                        "transformations": [
                            {
                                "primitive_transformation": {
                                    "replace_with_info_type_config": {}
                                },
                                # Specify info types; adjust based on the field type
                                "info_types": [
                                    {"name": "IP_ADDRESS"}
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }

    # Call DLP API for anonymization
    response = dlp_client.deidentify_content(
        request={
            "parent": parent,
            "deidentify_config": deidentify_config,
            "item": table_item,
        }
    )

    # Write anonymized data back to a CSV file
    def write_data(value):
        return value.string_value

    with open(output_csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers
        for row in response.item.table.rows:
            writer.writerow([write_data(value) for value in row.values])

    print(f"Anonymized data saved to {output_csv_file}")

# Example Usage:
anonymize_data("ghyve-non-production", "E-commerce_Website_Logs.csv", "anonymized_logs.csv", ["ip"])
