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
kfmul = len(kw)*len(formats)
for keyword in kw:
    for fformat in formats:
        done += 1
        print(f"{done}/{kfmul} done.")
        reqcode = requests.get(link.replace("FNAMELINK",keyword).replace("FFORMAT",fformat))
        if reqcode.ok:
            print(link.replace("FNAMELINK",keyword).replace("FFORMAT",fformat), f"{reqcode}")
print("DONE!")