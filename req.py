import requests


start_url = open("/home/egorliovkin/Downloads/dataset_3378_3.txt").readline().strip()
text_xs = requests.get(start_url).content.splitlines()
print(len(text_xs))