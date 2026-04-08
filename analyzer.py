import re

failed_attempts = {}
threshold = 3

with open("auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            
            ip = re.findall(r"\d+\.\d+\.\d+\.\d+", line)
            
            if ip:
                ip = ip[0]
                
                if ip in failed_attempts:
                    failed_attempts[ip] += 1
                else:
                    failed_attempts[ip] = 1

print("Failed Login Summary:\n")

for ip, count in failed_attempts.items():
    print(f"{ip} → {count} attempts")

print("\nSuspicious IPs:\n")

with open("alerts.txt", "w") as alert_file:
    for ip, count in failed_attempts.items():
        if count >= threshold:
            alert_msg = f"ALERT: {ip} → {count} failed attempts"
            print(alert_msg)
            alert_file.write(alert_msg + "\n")
