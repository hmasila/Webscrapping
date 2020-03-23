from bs4 import BeautifulSoup
import mechanize
import csv

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

url = 'https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p433'
page = br.open(url)

with open('comments.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    while True:
        print(url)
        page = br.open(url)
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

        try:
            url = br.follow_link(text_regex=r"»").geturl()
        except:
            print("this is the last page")
            break
