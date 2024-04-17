import os
import shutil


path=input('enter the path of the folder:--')
path=path.replace('\\','/')
os.chdir(path)
print(os.getcwd())

folder=[]
content=os.listdir(path)
print(content)


for i in content:
    if '.' not in i:
        folder.append(i)
for i in folder:
    if i in content:
        content.remove(i)

List_=[]
extensions_=[]
for i in content:
    j=i.rsplit('.',1)
    List_.append(j)
for i in List_:
    extension= i[-1]
    extensions_.append(extension)
    if not os.path.exists(path+'/file of '+extension):
        os.makedirs(path+'/file of '+extension)

for i in List_:
    for j in extensions_:
        if i[-1]==j:
            
            i[-1]='.'+i[-1]
            shutil.move(path+'/'+''.join(i),path+'/file of '+j+'/'+''.join(i))

    
    
    
    
