
def return_day(nums):
    days= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if nums>0 and nums<=len(days):
        return days[nums-1]
    else:
        return None
    
print (return_day(2))