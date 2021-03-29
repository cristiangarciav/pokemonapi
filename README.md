# Pokemon API project

This is a sample rest API that provides information in order to be ready for the Pokemon Battle!

# Remote Access

This Pokemon API has been temporaly installed into a Google Cloud Kubernetes Cluster
and can be accessed through the below URL:

  https://35.192.16.221/

> NOTE: This deployment is just temporal and will be disabled soon to avoid extra costs.

## Local Installation

You can clone the respository to your machine in order to run the API locally:
  ```bash
  $ git clone https://github.com/cristiangarciav/pokemonapi.git
  ```

## Running a container locally

The project runs inside a [Docker](https://docs.docker.com/)
container, the container runs with a volume bound to the `services/api`
folder. This approach doesn't require you to install any dependencies other
than [Docker Desktop](https://www.docker.com/products/docker-desktop) on
Windows and Mac, and [Docker Compose](https://docs.docker.com/compose/install/)
on Linux.

1. Build the docker image 

   ```bash
   docker-compose build
   ```

1. Run the built image

   ```bash
   docker-compose up
   ```

   > NOTE: You can run both commands at once with `docker-compose up --build`.

1. Verify that the service is working. 

   Open your web browser and type `http://localhost:5000` in your navigation bar,
   This opens a local instance of the API. You can now make POST requests to the API

### Cleanup

To stop Docker Compose, on your terminal window, press **Ctrl + C**. 

To remove the produced images run:

```console
docker-compose rm
```
For more information see the [Docker Compose
documentation](https://docs.docker.com/compose/gettingstarted/).

### Project Structure:

```console
├── README.md
├── cheat_sheet
├── deploy.sh
├── docker-compose.yaml
├── k8s
│   ├── api-cluster-ip-service.yaml
│   ├── api-deployment.yaml
│   └── ingress-service.yaml
├── service-account.json.enc
└── services
    └── api
        ├── Dockerfile
        ├── Pipfile
        ├── Pipfile.lock
        ├── manage.py
        ├── requirements.txt
        ├── src
        │   ├── app.py
        │   ├── handlers
        │   │   ├── __init__.py
        │   │   └── routes.py
        │   ├── resources
        │   │   ├── __init__.py
        │   │   ├── pokemon.py
        │   │   └── pokeresources.py
        │   └── templates
        │       └── index.html
        └── test
            ├── get_mock_data.py
            ├── mock_data
            │   ├── language_es_mock.json
            │   ├── move_attract_mock.json
            │   ├── move_brick-break_mock.json
            │   ├── move_bulldoze_mock.json
            │   ├── pokemon_arceus_mock.json
            │   ├── pokemon_charmander_mock.json
            │   ├── pokemon_drapion_mock.json
            │   ├── pokemon_grumpig_mock.json
            │   ├── pokemon_pikachu_mock.json
            │   ├── type_dark_mock.json
            │   ├── type_electric_mock.json
            │   └── type_poison_mock.json
            ├── mock_data.py
            └── test_pokemonapi.py      
```
