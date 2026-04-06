def calculation(rain,wind):
 weather_severity=(rain*10)+wind
 return weather_severity
rain_data=[]
wind_data=[]
while True:
 line=input()
 parts=line.split()
 rain_val=float(parts[0])
 if rain_val<=-1.0:
  break
 wind_val=float(parts[1])
 rain_data.append(rain_val)
 wind_data.append(wind_val)
 day_count=len(rain_data)
if day_count> 0:
 avg_rain=sum(rain_data)/day_count
 avg_wind=sum(wind_data)/day_count
 severity=calculation(avg_rain, avg_wind)
 print(avg_rain,avg_wind,day_count,severity)
#Renan Faria Schmidt