import csv

THRESHOLD = 10

with open("sample.log", "r") as file:
    lines = file.readlines()

requests_per_ip = {}
endpoint_counts = {}
failed_attempts = {}

for line in lines:
    parts = line.split()
    if len(parts) > 8:
        ip = parts[0]
        endpoint = parts[6]
        status_code = parts[8]

        if ip in requests_per_ip:
            requests_per_ip[ip] += 1
        else:
            requests_per_ip[ip] = 1

        if endpoint in endpoint_counts:
            endpoint_counts[endpoint] += 1
        else:
            endpoint_counts[endpoint] = 1

        if status_code == "401":
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

most_accessed_endpoint = max(endpoint_counts, key=endpoint_counts.get)
most_accessed_count = endpoint_counts[most_accessed_endpoint]

suspicious_activity = [
    {"IP Address": ip, "Failed Login Count": count}
    for ip, count in failed_attempts.items()
    if count > THRESHOLD
]

print("Requests per IP:")
print(f"{'IP Address':<20}{'Request Count'}")
for ip, count in requests_per_ip.items():
    print(f"{ip:<20}{count}")
print()

print(f"Most Frequently Accessed Endpoint: {most_accessed_endpoint} (Accessed {most_accessed_count} times)\n")

print("Suspicious Activity Detected:")
print(f"{'IP Address':<20}{'Failed Login Count'}")
for activity in suspicious_activity:
    print(f"{activity['IP Address']:<20}{activity['Failed Login Count']}")
print()

with open("log_analysis_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["Requests per IP"])
    writer.writerow(["IP Address", "Request Count"])
    for ip, count in requests_per_ip.items():
        writer.writerow([ip, count])
    writer.writerow([])

    writer.writerow(["Most Accessed Endpoint"])
    writer.writerow(["Endpoint", "Access Count"])
    writer.writerow([most_accessed_endpoint, most_accessed_count])
    writer.writerow([])

    writer.writerow(["Failed Attempts"])
    writer.writerow(["IP Address", "Failed Login Count"])
    for ip, count in failed_attempts.items():
        print(f"{ip} \t\t {count}")
        writer.writerow([ip, count])
