import json
import requests

with open("config") as cfg:
    config = json.load(cfg)
    link = config["send_config"][0]['link']
    if config["send_config"][0]['database_path'] == "":
        kw = config["send_config"][0]['keywords']
        formats = config["send_config"][0]['formats']
    else:
        with open(config["send_config"][0]['database_path'], encoding="UTF-8") as kwdb:
            kwr = kwdb.read().split("\n")
            formats = kwr[1:kwr.index("__KEYWORDS:")]
            kw = kwr[kwr.index("__KEYWORDS:")+1:]

print("WORKING...")
done = 0
lastdone = 0
for keyword in kw:
    for fformat in formats:
        done += 1
        percentage_formula = round(done/(len(kw)+len(formats)))
        if not lastdone == percentage_formula:
            print(f"{percentage_formula}% done.")
            lastdone = round(done/(len(kw)+len(formats)))
        reqcode = requests.get(link.replace("FNAMELINK",keyword).replace("FFORMAT",fformat))
        if reqcode.ok:
            print(link.replace("FNAMELINK",keyword).replace("FFORMAT",fformat), f"{reqcode}")

print("DONE!")