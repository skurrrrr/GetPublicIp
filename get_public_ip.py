import requests
import json

# Send the request and store the response
response  = requests.get('http://icanhazip.com')

# Read the config.json file
with open('config.json', 'r') as f:
    config = json.load(f)

# Access the value from the JSON object
machine_name = config['this machine']

# Save the content of the response as a JSON file with the new key-value pair
with open('public_ip.json', 'w') as f:
    json.dump({'machine_name': machine_name, 'IP Address': response.text.strip()}, f)