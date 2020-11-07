import time
from datetime import datetime as dt

host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list = ["facebook.com","www.facebook.com","instagram.com","www.instagram.com"]

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt(dt.now().year, dt.now().month, dt.now().day, 18): #used to access the current date, time and year

       with open(host_path, "r+") as file:
           content = file.read()
           for website in website_list:
               if website in content:
                   pass
               else:
                   file.write(redirect+" "+website+"\n")

       print("All the listed websites are BLOCKED for the working time.")
       break

    else:

        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()
        print("The blocked websites are UNBLOCKED.")
        break
