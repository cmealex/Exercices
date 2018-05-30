import urllib.request as ur
import random

def download_img(url):
    file_name = str(random.randint(1, 100)) + ".jpg"
    ur.urlretrieve(url, file_name)

download_img("https://scontent.fotp3-2.fna.fbcdn.net/v/t1.0-9/28166604_10156047898907394_4828199847361573664_n.jpg?_nc_cat=0&oh=2297284a01458775db228993b88dd6d3&oe=5B93FEBA")