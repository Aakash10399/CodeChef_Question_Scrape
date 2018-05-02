import urllib2
import requests
from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://www.codechef.com/contests'
driver.get(url)
codechef_main = str(driver.page_source.encode("utf-8"))
codechef_main = codechef_main[codechef_main.find("Past Contests"):]
f = open('data/codechef_contests.html','w')
f.write(codechef_main)
f.close
##################

##################
contests = []
marker = '<tr>'
contests_code = open('data/codechef_contests.html','r') 
contests_code2 = str(contests_code.read())
contests_code2 = contests_code2[contests_code2.find("<tbody>"):contests_code2.find("</tbody>")]
while marker in contests_code2:
	contests_code2 = contests_code2[contests_code2.find(marker):]
	contests_code2 = contests_code2[contests_code2.find("<td>")+4:]
	contests.append(str(contests_code2[:contests_code2.find("</td>")]))
for element in contests:
	page = requests.get("https://www.codechef.com/"+str(element)).text
	page = page[page.find('problemname'):]
	page = page[:page.find('</table>')]
	qcodes = []
	print "curr-->"+str(element)
	marker2 = "flexbox"
	for marker2 in page:
		page = page[page.find("flexbox"):]
		page = page[page.find("<td"):]
		page = page[page.find(">")+1:]
		if str(page[:page.find("</td")])=='':
			break
		qcodes.append(str(page[:page.find("</td")]))
	for element2 in qcodes:
		page2 = requests.get("https://www.codechef.com/"+str(element)+'/problems/'+str(element2)+'/').text
		#print str("https://www.codechef.com/"+str(element)+'problems/'+str(element2)+'/')
		page2 = page2[page2.find("All Submissions"):]
		page2 = page2[page2.find("content")+9:page2.find("Languages:")]
		fname = 'data/'+str(element)+'-'+str(element2)+'.html'
		fname.replace(' ','-')
		fname.replace('/','-')
		f = open(fname,'w')
		f.write(page2.encode("utf-8"))
		f.close

