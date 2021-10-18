# python program Find number of 
# times every day occurs in a Year 


import datetime 
import calendar 

def day_occur_time(year): 
	
	# stores days in a week 
	days = [ "Monday", "Tuesday", "Wednesday", 
		"Thursday", "Friday", "Saturday", 
		"Sunday" ] 
	
	# Initialize all counts as 52 
	L = [52 for i in range(7)] 
	
	# Find the index of the first day 
	# of the year 
	pos = -1
	day = datetime.datetime(year, month = 1, day = 1).strftime("%A") 
	for i in range(7): 
		if day == days[i]: 
			pos = i 
			
	# mark the occurrence to be 53 of 1st day 
	# and 2nd day if the year is leap year 
	if calendar.isleap(year): 
		L[pos] += 1
		L[(pos+1)%7] += 1
		
	else: 
		L[pos] += 1
		
	
	# Print the days 
	for i in range(7): 
		print(days[i], L[i]) 
	


def occu_days(year):
	occu_day = {
	"Monday":52,
	"Tuesday":52,
	"Wednesday":52,
	"Thursday":52,
	"Friday":52,
	"Saturday":52,
	"Sunday":52
	}

	if calendar.isleap(year): 
		day_one= datetime.datetime(year, month = 1, day = 1).strftime("%A")
		day_two= datetime.datetime(year, month = 1, day = 2).strftime("%A")
		occu_day[day_one] +=1
		occu_day[day_two] +=1
		
	else: 
		day_one= datetime.datetime(year, month = 1, day = 1).strftime("%A")
		occu_day[day_one] +=1

	for k,v in occu_day.items():
	    print(k+' '+str(v))

# Driver Code 
year = int(input("Enter year:"))

day_occur_time(year) 
print("My solution ho.")
occu_days(year)

