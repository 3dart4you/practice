import requests
from my_data import token, username
from datetime import datetime

GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params) #creating an account
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers) #creqting a graph
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Km?"),
}
response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers) #updating the graph
print(response.text)

update_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/{pixel_data['date']}"

new_pixel_data = {
    "quantity": "18",
}

# response = requests.put(update_endpoint, json=new_pixel_data, headers=headers) #update the pixel
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/{pixel_data['date']}"
# response = requests.delete(delete_endpoint, json=pixel_data, headers=headers) # deleting pixel
# print(response.text)