import webbrowser

url_lists = [
    'http://www.python.org',

]

# for url in url_lists:
#     webbrowser.open_new_tab(url)


########################
# requests
########################

import requests


# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

# response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)


#reading from an API


url = "https://restcountries.com/v3.1/all"
params = {"fields": "name,capital,region"}

response = requests.get(url, params=params)

print(response.status_code)

countries = response.json()
print(countries[:1])

