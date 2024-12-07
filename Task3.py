THRESHOLD = 10
with open("sample.log", "r") as file:
    lines = file.readlines()

failed_attempts = {}

for line in lines:
    if "401" in line:
        ip = line.split()[0]

        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1

print("Suspicious Activity Detected:")
print(f"{'IP Address':<20}{'Failed Login Attempts'}")
print("-" * 35)

for ip, count in failed_attempts.items():
    print(f"{ip} \t\t {count}")
    if count > THRESHOLD:
        print(f"{ip:<20}{count}")
