import webbrowser
import time
i=0
print "This program started at " + time.ctime()
while i<3:
    #make the program wait for certain time
    time.sleep(10)

    #Getting the program to open the URL to our favorite song!
    webbrowser.open("https://youtu.be/Sv6dMFF_yts?list=RDMMSv6dMFF_yts", new=0, autoraise=True)
    i=i+1
