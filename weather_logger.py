temps = []

while True:
    temp = input("Enter temperature: ")

    if temp == "done":
        break

    temps.append(float(temp))


def summarize(temps):
    return {
        "minimum": min(temps),
        "maximum": max(temps),
        "average": sum(temps) / len(temps)
    }


print(summarize(temps))