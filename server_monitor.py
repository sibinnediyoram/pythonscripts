# Server monitoring script to check CPU load average and to send mail with memory statistics, disk space details, and server load
# at the time of reaching the threshold value
#Written by : Sibin John
#Date: November 26th, 2018
import psutil
from os import popen

def memory_stat():
    """ We can get the memory status details using free -t -m , command with popen module """
    total_Memory, used_Memory, free_Memory = map(int, popen('free -t -m').readlines()[-1].split()[1:])
    return 'Total Memory = ' + str(total_Memory) + ' MB\n'+'Used Memory = ' + str(used_Memory) + ' MB\n'+'Free Memory = ' + str(free_Memory) + ' MB'

def getDiskSpace():
    p = popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

disk_Stat = getDiskSpace()
disk_Total, disk_Used, disk_Free = disk_Stat[0], disk_Stat[1], disk_Stat[2]
current_diskusage = 'Total Disk Space= ' + str(disk_Total) + '\n' + 'Free Disk Space available= ' + str(disk_Free) +'\n' + 'Total Disk Space Used= ' + str(disk_Used)

def system_busy():
    """
    :param float threshold: relative threshold (load_1min/num_cpus) past which the system is considered busy
    :return: True if the system is considered busy; False otherwise
    :rtype: bool
    """
    from psutil import cpu_count
    from os import getloadavg
    import smtplib
    from socket import gethostname
    import platform
    import string
    server = smtplib.SMTP('smtp.gmail.com', 587)
    threshold = float(0.2)
    load_1, load_5, load_15 = getloadavg()
    server_Loadaverage = str(getloadavg())
    if load_1 / psutil.cpu_count() >= threshold:
        OS_VERSION = platform.linux_distribution()[0] + ' ' + platform.linux_distribution()[1]
        HOST_NAME = gethostname()
        OS_ARCH = platform.architecture()[0]
        FROM = "demomail@gmail.com"
        MY_PASSWORD = "demopassword"
        TO = "sibin.j@hostdime.in"
        SUBJECT = "server cpu overloaded"
        print "server is having high cpu load"
        # Next, log in to the mail server

        # Send the mail
        TEXT = HOST_NAME + OS_VERSION + OS_ARCH + '\n' + "cpu overloaded" + '\n' + "Current load is: " + '\n' + server_Loadaverage + '\n' + "memory status is: "+ '\n' + memory_stat() + '\n' + "Disk status is: " + '\n' + current_diskusage
        message = """\
        From: %s  
     
        Subject: %s
        
        %s
        """ % (FROM, SUBJECT, TEXT)
        try:
            server.ehlo()
            server.starttls()
            server.login(FROM, MY_PASSWORD)
            server.sendmail(FROM, TO, message)
            server.close()
        except:
            print 'Mail sending failed...'
    else:
        print "your server cpu load is normal"

# Check server load and other stats now
system_busy()






