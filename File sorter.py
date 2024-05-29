import os
import shutil

#####

path=input('enter the path of the folder:--')
path=path.replace('\\','/')
os.chdir(path)
print(os.getcwd())


ext_toexclude=['db','ini','lnk']
folder=[]
content=os.listdir(path)

# Code for excluding extensions

while True:
    choice=input('Enter do you want any extension to excluded  (y/n):-->')
    if choice=='y':
        ext_toexclude_=input('Enter the extension only ("." not needed):-->')
        ext_toexclude.append(ext_toexclude_)
    if choice=='n':
        break

######
    
for i in content:
    if '.' not in i:
        folder.append(i)
for i in folder:
    if i in content:
        content.remove(i)

l=[]
extension_final=[]
for i in content:
    j=i.rsplit('.',1)
    l.append(j)

for i in l:
    extension= i[-1]
    if extension in ext_toexclude:
        continue
    extension_final.append(extension)
    if not os.path.exists(path+'/file of '+extension):
        os.makedirs(path+'/file of '+extension)

for i in l:
    for j in extension_final:
        if i[-1]==j:
            i[-1]='.'+i[-1]
            shutil.move(path+'/'+''.join(i),path+'/file of '+j+'/'+''.join(i))
    
    
    
    
