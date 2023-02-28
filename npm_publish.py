import os, time, sys
print(sys.argv)

curr_folder_name = os.getcwd().split('/')[-1].strip()

os.system('zip -r ../%s.zip ../%s'%(curr_folder_name, curr_folder_name))

os.system('rm -rf ./node_modules')
os.system('npm install')

def compile_files(folder=None):
  if folder: 
    if folder == 'node_modules': return
    os.chdir(folder)
  directories = os.listdir()
  for file_to_compile in directories:
    if file_to_compile.endswith('.js'):
      os.system('npx babel %s --out-file %s'% (file_to_compile,file_to_compile))
      print("Compiled: %s/%s"%(folder or '',file_to_compile))
    else:
      if (os.path.isdir(file_to_compile)):
        compile_files(file_to_compile)
  if folder: os.chdir('..')
  
compile_files()

if not sys.argv.count('--no-publish'):
  os.system('npm publish')
  os.chdir('..')
  os.system('zip -r ../%s-compiled.zip ../%s'%(curr_folder_name, curr_folder_name))
  os.system('unzip %s.zip'%curr_folder_name)
  os.chdir('./%s'%curr_folder_name)
  os.system('python3 ~/Develop/scripts/gitcode.py')
else:
  pass
  

