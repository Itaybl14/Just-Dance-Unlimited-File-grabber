import requests

def jdurequest(link):
    headers = {"X-SkuId":skuid,"Authorization":f"Ubi_v1 {ticket}"}
    j = requests.get(link, headers=headers)
    if j.status_code != 200:
        import time
        print(f"[{j.status_code}] something went wrong while getting a request from prod.")
        time.sleep(5)
        exit()
    else:
        json = j.json()
        return json

print("\n----------\nJust Dance Unlimited tools by Itay\nCredits: Ron (todoroki)\n----------\nOptions:\n1 - Get ticket\n2 - Get SongDB\n3 - Get sku-packages\n4 - Get & Download No Huds\n----------\n")

while True:
    option = int(input("Option => "))
    if option < 5:
        break
    else:
        print("wrong option!")
        continue

while True:
    jdversion = int(input("\nJDVersion (2016-2022) => "))
    if jdversion == 2016 or 2017 or 2018 or 2019 or 2020 or 2021 or 2022:
        break
    else:
        print("wrong jdversion!")
        continue

if jdversion == 2016:
    appid = '2714264f-9d54-4810-845f-3f5c2135f965'
    skuid = 'jd2016-xone-emea'
elif jdversion == 2017:
    appid = '155d58d0-94ae-4de2-b8f9-64ed5f299545'
    skuid = 'jd2017-xone-emea'
elif jdversion == 2018:
    appid = 'ccfda907-9767-4ae5-895c-6204e7a39cbd'
    skuid = 'jd2018-xone-emea'
elif jdversion == 2019:
    appid = 'f64e368b-88c7-49e7-bc57-f3cfee43d70f'
    skuid = 'jd2019-xone-all'
elif jdversion == 2020:
    appid = '7df3c817-cde1-4bf9-9b37-ceb9d06c4b96'
    skuid = 'jd2020-xone-all'
elif jdversion == 2021:
    appid = 'f78cbbdb-72eb-47f4-af54-91618c1eecd0'
    skuid = 'jd2021-xone-all'
elif jdversion == 2022:
    appid = '594d5ecc-0c64-441b-b129-42ceafb22c81'
    skuid = 'jd2022-xone-all'

with open("token.txt") as f:
    token = f.read()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44","Authorization":token,"Ubi-AppId":appid,"Content-Type":"application/json"}
r = requests.post('https://public-ubiservices.ubi.com/v3/profiles/sessions', headers=headers)
if "ticket" in r.json():
    ticket = r.json()["ticket"]
else:
    import time
    print(f"\n[{r.status_code}] something went wrong while generating a ticket.")
    time.sleep(5)
    exit()

if option == 1:
    print("\n\n" + ticket)
elif option == 2:
    if jdversion == 2019 or 2020 or 2021 or 2022:
        songdburl = jdurequest('https://prod.just-dance.com/songdb/v2/songs')["songdbUrl"]
        print("\n----------\nSongDB URL:\n" + songdburl)
        download = input("----------\nDownload? ").lower()
        if download == "yes" or "y":
            import wget
            sdb = requests.get(songdburl)
            wget.download(f'{songdburl}', f"output/{jdversion}_songdb.json")
        else:
            pass
    else:
        songdb = str(jdurequest('https://prod.just-dance.com/songdb/v1/songs')).replace("'", '"')
        open(f"output/{jdversion}_songdb.json", "w", encoding="utf-8").write(songdb)    
elif option == 3:
    skupackages = str(jdurequest('https://prod.just-dance.com/packages/v1/sku-packages')).replace("'", '"')
    open(f"output/{jdversion}_sku-packages.json", "w", encoding="utf-8").write(skupackages)
elif option == 4:
    import os, wget
    codename = input("\nCodename (with big letters!): ")
    print("\n----------")
    nohuds1 = jdurequest(f'https://prod.just-dance.com/content-authorization/v1/maps/{codename}')
    nohuds = nohuds1["urls"]
    os.mkdir(f'output/{codename}')
    open(f"output/{codename}/{codename}.json", "w", encoding="utf-8").write(str(nohuds1).replace("'", '"'))
    for type in nohuds:
        if type.find('/'):
            filename = type.rsplit('/', 1)[1]
        print(f"\nDownloading [{filename}]")
        wget.download(nohuds[type], f'output/{codename}/{filename}')

input("\nPress Enter to continue...")    
