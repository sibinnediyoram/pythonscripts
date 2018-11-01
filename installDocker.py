import subprocess
import os

def install_docker():
    os.system('yum -y install yum-utils device-mapper-persistent-data lvm2')
    subprocess.call('yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && yum install docker-ce', shell = true)
    subprocess.call('systemctl start docker && systemctl enable docker', shell = true)
    dockerVersion = str(docker -v)
    return dockerVersion

if __name__=='__main__':
    install_docker()


