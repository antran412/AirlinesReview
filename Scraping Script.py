from requests_html import HTMLSession
import csv, json

session = HTMLSession()
url = "https://www.airlinequality.com/airline-reviews/british-airways"
resp = session.get(url)
master = {}
reviewpages = resp.html.xpath("//div[@class='col-content']/div/article/ul")[0].text
total_pages = int(reviewpages[-7:-3])

for i in range(1, total_pages+1):
    url = f"https://www.airlinequality.com/airline-reviews/british-airways/page/{i}"
    resp = session.get(url)
    reviewElements = resp.html.xpath("//div[@class='col-content']/article/article")

    for review in reviewElements:
      reviews ={}
      #Get overall rating
      try:
        reviewRating = review.xpath("//div[@class ='rating-10']/span[1]")
        rating = reviewRating[0].text
      except:
        rating = ''
      reviews['Overall Rating'] = rating
      #Get header
      reviewHeader = review.xpath("//div[@class = 'body']/h2")
      header = reviewHeader[0].text
      reviews['Title'] = header
      #Get Country
      countryT=review.xpath("//div[@class = 'body']/h3")
      country = countryT[0].text
      #will print in fomat name (country) date published, so we can find the country by choosing only words in bracket

      #Get time published
      datePublished=review.xpath("//div[@class = 'body']/h3/time[@itemprop = 'datePublished']")
      date = datePublished[0].text
      reviews['Date Published'] = date
      #Get text review
      textReview = review.xpath("//div[@class='body']/div[@class = 'tc_mobile']/div[@class='text_content']")
      text = textReview[0].text #need to text to see if it is actually 1 indexed
      reviews['Text Review'] = text
      #Get other stats
      statsItem = review.xpath("//tr")
      stats = {}
      for item in statsItem:

        if item.xpath('.//td[2]/span[@class="star fill"]'):
          itemHeader = item.xpath('.//td[1]')[0].text
          itemContent = item.xpath('.//td[2]/span[@class="star fill"]')[-1].text

        else:
          itemHeader = item.xpath('.//td[1]')[0].text
          itemContent = item.xpath('.//td[2]')[0].text
        stats[itemHeader] = itemContent

        reviews['Review Rating'] = stats
      master[country] = reviews

#Create json file
data_json = open('bareview.txt', 'w+')
json.dump(master, data_json, indent = 4)
data_json.close()

#Create csv file for further analysis
data_csv = open('bareview.csv', 'w', newline = '')
writer = csv.writer(f, delimiter = ',')
header = ['Country', 'Overall Rating', 'Title', 'Date Published', 'Text Review', 'Type of Traveller', 'Seat Type', 'Route', 'Aircraft', 'Date Flown', 'Seat Comfort', 'Cabin Staff Service', 'Food & Beverages',
                  'Inflight Entertainment', 'Ground Service', 'Wifi & Connectivity', 'Value For Money', 'Recommended']
rating = ['Type of Traveller', 'Seat Type', 'Route', 'Aircraft', 'Date Flown', 'Seat Comfort', 'Cabin Staff Service', 'Food & Beverages',
                  'Inflight Entertainment', 'Ground Service', 'Wifi & Connectivity', 'Value For Money', 'Recommended']
writer.writerow(header)
for key, elem in master.items():
  row = [key, elem['Overall Rating'], elem['Title'], elem['Date Published'], elem['Text Review']]
  for i in rating:
    if i in elem['Review Rating']:
      row.append(elem['Review Rating'][i])
    else:
      row.append('')
  writer.writerow(row)
data_csv.close()

