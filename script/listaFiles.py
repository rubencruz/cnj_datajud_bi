from os import listdir
from os.path import isfile, join
path = '/home/CNJ/dados/base/dados/justica_eleitoral/'
sub1 = [f for f in listdir(path) ]
i=0
for sub2 in sub1:
   files = [f for f in listdir(path+sub2) if isfile(join(path+sub2, f))]
   for file1 in files:
      i++
      pathFile = path+sub2+file1
      print(pathFile)
      print("numero: ", i)
