import os

#print(dir(os))  # shows all attributes and methods

# current directory: note that is not the directory with the source code!!!
print(os.getcwd()) 
# CWD can be changed by os.chdir()
os.chdir('/home/user/projects/selenium/app/src')
print(os.getcwd()) 

print(os.listdir())
# os.makedirs(1/2/3/4) # will create all the subdirectories

for dir_path, dir_names, file_names in os.walk(os.getcwd()):
#for dir_path, dir_names, file_names in os.walk('/home/user/'): # bad idea
    print('Current Path: ', dir_path)
    print(' Directories: ', dir_names)
    print('       Files: ', file_names)
    print('')

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)  # /home/user/test.txt

