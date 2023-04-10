# strip and replace

sentence = "Sales analytics is the practice of generating insights from sales data, trends, and metrics to set targets and forecast future sales performance. Sales analysis is mining your data to evaluate the performance of your sales team against its goals. It provides insights about the top performing and underperforming products/services, the problems in selling and market opportunities, sales forecasting, and sales activities that generate revenue."

# .replace() method is used to replace any targetted character/characters in a given string.
# print(sentence.replace("the", 'd'))
# print(sentence)

# sentence = sentence.replace("sales", 'Sales')
# sentence = sentence.replace("Sales", "Sell", 3)
"""
  First value is the old str/char, second value is the new str/char. 3rd value is the count
"""

# print(sentence)

name = "Bello AbdulHakeem "

print(name.strip())

"""
  Strip method is used to strip out/ remove certain unwanted characters in a targetted str. By default, it strips whitespaces .strip("")
"""
website_domain = "http//:www.google.com"

website_name = website_domain.strip("http//:")
# website_name = website_name.strip("www.")
# website_name = website_name.strip(".com")

website_name = website_name.strip("w.moc")
print(website_name)



