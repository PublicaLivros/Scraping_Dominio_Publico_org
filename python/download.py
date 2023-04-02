import requests
import json
import os

with open("../json/raw_data.json") as dataRaw:
    data = json.load(dataRaw)

def verifyDirsExist():
    if not os.path.exists('dist'): os.makedirs('dist')

def requestPdf(url, name, id):
    url = f'{url}&co_midia=2'
    response = requests.get(url)
    try:
        with open(f'./dist/{name}_{id}.pdf', 'wb') as f:
            f.write(response.content)
        print(f'\033[1;32mBook saved:\033[1;m {name}. \33[1;32mID:\33[1;m {id}')
    except:
        print(f'Unable to save book: {name}, ID: {id}')

def tryDownload(index):
    try:
        requestPdf(data[index]["link"].replace("DetalheObraForm.do", "DetalheObraDownload.do", 1), data[index]["titulo"], index)
    except:
        print(f'Unable do download book: {data[index]["titulo"]}')

def init():
    verifyDirsExist()
    for i in range(0, 2): tryDownload(i)

init()



