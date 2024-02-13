# Algorithm for determining the torrents with the best ratio from a list of torrents

# go through a list of divs of class torrentrow
# if inside the 2nd div, inside span, inside img attributes there is an alt="FreeLeech" then
# the value from the 9th div is stored inside a span tag, inside a b tag, inside a font tag, store it as an int as a variable SEEDERS
# the value from the 10th div is stored inside a span tag, inside a b tag, store it as an int as a variable LEECHERS
# divide the SEEDERS by the LEECHERS and store the result in a variable RATIO of type float
# if RATIO is greater than 4
# retrieve the name of the torrent (inside the 2nd div, inside span, inside span, inside the tag of a link) and the link to the torrent (inside the 2nd div, inside span, inside span, inside the href propery of the link)
# and store the name, link and ratio in a list then write the list to a file, sorted in decreasing order by ratio

# import libraries
# if you don't have them installed, run the following commands in the terminal:
# pip install beautifulsoup4
# pip install datetime
from bs4 import BeautifulSoup
from datetime import datetime

## edit html_content.html with the content from the torrent list you want to parse
# import all the content from html_content.html
html_content = open("filelist.html", "r")

file = open("results.txt", "w")
#clear the file
file.write("")

soup = BeautifulSoup(html_content, "html.parser")

torrents = soup.find_all("div", class_="torrentrow")

good_torrents = []

for torrent in torrents:
     #check if the torrent has any img tags inside the 2nd div
     if torrent.find_all("div")[1].find("span").find_all("img"):
            list_of_img = torrent.find_all("div")[1].find("span").find_all("img")
            is_freeleech = False
            is_2x_upload = False
            #check if the torrent is freeleech
            for img in list_of_img:
                if img["alt"] == "FreeLeech":
                    is_freeleech = True
                if img["alt"] == "DoubleUp":
                    is_2x_upload = True
            if is_freeleech:
                seeders = int(torrent.find_all("div")[8].find("span").find("b").text)
                leechers = int(torrent.find_all("div")[9].find("span").text)
                ratio = leechers / seeders
                if is_2x_upload:
                    ratio = ratio * 2
                #modify minimum ratio or leecheers
                if ratio >= 0.20 and leechers > 44:
                    name = torrent.find_all("div")[1].find("span").find("span").find("a").text
                    link = torrent.find_all("div")[1].find("span").find("span").find("a")["href"]
                    size = torrent.find_all("div")[6].find("span").find("font").text

                    if is_2x_upload:
                        name = "!2x upload! " + name + " actual ratio = ratio / 2"

                    good_torrents.append([name, link, round(ratio, 2), leechers, size])

# sort the list in decresing order by ratio
good_torrents.sort(key=lambda x: x[2], reverse=True)

#write in file the current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
file.write("Last modified: " + dt_string + "\n\n")

#write name, ratio and link in the file
for torrent in good_torrents:
    file.write("Name: " + torrent[0] + "\n")
    file.write("Ratio: " + str(torrent[2]) + "\n")
    file.write("Leechers: " + str(torrent[3]) + "\n")
    file.write("Size: " + torrent[4] + "\n")
    file.write("filelist.io/"+ torrent[1] + "\n\n")

file.close()
print("Done!")