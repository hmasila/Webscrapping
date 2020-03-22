from bs4 import BeautifulSoup
import mechanize
import csv

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

links = []
edmunds_forum = 'https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans'
links.append(edmunds_forum)

for i in range(2,301):
    links.append(edmunds_forum+'/p'+str(i))

with open('comments.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)

    for pg in links:
        print(pg)
        page = br.open(pg)
        soup = BeautifulSoup(page.read(),'html.parser')
        table = soup.find('ul', attrs={'class': 'MessageList DataList Comments'})

        for row in table.find_all('li'):
            date_box = row.find_next('a', attrs={'class': 'Permalink'})
            date = date_box.text.strip()


            userid_box = row.find_next('a', attrs={'class': 'Username'})
            userid = userid_box.text.strip()

            message_box = row.find_next('div', attrs={'class': 'Message'})
            message = message_box.text.strip()

            writer.writerow([date, userid, message])    

