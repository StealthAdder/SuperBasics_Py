# -------------------------------------------------------------------------------------------
# Dictionaries
# special structure in py which allows us to store info in key value pairs
# the key must be unique 

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Oct"])
print(monthConversions.get("Oct")) #get can also be used to access the definition using key
print(monthConversions.get("Dsa", "Not a valid key"))   #As this key isnt present, the get function will print "Not a valid key"

# OUTPUT: October
# October
# Not a valid key
# ------------------------------------------------------------------------------------------------------------