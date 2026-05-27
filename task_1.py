a = '1h 45m,360s,25m,30m 120s,2h 60s'
b = a.split(',')
sum_minutes = 0

for i in b:
    time = i.split()
    string_minutes = 0
    
    for value in time:
        if 'h' in value:
            hours = int(value.replace('h', ''))
            string_minutes += hours * 60
        elif 'm' in value:
            minutes = int(value.replace('m', ''))
            string_minutes += minutes
        elif 's' in value:
            seconds = int(value.replace('s', ''))
            string_minutes += seconds // 60
    
    sum_minutes += string_minutes

print(sum_minutes)