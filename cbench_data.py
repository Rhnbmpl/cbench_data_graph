#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
o=len(sys.argv)
file=list(sys.argv)
le=[]
#print("Enter the legend names of the files in order: ")
#for q in range(1,o):
#	na=input()
#	le.append(na)

#file.append(input('Enter file1 : '))
#file.append(input('Enter file2 : '))
color=['-ro','-b*','-g+','-m^'] #Line draw format can add more if input files are more than 4
for q in range(1,o):
    F=open(file[q],'r')
    time=[]
    data=[]
    start=0.0
    for i in range(0,16):   #Extracting data from cbench output file
        y=F.readline()
        x=y.split(':',2)
        m=float(x[1])
        z=x[2].split(' ')
        temp=z[0].split(' ',1)
        t=float(temp[0])+60*m
        if i==0:
            start=t
            t=0.0
            print(start)
        else:
            t=t-start
        time.append(t)
        x=y.split(' = ')
        z=x[1].split(' ',1)
        dat=float(z[0])
        data.append(dat*1000)
    F.close()
    colo=color[q-1]         #Enter names of lines manually for now, add more if you like with extra else if statements
    #c=some string operations with the current file name eg: NOX_thr.txt====>NOX or just enter the names manually like below
    if q==1:
        c='NOX'
    elif q==2:
        c='POX'
    elif q==3:
    	c='Beacon'
    elif q==4:
    	c='OpenDaylight'

    plt.plot(time,data,colo,label=c,linewidth=4) #change line thickness by changing linewidth value
    print(data)
    print(time)
plt.legend(loc=4)				#Location for legend; 1==>top-left; 2==>top-right; 3==>bot-right; 4==>bot-right
plt.title('Latency of NOX vs POX vs Beacon vs Opendaylight')#Title
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlabel('Time(seconds)')     #X-Axis Label
plt.ylabel('Flows per second')  #Y-Axis label
plt.show()
