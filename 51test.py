import requests
from requests.exceptions import HTTPError
import re

def GetHTML(url,path):       
    try:
        res=requests.get(url)
        res.raise_for_status()
        coding=res.encoding
        with open(path,"w+",encoding=coding) as MyFile:
            MyFile.write(res.text)       
    except HTTPError:
            print("HTTP Error!")       
    except ConnectionError:
        print("Failed to connect!")
        
def DataWash(path):
    mid=[]
    final=[]   
    with open(path,"r",encoding="gbk") as ReadFile: 
        MyLines=ReadFile.readlines()       
        for ML in MyLines:
            if re.search("<p>.+?</p>",ML)!=None:
                mid.append(ML)
        for i in mid:
            i=re.sub("<br>","\n",i)
            i=re.sub("</p>","\n",i)
                      
            i=re.sub("<.+?>"," ",i)           
            final.append(i)
        return final
    
def SaveFile(final,path):
    with open(path,"w+",encoding="gbk") as FinalFile:
            for i in final:               
                if len(i)!=0:
                    FinalFile.write(i)
                    

if __name__=='__main__':
    print("Welcome!\nAll the codes and .exe files are copyright to wuming")
    print("Do not use for commercial purposes!")
    url=input('input url of 51test:')
    path=input('input save path:')
    
    GetHTML(url,path)
    final=DataWash(path)
    SaveFile(final,path)
    print('Done')
