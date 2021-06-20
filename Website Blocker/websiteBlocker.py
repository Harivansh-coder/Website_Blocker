# The following code is for linux/mac

from datetime import datetime ,timedelta

current = datetime.now()

#amount of time for the website to be blocked
time = 1 # if you want to change amount of blocked time change value here (in Hours)

end = current + timedelta(hours=time) #time till the websites will be blocked

sites = ["www.youtube.com","youtube.com","www.twiter.com","www.facebook.com"]

hostfile_path = "/etc/hosts"


local = "127.0.0.1"

def block():
    if current < end:
        print("Sites Blocked")
        with open(hostfile_path,'r+') as hostfile:
            file_content = hostfile.read()
            for site in sites:
                if site not in file_content:
                    hostfile.write(local+" "+site+"\n")
    else:
        print("Sites Unblocked")
        with open(hostfile_path,'r+') as hostfile:
            lines = hostfile.readline
            hostfile.seek(0)
            for line in lines:
                if  not any(site in line for site in sites):
                    hostfile.write(line)
            hostfile.truncate()

if __name__ == "__main__":
    block()

