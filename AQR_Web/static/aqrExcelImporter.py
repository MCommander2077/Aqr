import pandas as pd


def excelimport():
    df = pd.read_excel('./gsheets_data.xlsx', sheet_name='主表')

    ids = df.values[:, 0].tolist()
    hrefs = df.values[:, 11].tolist()
    print(hrefs)
    artists = df.values[:, 2].tolist()
    songs = df.values[:, 1].tolist()
    authors = df.values[:, 3].tolist()
    levels = df.values[:, 6].tolist()
    difficulties = df.values[:, 5].tolist()
    vluations = df.values[:, 7].tolist()
    vluation_colors = []
    video_herfs = df.values[:, 12].tolist()

    bdjs = 'let buttonsData = ['

    for i in range(len(hrefs)):
        song = str(songs[i]).replace('"', '“').replace('\n', '').replace('\r', '')
        author = str(authors[i]).replace('"', '“').replace('\n', '').replace('\r', '')
        artist = str(artists[i]).replace('"', '“').replace('\n', '').replace('\r', '')
        href = str(hrefs[i]).replace('\n', '').replace('\r', '')
        video_href = str(video_herfs[i]).replace('\\', '/').replace('\n', '').replace('\r', '')
        button_data = '{' + f'''
        "href": "{href}", 
        "imgSrc_lv": "", 
        "imgSrc_df": "", 
        "artist": "{artist}", 
        "song": "{song}", 
        "author": "{author}", 
        "level": "{levels[i]}", 
        "difficulties": "{difficulties[i]}", 
        "vluation": "{vluations[i]}", 
        "vluation_color": "rgb(255,255,255)",
        "video_herf": "{video_href}"''' + '},'
        bdjs = f"{bdjs}{str(button_data)}"
    bdjs = bdjs + '];'
    bdjs = str(bdjs)
    with open('./buttonsData.js', 'w+', encoding='utf-8') as f:
        f.write(bdjs)
        f.close()
