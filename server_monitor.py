import psutil
from os import popen
def is_system_busy():
    """
    :param float threshold: relative threshold (load_15min/num_cpus) past which the system is considered busy
    :return: True if the system is considered busy; False otherwise
    :rtype: bool
    """
    from psutil import cpu_count
    from os import getloadavg
    threshold = 2
    load_1, load_5, load_15 = getloadavg()
    server_Loadaverage = str(getloadavg())
    if load_15 / psutil.cpu_count() >= threshold:
        print "server is having high cpu load"
    else:
        print "your server cpu load is normal"
    return server_Loadaverage

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
print is_system_busy()
print memory_stat()
print 'Total Disk Space= ' + str(disk_Total) + '\n' + 'Free Disk Space available= ' + str(disk_Free) +'\n' + 'Total Disk Space USed= ' + str(disk_Used)





