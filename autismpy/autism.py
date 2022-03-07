import subprocess
import time
import os
for x in range(120,153):
	command = 'py randomware.py --output biglinus'+str(x)+'.jpg --rainbow --input biglinus.jpg --lumen -100 --offset '+str(x*10)
	subprocess.call(command,shell=True)
