performances = {}

try:
    schedule_file = open('schedule.txt', 'r')
except:
    print("File doesn't exist")
except FileNotFoundError as err:
    print(err)
for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show] = time

schedule_file.close()
print(performances)