import urllib3
import re
import dryscrape
from bs4 import BeautifulSoup
from time import sleep
# baseurl = "http://jobs.philips.com/jobs/#12"
# baseurl = "https://www.amazon.jobs/en/locations/"
# qurl = "?base_query=&loc_query=&job_count=100&result_limit=100&sort=relevant&cache"
# https://www.amazon.jobs/en/locations/aachen-germany?base_query=&loc_query=&job_count=100&result_limit=100&sort=relevant&
# location = ["castel-san-giovanni-italy","changchun","charleston-sc",
# #             "charlotte-northcarolina","chattanooga-area-tn","bangalore-india"]
# qurl = ""
# location = [""]
#
# fname = "sites.txt"
# with open(fname) as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# sites = [x.strip() for x in content]

site = "https://www.daysoftheyear.com/days/2017/"
r = ["01","02","03","04","05","06","07","08","09","10","11","12"]

f = open('worldDays.txt', 'w')

for r in range(1,13):
    url = site + (str(r) if r >= 10 else "0"+str(r))

# f.write("link,job title,location,team,BASIC QUALIFICATIONS,PREFERRED QUALIFICATIONS\n")
# for l in location:
#     url = baseurl + l + qurl
#     print(url)
    session = dryscrape.Session()
    session.set_header('user-agent', 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36')
#
    print("visit : " , url)
    try:
        session.visit(url)
        sleep(2)
        response = session.body()
    #     # print(response)
        soup = BeautifulSoup(response ,"lxml")
        i = 0
        f.write(str(i)+ url + "\n")
        for link in soup.find_all("a" , class_="dayLink"):
            i = i + 1
            print(str(i), link['href'])
            f.write(link["href"] + "\n")
        continue
    except:
        print ('Error')
        continue


#         # csvline = ""
#         # s2 = dryscrape.Session()
#         # s2.set_timeout(30)
#         # s2.set_header('user-agent', 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36')
#         # u =  "https://www.amazon.jobs" + link['href']
#         # try:
#         #     s2.visit(u)
#         # except TimeoutError:
#         #     print("TimeoutError")
#         #     continue
#         # except:
#         #     continue
#         # r = s2.body()
#         # sp = BeautifulSoup(r ,"lxml")
#         # csvline += u + ","                                                                  # link
#         # jt = sp.find('h1', attrs = {'class' : 'title'})
#         # if jt:
#         #     csvline += jt.text.replace(",","-") + ","                        #job title
#         # else:
#         #     csvline += ","
#         # loc = sp.find('div', attrs = {'class' : 'association location-icon'})
#         # if loc:
#         #     csvline += loc.text.replace(",","-") + ","   # location
#         # else:
#         #     csvline += ","
#         # ti = sp.find('div', attrs = {'class' : 'team-icon'})
#         # if ti:
#         #     csvline += ti.text.replace(",","-") + ","
#         # else:
#         #     csvline += ","                   # team
#         #
#         # # csvline += sp.find('p', text = re.compile('Job details')).parent
#         # bq = sp.find('h3', text = re.compile('BASIC QUALIFICATIONS'))
#         # if bq:
#         #     csvline += bq.next_sibling.text.replace(",","-") + ","
#         # else:
#         #     csvline += ","
#         # pq = sp.find('h3', text = re.compile('PREFERRED QUALIFICATIONS'))
#         # if pq:
#         #     csvline += pq.next_sibling.text.replace(",","-") + "\n"
#         # else:
#         #     csvline += "\n"
#         #
#         # f.write(csvline)
#
#     sleep(20)
#
# # ","aachen-germany
