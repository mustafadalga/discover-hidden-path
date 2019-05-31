#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
from optparse import OptionParser
from termcolor import colored


class Path():
    def __init__(self):
        self.about()
        self.script_desc()
        self.hiddenpath=0

    def arguman_al(self):
        parse = OptionParser(description=self.description,epilog=self.kullanim,prog=self.program)
        parse.add_option("-u", "--url", dest="url", help="Hedef url")
        (options, arguments) = parse.parse_args()
        if not options.url:
            parse.error("[-] Lutfen bir url belirtin,daha fazla bilgi icin --help kullanın.")
        return options

    def request(self,url):
        try:
            if "http://" in url   or "https://" in url:
                return requests.get(url)
            else:
                return requests.get("http://"+url)
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.InvalidURL:
            pass
        except UnicodeError:
            pass



    def discover(self,url):
        print(colored('[+] Hedef Domain:'+url, 'green'))
        with open("paths.txt","r") as pathlist:
            for line in pathlist:
                word=line.strip()
                target_url=url+"/"+word
                response=self.request(target_url)
                if response:
                    self.hiddenpath+=1
                    print(colored("[+] Url Keşfedildi --> ","blue")+target_url)

    def result_count(self):
        print(colored("[+] Toplamda "+ str(self.hiddenpath)+" tane adres bulundu","green"));


    def script_desc(self):
        self.program = "discoverHiddenPath"
        self.kullanim = """Ornek Kullanim1: python discoverHiddenPath.py --url 10.0.2.6/mutillidae/
        \n\n\n\n\n 
        Ornek Kullanim2: python discoverHiddenPath.py --u 10.0.2.6/mutillidae/"""
        if sys.version_info[0] >= 3:
            self.description = "Hedef url adresindeki gizli yolları bulmanıza yarayan bir python scripti"
        else:
            self.description =unicode( "Hedef url adresindeki gizli yolları bulmanıza yarayan bir python scripti", "utf8")
            self.kullanim = unicode(self.kullanim, "utf8")


    def about(self):
        print(colored(" ____  _                               ____       _   _     ", "green"))
        print(colored("|  _ \(_)___  ___ _____   _____ _ __  |  _ \ __ _| |_| |__  ", "green"))
        print(colored("| | | | / __|/ __/ _ \ \ / / _ \ '__| | |_) / _` | __| '_ \ ", "green"))
        print(colored("| |_| | \__ \ (_| (_) \ V /  __/ |    |  __/ (_| | |_| | | |", "green"))
        print(colored("|____/|_|___/\___\___/ \_/ \___|_|    |_|   \__,_|\__|_| |_|", "green"))
        print(colored("# author      :","green")+"Mustafa Dalga")
        print(colored("# linkedin    :","green")+"https://www.linkedin.com/in/mustafadalga")
        print(colored("# github      :","green")+"https://github.com/mustafadalga")
        print(colored("# title       :","green")+"discoverHiddenPath.py")
        print(colored("# description :","green")+"Hedef url adresindeki gizli yolları bulmanıza yarayan bir python scripti")
        print(colored("# date        :","green")+"30.05.2019")
        print(colored("# version     :","green")+"1.0")
        print("#==============================================================================")


    def keyboardinterrupt_message(self):
        print("[-] CTRL+C basıldı. Uygulamadan çıkılıyor...")
        print("[-] Uygulamadan çıkış yapıldı!")

try:
    path=Path()
    options=path.arguman_al()
    path.discover(options.url)
    path.result_count()
except KeyboardInterrupt:
    path.keyboardinterrupt_message()