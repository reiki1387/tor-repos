import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

#if directory doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)  #make new directory
    
#print(os.listdir(path)) #['bulbasaur.jpg', 'charmander.jpg', 'pikachu.jpg', 'squirtle.jpg']
for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]

     #added the \ in case user doesn't enter it. Same as escape sequence \n, \t
    img = Image.open(f'{path}\\{filename}')
    img.save(f'{directory}\\{clean_name}.png', 'png') #arg1 = new name, arg2= conversion(new extension)
print('all done!')
