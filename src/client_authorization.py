"""
This script show how a service can check if the caller is authorized to access the data.
It receive a access token from the client, then it check if it is authorized using keycloak.
"""

import requests
from keycloak import KeycloakOpenID


# this is the simulated token we are going to validate
token = {'access_token': "beyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBWDlIRF8zSXl5aXdUbWNVRHlGMjdjT1RfWm52UjJOekZ1aDdsTjFRRVRZIn0.eyJleHAiOjE2ODIwODI5MDcsImlhdCI6MTY4MjA4MjYwNywianRpIjoiZDE3ZDM5YTctYzk4Ny00YWU4LWJmNGItZGI4ZjRlYTc5MDFkIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2F1dGgvcmVhbG1zL3JlbGV2aXVtIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImJlMDk1ZDdhLTUxOGYtNDkzZC05ZGY3LTIyOTU4OTcxMjgxNSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImV3c19jbGllbnQiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiZGVmYXVsdC1yb2xlcy1yZWxldml1bSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJjbGllbnRJZCI6ImV3c19jbGllbnQiLCJjbGllbnRIb3N0IjoiMTcyLjI0LjAuMSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWV3c19jbGllbnQiLCJjbGllbnRBZGRyZXNzIjoiMTcyLjI0LjAuMSJ9.XSbJVqAxJ8cau5m20RXc60MQcOAwK_UlIA0Gsv4EG4UxIr5471_cwMIkymydtfxWY_dSO9JBT-T3H0JMH1gHtT77UlwiNekEaaXkvV4Cc514EYsFNyUlBV7wWc1uLkhRgV3vs20ATvspu_gSz1UJy_z3wDjoljU_Qe_0IszJ3LZ2UKe6RXtpNdpnl_DeU3EJ0UvW3ltNRBAikKuzLwyS_dy0K5ousR0p3kDsmyTgOoT2PgUo0z7NAGR-hZnKkddp5mwcw9ylA8SXxCGEZoOAgRUM7V7XUTiUtzGCBDbiwfOUHrE8WpY6FB5BBdHm9nWloAzx-rDyZsjwrDc8Rixa5g"}

# This has to be done to use the keycloak python library
# otherwise you have to use low-lever library and get requests to validate the token.
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                                 client_id="test_client",
                                 realm_name="relevium",
                                 client_secret_key="zTaGt5rOw4d3ZW87UiUvUGViSBp16Z1d")

KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + keycloak_openid.public_key() + "\n-----END PUBLIC KEY-----"

# verify signature option is the key to verify that the request is from a valida client.
options = {"verify_signature": True, "verify_aud": False, "verify_exp": False}
token_info = None

try:
    token_info = keycloak_openid.decode_token(token['access_token'], key=KEYCLOAK_PUBLIC_KEY, options=options)
except Exception as e:
    print(f"Not a valid token: {e}")
    # refuse request
else:
    print(f"Valid token: {token_info}")
    # manage the incoming request