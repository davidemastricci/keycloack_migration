# Keyclock Migration

This a guide project for whenever you have to configure\test your keyclock instance on your laptop and then migrate elsewhere.

First of all this guide use Keyclock docker instance and PostegresSQL docker instance to store the information.

## Pre-requisites

You must have docker installed on you machine.

## Start your keyclock

Use [run_docker_compose.sh](./run_docker_compose.sh) to set everything up

**Warnings**: 
- keyclock is up and running on localhost:8080
- PostegresSQL is up and running on localhost:5432

You can change them in .env file.


## Export your keyclock

once you've configured your instance you can export the desidered realm using running the [run_export.sh](./run_export.sh). When it ends use CTRL+c to leave the console.
It will create a file inside *bkp\export* path, open it and check that your clients and users are present.

## Migrate your keyclock

- Create a directory *bkp\import* and copy the exported json.
- Move this porject into the other machine.
- Use the [run_docker_compose_import.sh](./run_docker_compose_import.sh) and and enjoy.


## Bonus 1: Test a client with python

Inside directory src there are some routines you can use to test your client log in.
- Use [client_authentication.py](./src/client_authentication.py) to test the access_token request. Adjust your client id, client secret and realm name in [keycloack_params.yml](./conf/keycloack_params.yml).
- Enjoy.


## Bonus 2: Test client authorization
Inside directory src there are some routines you can use to test if a client is authorized.
- Use [client_authorization.py](./src/client_authorization.py) to test decode the access_token.
- Create another client in keycloak and replace the test client and real with yours in the script.
- Replace the token with a toke generated from a valid client, use [client_authentication.py](./src/client_authentication.py) for example.
- Enjoy.




## Acknowledgements

 - [How to export a realm with users and secrets](https://keepgrowing.in/tools/keycloak-in-docker-5-how-to-export-a-realm-with-users-and-secrets)
 - [How to import a Keycloak realm](https://keepgrowing.in/tools/keycloak-in-docker-2-how-to-import-a-keycloak-realm/)
 - [How to run Keycloak in a Docker container](https://keepgrowing.in/tools/keycloak-in-docker-1-how-to-run-keycloak-in-a-docker-container)

