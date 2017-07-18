import sys
import os

# simple binary echo script
sys.stdout.write(sys.stdin.read())

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
  print (f)

files = [f for f in os.listdir('../') if os.path.isfile(f)]
for f in files:
  print (f)
  
