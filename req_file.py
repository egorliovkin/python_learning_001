import requests
import time

start_url = "https://stepik.org/media/attachments/course67/3.6.3/"
start_fname = open("/home/egorliovkin/Downloads/dataset_3378_3.txt").readline().strip()

r = requests.get(start_fname)
while r.status_code != 200:
    r = requests.get(start_fname)
line = r.content.decode('utf-8').strip()
print(start_url+line)

count = 0
while line[:2] != "We":
    r = requests.get(start_url+line)
    while r.status_code != 200:
        count += 1
        if count < 10:
            r = requests.get(start_url+line)
        else:
            raise NameError(start_url+line+str(r.status_code))
    count = 0
    line = r.content.decode('utf-8').strip()
    print(line)
    # time.sleep(1)
    