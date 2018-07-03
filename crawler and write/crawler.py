

import urllib.request as request
import json
src="http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as response:
    data=json.load(response)
    #.decode("utf-8")
clist=data["result"]["results"]
with open("company.txt","w",encoding='utf-8') as file:
    for a in clist:
        comid = int(a["_id"])
        comss = a["﻿統編"]
        comname = a["公司名稱"]
        comadd = a["公司地址"]
        file.write("NO.%.4d" % (comid) +" "+ str(comss) +" "+ str(comname) +" "+ str(comadd) + "%\n")

