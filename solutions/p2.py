# Part I
def is_safe_report(report):
    increasing = report[1] > report[0]
    decreasing = report[1] < report[0]
    for i in range(1,len(report)):
        if increasing and report[i] - report[i-1] > 0 and report[i] - report[i-1] < 4:
            continue
        elif decreasing and report[i-1] - report[i] > 0 and report[i-1] - report[i] < 4:
            continue
        else:
            return False
    return True


# Part II
def safe_with_dampener(report):
    for i in range(len(report)):
        if is_safe_report(report[:i] + report[i+1:]):
            return True
    return False


with open('inputs/i2.txt', 'r') as file:
    safe_reports = 0
    for line in file:
        report = list(map(int, line.strip().split()))
        if safe_with_dampener(report):
            safe_reports += 1
    print(safe_reports)
