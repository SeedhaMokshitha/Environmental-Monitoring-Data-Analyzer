# Environmental Monitoring Data Analyzer

def analyze_data(data, limit):
    total = 0
    count = 0
    highest = data[0][0]
    lowest = data[0][0]

    print("\nEnvironmental Monitoring Report")
    print("-" * 40)

    for day in range(len(data)):
        for reading in range(len(data[day])):
            value = data[day][reading]

            total += value
            count += 1

            if value > highest:
                highest = value

            if value < lowest:
                lowest = value

            if value <= limit:
                status = "Normal"
            else:
                status = "Above Limit"

            print("Day", day + 1,
                  "Reading", reading + 1,
                  ":", value, "-", status)

    average = total / count

    print("\nSummary")
    print("-" * 40)
    print("Total Readings :", count)
    print("Average Value  :", round(average, 2))
    print("Maximum Value  :", highest)
    print("Minimum Value  :", lowest)
    print("Threshold     :", limit)


# Main program
print("Environmental Monitoring Data Analyzer")
print("1. Air Quality")
print("2. Water Quality")

choice = int(input("Select monitoring type: "))

if choice == 1:
    data = [
        [45, 60, 72],
        [55, 80, 95],
        [40, 65, 110]
    ]
    limit = 100
    print("\nAir Quality Selected")

elif choice == 2:
    data = [
        [6.5, 7.0, 7.2],
        [6.8, 8.1, 7.5],
        [6.2, 7.4, 8.5]
    ]
    limit = 8.0
    print("\nWater Quality Selected")

else:
    print("Invalid choice!")
    exit()

analyze_data(data, limit)
