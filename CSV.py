import io
import pandas as pd


def get_csv(bucket_object_body: object):
    return pd.read_csv(bucket_object_body)


def get_columns(csv_file):
    return csv_file.columns

def save_csv_file(dataframe):
    str_buffer = io.StringIO()
    dataframe.to_csv(str_buffer)
    return str_buffer


def put_object(str_buffer, client, csv_file):
    client.get_client().put_object(Body=str_buffer.getvalue(), Bucket=client.get_bucket_name(), Key=f"Data100/fish/Robert.csv")