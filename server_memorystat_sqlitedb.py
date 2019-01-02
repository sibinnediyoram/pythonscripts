# A simple python script to update memory statistics in Linux machine to a sqlite3 DB
# Written by Sibin John
# Date: 25th July 2018
#!/usr/local/bin/python
import distro
import os
import time
import sqlite3
import re
memfile = "/home/sibin/python-projects/memstat"
db = sqlite3.connect('/home/sibin/python-projects/data.db')
os_version = distro.linux_distribution()
def mem_info():
  with open("/proc/meminfo", "r") as f:
    lines = f.readlines()
    line1 = lines[0].strip()
    line2 = lines[1].strip()
    line3 = lines[3].strip()
    line4 = lines[14].strip()
    line5 = lines[15].strip()
    line = ("%s \n %s \n %s \n %s \n %s \n %s \n" % (os_version,line1,line2,line3,line4,line5))
    result1 = re.sub('[^0-9]','',line1)
    result2 = re.sub('[^0-9]','',line2)
    result3 = re.sub('[^0-9]','',line3)
    result4 = re.sub('[^0-9]','',line4)
    result5 = re.sub('[^0-9]','',line5)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS memoryinfo(id INTEGER PRIMARY KEY,MemTotal TEXT, MemFree TEXT,
    Buffers TEXT, SwapTotal TEXT,SwapFree TEXT)''')
    for i in line:
      cursor.execute('''INSERT INTO memoryinfo(MemTotal, MemFree, Buffers, SwapTotal, SwapFree)
      VALUES(?,?,?,?,?)''', (result1, result2, result3, result4, result5))
      db.commit()
  return mem_info
while True:
  mem_info()
  time.sleep(3)
