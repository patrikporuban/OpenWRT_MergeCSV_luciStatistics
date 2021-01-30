import csv, os
from datetime import datetime
import matplotlib.pyplot as plt 

file_array = []
x = []
x_a = []
y = [] 
y_a = []

y_above = 200
i = 0
  
# Insert your path to csv files folder (you can use data transfer directly from OpenWrt)
# This is for ping plugin
path = "//Cloud/OpenWrt/ping/"

for file in os.listdir(path):
    # change ping- with plugin name you are outputing
    if file.startswith("ping-"):
        file_array.append(file)

for CSV in file_array:
    CSV = path + CSV
    # This is your output file with all data
    CSV_S = "Output.csv"

    # CSV merge
    with open(CSV, 'r') as csvfile: 
        csvreader = csv.reader(csvfile, delimiter=',') 
        next(csvreader, None)
        
        for row in csvreader:
            x.append(datetime.fromtimestamp(int(float(row[0]))))
            y.append(int(float(row[1])))
            if int(float(row[1])) > y_above:
                x_a.append(datetime.fromtimestamp(int(float(row[0]))))
                y_a.append(int(float(row[1])))

# Write to CSV
with open(CSV_S, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["ID", "Datum", "Ping"])

    for row in x:
        writer.writerow([i, x[i], y[i]])
        i+=1

# Plot for your data
plt.plot(x, y) 
plt.xlabel('Čas') 
plt.ylabel('Ping') 
plt.title('Ping') 
plt.show()