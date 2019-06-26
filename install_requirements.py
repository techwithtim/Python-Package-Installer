import subprocess
import sys
import get_pip
import os
import importlib


def install(package):
    '''
    installs a package using pip

    :param package: string
    '''
    subprocess.call([sys.executable, "-m", "pip", "install", package])


required = []

# Try to open reqirements.txt file and read all required packages
try:
    file = open("requirements.txt", "r")
    file_lines = file.readlines()
    required = [line.strip().lower() for line in file_lines]
    file.close()
except FileNotFoundError:
    print("[ERROR] No requiremnts.txt file found")


if len(required) > 0:
    print("[INPUT] You are about to install", len(required), "packages, would you like to proceed (y/n):", end=" ")
    ans = input()

    if ans.lower() == "y":
        for package in required:
            try:
            	print("[LOG] Looking for", package)
          		__import__(package)
          		print("[LOG]", package, "is already installed, skipping...")
      		except ImportError:
          		print("[EXCEPTION]", package, "not installed")

          		try:
              		print("[LOG] Trying to install", package, "via pip")
              		import pip
              		install(package)
              		print("[LOG]", package, "has been installed")
         		except ImportError:
              		print("[EXCEPTION] Pip not installed on system")
              		print("[LOG] Trying to install pip")
              		get_pip.main()
              		print("[LOG] Pip has been installed")
              		try:
                  		print("[LOG] Trying to install", package)
                  		import pip
                  		install(package)
                  		print("[LOG]", package, "has been installed")
              		except Exception as e:
                  		print("[ERROR 1]", package, "could not be installed:", e)

          		__import__(package)
  	else:
    	print("[STOP] Operation terminated by user")
else:
  print("[LOG] No packages to install")
