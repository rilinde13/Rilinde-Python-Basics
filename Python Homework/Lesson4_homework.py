import requests
import json


# Task 1: Get API data
def get_api_data():
    response = requests.get('https://www.ndosiautomation.co.za/APIDEV/groups')
    print(f'Status code is {response.status_code}')

    groups_response = response.json()
    return groups_response


# Task 2: Save data to a file
def save_data_to_file(data):
    with open('groups.json', 'w') as file:
        json.dump(data, file)
    print('Data saved to groups.json')


# Task 3: Read and search data
def search_group():
    with open('groups.json', 'r') as file:
        data = json.load(file)

    group_name = input('Enter the group name to search for: ')

    my_list = data['data']

    for group in my_list:
        if group['Name'] == group_name:
            print(f'Group found! Group Id is {group["Id"]} and Name is {group["Name"]}')
            return

    print(f'Error: Group "{group_name}" was not found.')


# Run all tasks
api_data = get_api_data()
save_data_to_file(api_data)
search_group()