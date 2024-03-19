def season(month,day):
    if (month =='jan' and day<=21 ) or (month == 'feb') or (month == 'mar' and day >21):
        return 'spring'
    elif (month =='april' and day <=21) or (month == 'may') or (month == 'june' and day >=21):
        return 'summer'
    elif (month =='july' and day <=21) or (month == 'aug') or (month == 'sep' and day <=21):
        return 'Fall'
    else:
        return 'winter'


month=input("enter the name of month eg:-jan,feb,mar:")
day=int(input("enter the day"))

seasons=season(month,day)
print("the season for given month and day is",seasons)
