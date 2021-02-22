from os import listdir
from os.path import isfile, join
import csv,json

from os import listdir
from os.path import isfile, join
path = '/home/CNJ/dados/base/dados/justica_federal/'
sub1 = [f for f in listdir(path) ]
for sub2 in sub1:
   #if sub2 == 'processos-trt24':
     files = [f for f in listdir(path+sub2) if isfile(join(path+sub2, f))]
     for file1 in files:
        input_file = path+sub2+"/"+file1
        output_file = input_file+".csv"
      
        with open(input_file) as f:
            content=json.load(f)
        try:
            context=open(output_file,'w',newline='') # Python 3
        except TypeError:
            context=open(output_file,'wb') # Python 2
        with context as file:
            writer=csv.writer(file)
            writer.writerow(content[0].keys()) # header row
            for row in content:
                writer.writerow(row.values())
        
        
