import os
 
print("=== Files in images/ folder ===")
try:
    files = os.listdir("images")
    for f in files:
        print(f)
except FileNotFoundError:
    print("ERROR: 'images' folder not found!")
    print("Current directory:", os.getcwd())