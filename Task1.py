with open("sample.log", "r") as file:
    lines = file.readlines()

    ipCount = {}

    for line in lines:
        ip =  line.split()[0]

        if ip in ipCount:
            ipCount[ip] += 1
        else :
            ipCount[ip] =1

    print("IP               Request Count")
    for ip, count in ipCount.items():
        print(f"{ip:<20}{count}")
