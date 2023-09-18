import os
import requests
import urllib.request
from bs4 import BeautifulSoup
import sys
#https://www.nos.nl/l/t/2372980




loop = "loop"
f = open("id.txt", "r")
idstr = f.read()

fatal_count = 0

id = int(idstr)
id += 1
print("loading loop")
while loop == "loop":
    
    result = requests.get('https://www.nos.nl/l/t/'+str(id))
    code = result.status_code

    if fatal_count > 3:
        f = open("error_log.txt", "a")
        f.write(id)
        f.write(code)
        f.close()
        sys.exit("error log done")






    elif code == 404:
        print("404")
        id += 1
        fatal_count = 0

    elif code == 200:
        


        page = urllib.request.urlopen('https://www.nos.nl/l/t/'+str(id))
        html = BeautifulSoup(page.read(), "html.parser")




        L = html.title.string
 

        file1 = open('myfile.txt', 'w')
        file1.writelines(L)
        file1.close()
 

        file1 = open('myfile.txt', 'r')
        Lines = file1.readlines()
    
        count = 0

        for line in Lines:
            count += 1
            if count == 2:
                f = open("id.txt", "w")
                f.write(str(id))
                f.close()
                title_link = ('https://www.nos.nl/l/t/'+str(id)+"  "+line.strip())
                f = open("lijst.txt", "a")
                f.write("\n")
                f.write(title_link)
                f.close()
                
                print(title_link)
                id += 1
                fatal_count = 0
                
    elif code == 410:
        error_link = ('https://www.nos.nl/l/t/'+str(id)+("  verwijderd artikel"))
        print (error_link)
        f = open("lijst.txt", "a")
        f.write("\n")
        f.write(error_link)
        f.close()
        id += 1
        fatal_count = 0
    
    elif code == 500:
        fatal_count += 1
        print("fatal error: debug info:")
        print(str(code))
        print(str(id))
        f = open("error.txt", "w")
        f.write(str(id))
        f.write(str(code))
        f.write("500 elif error")
        f.close()
        id += 1
    
    
    
    else:
        fatal_count += 1
        print("fatal error: debug info:")
        print(str(code))
        print(str(id))
        f = open("error.txt", "w")
        f.write(str(id))
        f.write(str(code))
        f.close()
        id += 1





#if a == ("404"):
#    print("error")
    
#else:
#    print("good")



input("aafdfsfsad")
