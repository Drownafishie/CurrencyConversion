def convert_currency(currency_type, value):
	# Dictionary containing all conversion rates from USD to different currencies
	conversions = {"usd" : 1, "gbp" : 0.67, "euro" : 0.93, "jpy" : 121.14, "cny" : 6.46 }
	# Character case conversion to avoid conflicts of USD vs usd, etc; Whitespace removal
	currency_type = (currency_type.lower()).strip()
	# Input validation of value argument
	try:
		value = float(value)
	except ValueError:
		print("Invalid value")
		return None

	# Input validation of currency_type argument
	if(currency_type in conversions.keys()):
		"""
		Takes inputted currency and converts it to USD to serve as a base for conversions.
		conversions.pop() is called in order to remove the original currency from dictionary
		(IE If the original currency is JPY then the JPY conversion is removed from the dictionary
			and is not returned in the output dictionary)
		"""
		conversionRate = conversions.pop(currency_type, 0)
		value /= conversionRate
		# Performs conversions to all other currencies in dictionary 
		for key in conversions:
			conversions[key] *= value
		return conversions
	else:
		print("Invalid currency type")
		return None

#Code to test function
currency_type = raw_input("What is the source currency type? ")
value = raw_input("What is the value? ")
conversions = convert_currency(currency_type, value)
if (conversions is not None):
	for key, value in conversions.items():
		roundedValue = "{0:.2f}".format(value)
		print(key + ": " + roundedValue)
	raw_input("Press enter to continue")
