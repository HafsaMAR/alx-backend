#!/usr/bin/env python3
import requests

url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240401%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240401T125010Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9ba3a96413591c8382b31c8ae9c512f6674ed032a9b864ef9156628e571f0a67"

response = requests.get(url)

if response.status_code == 200:
    with open("Popular_Baby_Names.csv", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download the file.")
