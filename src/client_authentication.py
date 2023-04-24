"""
This script shows how signed client in keycloak can request for an access token from keycloakc service.
"""
import requests
import yaml
import os


# Get the confs
absolute_path = os.path.dirname(__file__)
conf_path = "../conf/keycloack_params.yml"
conf_path = os.path.join(absolute_path, conf_path)

with open(conf_path) as f:
    keycloack_params = yaml.load(f, yaml.BaseLoader)

# Keycloak token endpoint URL
token_url = keycloack_params['urls']['token'] 

# client ID and secret for your Keycloak client
client_id = keycloack_params['client']['id']
client_secret = keycloack_params['client']['secret']

# Set the grant type to 'password' for direct access (user to machine communication)
# Set the grant type to 'client_credentials' for service role (machine to machine communication)
# This works if client authtication flow is "Service account roles"
grant_type = 'client_credentials'

# Make a POST request to the token endpoint with the appropriate parameters
response = requests.post(token_url, data={
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': grant_type
})

# Check if the request was successful
if response.status_code == 200:
    
    # Extract the access token from the response
    access_token = response.json()['access_token']
    print('Access token:', access_token)
else:
    print(f'Failed to obtain access token, error: {response.status_code}')

