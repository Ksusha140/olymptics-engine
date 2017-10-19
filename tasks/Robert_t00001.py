def year_days(year):
	leap = year % 4 == 0
	return "{} has {} days".format(year, 365+leap)