# assume there are many cities on earth with authorities
# publish temperature every day, eod
# they may make mistakes -> temperature can be wrong
# may republish later in the day, changing the temperature
#
# goal: design a data structure / db to store all of the data including the changes
# provide a function to access the structure / db to get all the historical data for a city
# !!: get by as of a date

# new york: feb 6 : 5  degrees
#           feb 7 : 6  degrees
#           feb 8 : 10 degrees
#           feb 15: feb 7 -> 8 degrees

# store a diff for each day
# a database entry, or entry in an array or similar
# detailiing what changed on a day
# then, when information is requested up to a particular day
# the changes can be replayed, similar to a log-structured file system
# for performance reasons we can make complete images of the data
# at regular intervals, so that if we want data up to a particular date
# we may start with a complete image and replay at most the number of days
# that is the period of the complete image interval

# hashmap: city names -> instance
# array representing each day in a month
# each entry detail the changes* to the data on that day
# we regularly make complete images of the data (say, at the end of each month)
# if you want to get a view of the data on a particular day
# you can start from the most recent complete image, and replay the changes
# by going through the days in order

# time series db:
# key: (city, day, month, year) -> changes in that city's data for that date

# storing the whole image for each day
# key: (city, day, month, year) -> complete view of the data
