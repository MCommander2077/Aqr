import requests


def download_gsheets(file_id):
    # 设置Gsheets API的URL
    gsheets_url = f"http://154.12.38.20/spreadsheets/d/{file_id}/export?format=xlsx"

    # Send a GET request to download the file
    response = requests.get(gsheets_url)

    contents = response.content
    # Save the response content to a file
    with open("gsheets_data.xlsx", "wb") as file:
        file.write(contents)


if __name__ == '__main__':
    download_gsheets('1bZcB1wcdlNxXianLqJEHBh6BOSczN9yw73NSUaTDaNA')
