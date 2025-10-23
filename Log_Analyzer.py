import re

with open("/var/log/auth/log") as log:
   for line in log:
      if re.search(r"Failed password", line) or re.search(r"Accepted password", line):
         print(line.strip())
