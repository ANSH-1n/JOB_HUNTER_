import requests 
from bs4 import BeautifulSoup 
import time

known_skills = input("Enter your skills in a comma separated way:")
known_skills.split(",")

def scrap_jobs():
    #fetch the html content of the web page : used(requests-library)
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python+developer&txtLocation=").text
    #print(html_text)


    #scrap the data to fetch the results : used(beautiful--library)
    soup =  BeautifulSoup(html_text,"lxml")
    #print(soup.prettify())  #prettify() is used to get proper format



    jobs = soup.find_all("li",class_ = "clearfix job-bx wht-shd-bx")
   
    for job in jobs:
       date_posted = job.find("span",class_="sim-posted").text.replace(" ",  "").strip().split()
       skills = job.find("span", class_="srp-skills").text.replace(" ","").strip().split(",")#to get the skills list

       if 'few' in date_posted or set(known_skills) and set(skills):
        company_name = job.find("h3",class_ ="joblist-comp-name").text.replace(" ","").strip()#to get the job list
        jd = job.header.h2.a["href"]

          # print(company_name)
          # print(skills)
        print(f'''
          Company name: {company_name }
          skills name : {skills}
          date posted : {date_posted}
          job link : {jd}
          ''')
       print('________________')
         

if __name__ == "__main__":
    while True:
        scrap_jobs()
        print("waiting for 5 seconds")
        time.sleep(5)