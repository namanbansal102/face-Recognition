import csv
from datetime import datetime
x=datetime.today()
print()

def writeAttendance(name):
    x=datetime.today()
    date=x.strftime("%d-%b-%Y")
    time=x.strftime("%I:%M:%S %p")
    print(x)
    fields=["Name","Time","Status"]
    row=[[name,time,"Present"]]
    with open(f'./attendance/{date}.csv','a',newline='') as csvfile:
        csvwriter=csv.writer(csvfile)
        if csvfile.tell()==0:
            csvwriter.writerow(fields)
        
        print(csvfile.tell())
        csvwriter.writerows(row)
    

   
   