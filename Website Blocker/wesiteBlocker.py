import platform
from datetime import datetime ,timedelta

os_name = platform.system()

current = datetime.now()
sites = ["youtube.com","www.youtube.com","facebook.com","www.facebook.com","reddit.com"]
#amount of time for the website to be blocked
# if you want to change amount of blocked time change value here (in Hours)

time = int(input("Enter the number of hours for the sites to be blocked: "))

end = current + timedelta(hours=time) #time till the websites will be blocked


if os_name == "Linux" or os_name == "Darwin":
    hostfile_path = "/etc/hosts"
elif os_name == "Windows":
    hostfile_path = "C:/Windows/System32/drivers/etc/hosts"


local = "127.0.0.1"

def block():
    if current < end:
        print("Blocked sites")
        with open(hostfile_path,'r+') as hostfile:
            file_content = hostfile.read()
            for site in sites:
                if site not in file_content:
                    hostfile.write(local+" "+site+"\n")
        return True

    elif end == current:
        return False

    else:
        print("sites unblocked")
        with open(hostfile_path,'r+') as hostfile:
            lines = hostfile.readline
            hostfile.seek(0)
            for line in lines:
                if  not any(site in line for site in sites):
                    hostfile.write(line)
                hostfile.truncate()

            return False

    
if __name__ == "__main__":

    while(block()):
        pass

