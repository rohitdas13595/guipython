import os
import numpy as np 


#creating a method to store data
class saveData:
    im=[]
    la=[]

#import dlod
arr = os.listdir('images')
print(arr)
for i in arr:
    cmd='dlod.py -i images/'+i+' -p MobileNetSSD_deploy.prototxt.txt -m MobileNetSSD_deploy.caffemodel'
    os.system(cmd)


#os.system('python dlod.py -i images/example_08.jpg -p MobileNetSSD_deploy.prototxt.txt -m MobileNetSSD_deploy.caffemodel')
#os.system('python dlod.py -i images/example_07.jpg -p MobileNetSSD_deploy.prototxt.txt -m MobileNetSSD_deploy.caffemodel')