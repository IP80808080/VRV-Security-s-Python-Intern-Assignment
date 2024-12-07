with open("sample.log", "r") as file:
    lines = file.readlines()

endpointCounts = {}

for line in lines:
    p = line.split()
    if len(p) > 6:
        endpoint = p[6]

        if endpoint in endpointCounts:
            endpointCounts[endpoint] += 1
        else:
            endpointCounts[endpoint] = 1

eath = max(endpointCounts, key=endpointCounts.get)
accessCount = endpointCounts[eath]

print("Most Frequently Accessed Endpoint:")
print(f"{eath} (Accessed {accessCount} times)")
