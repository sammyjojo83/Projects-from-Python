#   By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:             Samantha Merton
# Section:          Engineering 102 556
# Assignment:   WEATHER DATA (Lab 11.13)
# Date:               18 NOVEMBER, 2022

#weather data csv file located in repositories

#initialize empty lists to store data
dates = []
average_wind = []
precipitation = []
avg_temp = []
max_temp = []
min_temp = []
#open csv file and read data
with open('WeatherDataCLL.csv') as file:
    #skip header line
    file.readline()
    file.readlines(1)
    #loop over remaining lines and append the data to appropriate list
    for line in file.readlines():
        line = line.strip().split(',')
        dates.append(line[0])
        average_wind.append(float(line[1]))
        precipitation.append(float(line[2]))
        avg_temp.append(float(line[3]))
        max_temp.append(float(line[4]))
        min_temp.append(float(line[5])) 
    
print(f"3-year maximum temperature: {max(max_temp)} F")
print(f"3-year minimum temperature: {min(min_temp)} F")
print(f"3-year average precipitation: {round(sum(precipitation)/len(precipitation),3)} inches")

#ask for input
month = input("\nPlease enter a month: ")
year = input("Please enter a year: ")
#dict to get num value of month
month_map = {
    'January':'1',
    'February':'2',    
    'March':'3',    
    'April':'4',    
    'May':'5',    
    'June':'6',    
    'July':'7',    
    'August':'8',    
    'Septempber':'9',    
    'October':'10',    
    'November':'11',    
    'December':'12',    
}
month_num = month_map[month]
#initialize empty lsits to store filtered values
max_temp_filtered = []
wind_filtered = []
days = 0
days_percipitaion = 0

#check for the condition and append the values to list
for d, maxTemp, wind, preci in zip(dates, max_temp, average_wind, precipitation):
    if (month_num in d[:2]) and (year in d[-4:]):
        max_temp_filtered.append(maxTemp)
        wind_filtered.append(wind)
        days += 1
        if preci != 0:
            days_percipitaion += 1
    
#print the final required results        
print(f"\nFor {month} {year}:")
print(f"Mean maximum daily temperature: {round(sum(max_temp_filtered)/len(max_temp_filtered), 1)} F")
print(f"Mean daily wind speed: {round(sum(wind_filtered)/len(wind_filtered), 2)} mph")
print(f"Percentage of days with precipitation: {round((days_percipitaion/days) * 100, 1)} %")

        
        
        
        

        
        