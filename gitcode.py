import  os, time

initiated = os.listdir().count('.git')

if not initiated:
  os.system('git init')
  os.system('git add .')
  os.system('git commit -m "upload commit"')
  os.system('git branch -M master')
  os.system('git remote add origin git@github.com:immanuel-savvy/%s.git'
            % os.getcwd().split('/')[-1].strip())
  os.system('git push -u origin master')
else: 
  os.system('git add %s && git commit -m %d && git push -u origin master'%(os.getcwd(), time.time_ns()))
