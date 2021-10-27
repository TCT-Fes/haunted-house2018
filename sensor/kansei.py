#coding utf-8
import serial
import re
import subprocess
def main():
   with serial.Serial('/dev/ttyACM0',9600,timeout=1) as ser:

        while (True):
            c = ser.readline()
            d = re.findall('[0-9]+\.+[0-9]',str(c),flags=0)
            d = [float(i) for i in d]
            for i in range(0, len(d)): 
                if(d[i]>0):
                    if(d[i]<10):
                        subprocess.Popen("vlc -I rc --play-and-stop 04.mp3", shell=True)
                        break 
            else:
                continue
            break

if __name__=="__main__":
    main()   