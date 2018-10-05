
import requests
from bs4 import BeautifulSoup
import month
from datetime import datetime
import calendar


def get_html(url):
    r = requests.get(url) #Responce
    return r.text #html код


def get_image_url(reference, calendar_flag, image_type, width_x_height):
    href = reference.replace("full."+image_type, "")
    href = href + calendar_flag + "-" + width_x_height + "."+image_type
    t = href.split("/")
    t.insert(6, calendar_flag)
    h = "/".join(t)
    name = h.split('/')

    r = requests.get(h)  # create HTTP response object
    if h != None and r.status_code == 200:
        return h
    else:
        return None


def get_all_urls(html,  calendar_flag, width_x_height):
    links_to_load = []
    soup = BeautifulSoup(html, 'html.parser')

    for data in soup.find_all('figure'):
        for a in data.find_all('a'):
            if a.get('href').endswith(".png"):
                link = get_image_url(a.get('href'), calendar_flag, "png", width_x_height)
                if link != None:
                    links_to_load.append(link)
    return links_to_load

def facade(month_ = calendar.month_name[datetime.now().month].lower(), year = datetime.now().year , calendar_flag = "cal", width_x_height = "320x480"):

    if year >  datetime.now().year or (year == datetime.now().year and month.month__[month_] > datetime.now().month):
        return
    if month_ == 'january':
        url = "https://www.smashingmagazine.com/{}/12/desktop-wallpaper-calendars-{}-{}/".format( str(year-1), month_, str(year))
        return get_all_urls(get_html(url), calendar_flag, width_x_height)

    month_count = month.month[month_]
    month_index = ""
    if month_count < 10:
        month_index = "0"+str(month_count)
    else:
        month_index = str(month_count)

    url = "https://www.smashingmagazine.com/{}/{}/desktop-wallpaper-calendars-{}-{}/".format(str(year),month_index, month_, str(year))
    return get_all_urls(get_html(url), calendar_flag, width_x_height)