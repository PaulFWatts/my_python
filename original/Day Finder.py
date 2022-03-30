"""
Written by Shiven Saini :)
This program will find day of any date entered.
"""
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Defining a function to calculate Century Code.
def calCenturyCode(year):
	"""
	General Form of pre-digits : {10 + 4k}, k is a non-negative integer have C.C. 5
								 {11 + 4k}, k is a non-negative integer have C.C. 3
								 {12 + 4k}, k is a non-negative integer have C.C. 2
								 {13 + 4k}, k is a non-negative integer have C.C. 0
	"""

	PreDigits = year//100
	if (PreDigits - 10)%4 == 0:
		CenturyCode = 5
	elif (PreDigits - 11)%4 == 0:
		CenturyCode = 3
	elif (PreDigits - 12)%4 == 0:
		CenturyCode = 2
	elif (PreDigits - 13)%4 == 0:
		CenturyCode = 0
	else:
		print("Some Error happened while calculating Century Code.")		# Only for debugging purpose.

	return CenturyCode

def CalYearCode(year):
	"""
	1. Check how many 12 fits in last two digits.
	2. Subtract the 12 maximum multiple from last two digits.
	3. How many times 4 fits in the Calculation-2.
	4. Add First three calculations and Century Code.
	5. Find remainder of Calculation-4 when divided by 7.
	"""
	PostDigits = (year % 100)			# Getting last two digits only.

	Calc_1 = PostDigits//12
	Calc_2 = PostDigits%12
	Calc_3 = Calc_2//4
	Calc_4 = Calc_1 + Calc_2 + Calc_3 + calCenturyCode(year)

	YearCode = Calc_4 % 7

	return YearCode

def computeDay(dayCode, YearCode):
	dayCode = (dayCode + YearCode) % 7
	return dayCode

def calDay(date, month, year):
	YearCode = CalYearCode(year)

	if month == 1:
		if (year%4) == 0:							# Check whether the year is leap year. Doomsday of Jan, Feb depends on it.
			dayCode = date - (-3)
			return computeDay(dayCode, YearCode)
		else:
			dayCode = date - (-4)
			return computeDay(dayCode, YearCode)

	elif month == 2:
		if (year%4) == 0:
			dayCode = date - (-6)
			return computeDay(dayCode, YearCode)
		else:
			dayCode = date - 0
			return computeDay(dayCode, YearCode)

	elif month == 3:
		dayCode = date - (0)
		return computeDay(dayCode, YearCode)

	elif month == 4:
		dayCode = date - (-3)
		return computeDay(dayCode, YearCode)

	elif month == 5:
		dayCode = date - (-5)
		return computeDay(dayCode, YearCode)

	elif month == 6:
		dayCode = date - (-1)
		return computeDay(dayCode, YearCode)

	elif month == 7:
		dayCode = date - (-3)
		return computeDay(dayCode, YearCode)

	elif month == 8:
		dayCode = date - (-6)
		return computeDay(dayCode, YearCode)

	elif month == 9:
		dayCode = date - (-2)
		return computeDay(dayCode, YearCode)

	elif month == 10:
		dayCode = date - (-4)
		return computeDay(dayCode, YearCode)

	elif month == 11:
		dayCode = date - (0)
		return computeDay(dayCode, YearCode)

	elif month == 12:
		dayCode = date - (-2)
		return computeDay(dayCode, YearCode)

	else:
		print("Debugging : Month entered is invalid!")

def getDay(date, month, year):
	dayCode = calDay(date, month, year)

	if dayCode == 0:
		retunr("Sunday")
	elif dayCode == 1:
		return("Monday")
	elif dayCode == 2:
		return("Tuesday")
	elif dayCode == 3:
		return("Wednesday")
	elif dayCode == 4:
		return("Thursday")
	elif dayCode == 5:
		return("Friday")
	elif dayCode == 6:
		return("Saturday")
	else:
		print("Debugging : Error in getDay Function.")

# Getting input of Days.
try:
	date = int(input("Enter the date(DD) (As per Month) :- "))
except:
	print("Please enter only two digits (As per month(30 or 31))\nPlease try again!")
	quit()

if date in range(1, 32):
	pass
else:
	print("Date entered must be in the range [1, 31]!")
	quit()

# Getting input of Month.
try:
	month = int(input("Enter the month code(MM) [1-12] :- "))
except:
	print("Bro/Sis, Please enter only valid Digits(MM)!\nPlease try Again!")
	quit()

if month in range(1, 13):
	pass
else:
	print("Month entered must be in the range [1-12]!")
	quit()

# Getting input of Year.
try:
	year = int(input("Enter the year(YYYY) [1000-9999] :- "))
except:
	print("Lol! Months are digit only!\nPlease Try Again!")
	quit()

if year in range(1000, 10000):
	pass
else:
	print("Year entered must be in the range(1000, 10000)!")

if __name__ == "__main__":
	print(f"\nThe day on {date} {month_list[month-1]} {year} is {getDay(date, month, year)}.")
    
