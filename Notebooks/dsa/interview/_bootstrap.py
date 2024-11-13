import sys
import os
 
notebook_dir = os.getcwd()
root_dir = os.path.abspath(os.path.join(notebook_dir, '..', '..'))  

if root_dir not in sys.path:
    sys.path.append(root_dir)