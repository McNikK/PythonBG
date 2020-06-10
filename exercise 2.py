time = int(input('Please write time in seconds: '))
hr_vr = time//3600  #  hours
min_vr = time // 60 # seconds
bl_hr = min_vr % 60 # balance minute
bl_vr = time % 60 # balance seconds
if min_vr > 60:
    min_vr = bl_hr
print(hr_vr, 'hour(s):', min_vr, 'minute(s):', bl_vr, 'second(s):')


