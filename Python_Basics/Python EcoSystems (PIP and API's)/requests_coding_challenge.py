import requests

# 1. use .get method to fetch data from url
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

if response.status_code == 200:
    print('Success!')

    # 2. Save response as JSON Object(Dictionary)
    data = response.json()
    print(data['title'])
else:
    print('Something went wrong!')
