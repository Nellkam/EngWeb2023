import os
import re
from templates import *

PATTERN = r'.*"(.+)": (?:"(.+)"|(\d+))'
CITY_PATH = "./pages/id.html"

def cityIndex(city:dict[str,str]) -> str:
    s = TEMPLATE_INDEX_CITY
    s = re.sub("cod",city["id"],s,count=1)
    s = re.sub("nome",city["nome"],s,count=1)
    return s

def writeCity(path:str,city:dict[str,str]):
    s = TEMPLATE_CITY_PAGE
    for k,v in city.items():
        s = re.sub(k,v,s,count=2 if k=="nome" else 1)
    with open(path,"w") as fp:
        fp.writelines(s)

def readJson(path:str) -> str:
    index = ""
    with open(path,"r") as fp:
        city = {}
        for line in fp:
            match = re.match(PATTERN,line)
            if match is not None:
                g2 = match.group(2)
                city[match.group(1)] = match.group(3) if g2 is None else g2
            if len(city) == 5:
                writeCity(re.sub("id",city["id"],CITY_PATH),city)
                index = index + cityIndex(city) + "\n"
                city = {}
    return index

def main():
    try:
        os.mkdir("./pages")
        os.mkdir("./pages")
    except FileExistsError:
        index = readJson("./mapa.json")
        page = TEMPLATE_INDEX
        page = re.sub("inserir_indice",index,page,count=1)
        with open("./pages/index.html","w") as fp:
            fp.writelines(page)

main()
