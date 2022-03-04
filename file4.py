import csv
field_name=['No','Company','Car Model']
car=[{'No':1,'Company':'Ferrari','Car Model':'GH'},
     {'No':2,'Company':'BMW','Car Model':'X5'},
     {'No':3,'Company':'Audi','Car Model':'Rush'},
     {'No':4,'Company':'Toyota','Car Model':'Fortuner'}]
with open('b.csv','w') as csvfile:
     writer=csv.DictWriter(csvfile,fieldnames=field_name)
     writer.writeheader()
     writer.writerows(car)

with open('b.csv',newline='') as csvfile:
     d=csv.reader(csvfile,delimiter='|')
     for r in d:
          print(','.join(r))