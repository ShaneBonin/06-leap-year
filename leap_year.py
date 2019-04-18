# Write a function `is_leap_year` that takes a year as a parameter
#   -->**RETURNS**<-- True if the year is a leap year, False otherwise.
# The logic-chain is somewhat similar to the Sherlock problem.

# Don't forget to reach out for help after your own due diligence

def is_leap_year(year):
   leap = False
   if (year % 100 == 0) and (year % 400 != 0):
       leap = False
   elif  year % 4 == 0:
       leap = True
   else:
       leap = False
   return leap
