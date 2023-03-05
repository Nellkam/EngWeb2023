import re
from templates import *

PATTERN = r'.*"(.+)": (?:"(.+)"|(\d+))' 

def cityToHtml(city:dict[str,str]) -> str:
    s = TEMPLATE_CITY
    for k,v in city.items():
        s = re.sub(k,v,s,count=1)
    return s

def cityIndex(city:dict[str,str]) -> str:
    s = TEMPLATE_INDEX_CITY
    s = re.sub("cod",city["id"],s,count=1)
    s = re.sub("nome",city["nome"],s,count=1)
    return s

def readJson(path:str) -> tuple[str,str]:
    content = ""
    index = ""
    with open(path,"r") as fp:
        city = {}
        for line in fp:
            match = re.match(PATTERN,line)
            if match is not None:
                g2 = match.group(2)
                city[match.group(1)] = match.group(3) if g2 is None else g2
            if len(city) == 5:
                content = content + cityToHtml(city) + "\n"
                index = index + cityIndex(city) + "\n"
                city = {}
    return (index,content)

def main():
    index,content = readJson("./mapa.json")
    page = TEMPLATE_PAGE
    page = re.sub("inserir_index",index,page,count=1)
    page = re.sub("inserir_conteudo",content,page,count=1)
    with open("index.html","w") as fp:
        fp.writelines(page)

main()
