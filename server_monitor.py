import psutil
from os import popen
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
    import string
    server = smtplib.SMTP('smtp.gmail.com', 587)
    threshold = float(0.2)
    load_1, load_5, load_15 = getloadavg()
    server_Loadaverage = str(getloadavg())
    if load_1 / psutil.cpu_count() >= threshold:
        HOST_NAME = gethostname()
        FROM = "hostdimetestmail@gmail.com"
        MY_PASSWORD = "Test@123456"
        TO = "sibin.j@hostdime.in"
        SUBJECT = "server cpu overloaded"
        print "server is having high cpu load"
        # Next, log in to the mail server

        # Send the mail
        TEXT = HOST_NAME + '\n' + "cpu overloaded" + '\n' + "Current load is: " + '\n' + server_Loadaverage + '\n' + "memory status is: "+ '\n' + memory_stat() + '\n' + "Disk status is: " + '\n' + current_diskusage
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

#    return server_Loadaverage

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
system_busy()






