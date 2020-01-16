from google.cloud import storage
import json
import os, time, random

def write_to_file():
    with open('new.txt', 'w') as f:
        for x in range(100):
            big_number = x**2
            time.sleep(3)
            f.write(f'{x}#Stress-{big_number}\n')


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    """
    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
    """

def create_bucket_f2():
    # Instantiates a client
    storage_client = storage.Client()

    token = random.randint(1000,9999)

    # The name for the new bucket
    bucket_name = f'mikael-sky-demo-bucket-{token}'

    # Creates the new bucket
    storage_client.create_bucket(bucket_name)

    write_to_file()
    upload_blob(bucket_name, 'new.txt', 'new_uplod')

    #print("Bucket {} created.".format(bucket.name))