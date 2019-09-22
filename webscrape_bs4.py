# >pip install bs4
# >python

import bs4 #beautiful soup 4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


myurl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

#use soup to parse, the below is code for parsing
page_soup = soup(page_html, "html.parser")

#page_soup.h1
#page_soup.body

containers = page_soup.findAll("div", {"class": "item-container" })
#len(containers)
#containers[0]

### TO read HTML, go to https://beautifier.io/, and dump back to local to exam

# name the output file to write to local disk
out_filename = "graphics_cards.csv"
# header of csv file to be written
headers = "brand,product_name,shipping \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

# loops over each product and grabs attributes about
# each product
for container in containers:
    # Finds all link tags "a" from within the first div.
    make_rating_sp = container.div.select("a")

    # Grabs the title from the image title attribute
    # Then does proper casing using .title()
    brand = make_rating_sp[0].img["title"].title()

    # Grabs the text within the second "(a)" tag from within
    # the list of queries.
    product_name = container.div.select("a")[2].text

    # Grabs the product shipping information by searching
    # all lists with the class "price-ship".
    # Then cleans the text of white space with strip()
    # Cleans the strip of "Shipping $" if it exists to just get number
    shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    # prints the dataset to console
    print("brand: " + brand + "\n")
    print("product_name: " + product_name + "\n")
    print("shipping: " + shipping + "\n")

    # writes the dataset to file
    f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")

f.close()  # Close the file
