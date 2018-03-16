import urllib3
import re
import dryscrape
from bs4 import BeautifulSoup
from time import sleep
baseurl = "http://jobs.philips.com/jobs/#12"
# baseurl = "https://www.amazon.jobs/en/locations/"
# qurl = "?base_query=&loc_query=&job_count=100&result_limit=100&sort=relevant&cache"
# https://www.amazon.jobs/en/locations/aachen-germany?base_query=&loc_query=&job_count=100&result_limit=100&sort=relevant&
# location = ["castel-san-giovanni-italy","changchun","charleston-sc",
#             "charlotte-northcarolina","chattanooga-area-tn","bangalore-india"]
qurl = ""
location = [""]
f = open('workfile.csv', 'w')
f.write("link,job title,location,team,BASIC QUALIFICATIONS,PREFERRED QUALIFICATIONS\n")
for l in location:
    url = baseurl + l + qurl
    print(url)
    session = dryscrape.Session()
    session.set_header('user-agent', 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36')

    session.visit(url)
    sleep(2)
    response = session.body()
    # print(response)
    soup = BeautifulSoup(response ,"lxml")
    i = 0
    for link in soup.find_all(href=re.compile("job")):
        i = i + 1
        print(str(i), "http://jobs.philips.com" + link['href'])
        # csvline = ""
        # s2 = dryscrape.Session()
        # s2.set_timeout(30)
        # s2.set_header('user-agent', 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36')
        # u =  "https://www.amazon.jobs" + link['href']
        # try:
        #     s2.visit(u)
        # except TimeoutError:
        #     print("TimeoutError")
        #     continue
        # except:
        #     continue
        # r = s2.body()
        # sp = BeautifulSoup(r ,"lxml")
        # csvline += u + ","                                                                  # link
        # jt = sp.find('h1', attrs = {'class' : 'title'})
        # if jt:
        #     csvline += jt.text.replace(",","-") + ","                        #job title
        # else:
        #     csvline += ","
        # loc = sp.find('div', attrs = {'class' : 'association location-icon'})
        # if loc:
        #     csvline += loc.text.replace(",","-") + ","   # location
        # else:
        #     csvline += ","
        # ti = sp.find('div', attrs = {'class' : 'team-icon'})
        # if ti:
        #     csvline += ti.text.replace(",","-") + ","
        # else:
        #     csvline += ","                   # team
        #
        # # csvline += sp.find('p', text = re.compile('Job details')).parent
        # bq = sp.find('h3', text = re.compile('BASIC QUALIFICATIONS'))
        # if bq:
        #     csvline += bq.next_sibling.text.replace(",","-") + ","
        # else:
        #     csvline += ","
        # pq = sp.find('h3', text = re.compile('PREFERRED QUALIFICATIONS'))
        # if pq:
        #     csvline += pq.next_sibling.text.replace(",","-") + "\n"
        # else:
        #     csvline += "\n"
        #
        # f.write(csvline)

    sleep(20)

# ","aachen-germany
