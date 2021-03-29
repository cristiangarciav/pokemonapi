# Pokemon API project

This is a sample rest API that provides information to be ready for the Pokemon Battle!

# App Description

The app is written in Python with Flask Restful as the web framework. And has been validated with the Open API v 2.0 specification. 
> File: pokemonapi_spec.json

# App Architecture

The app is deployed into a Kubernetes Cluster. It uses Kubernetes Deployments, which will allows to scale the application. Deployments also provide additional features to control how new image updates are deployed and are handled on failures.

- gUnicorn Application Server
In order to run the Flask API an application server is required and gUnicorn is used in this implementation. The Kubernetes cluster is being configured to use 3 replicas of the gUnicorn server

- NGINX Web Server
A web server will handle all incoming requests, and then reverse proxy them to the application server. While the container could run the application server alone, a web server provides more control over the traffic hitting the Flask API.

NGINX is a highly efficient, event-driven web server that is capable of handling high volumes of traffic.


# Remote Access

The Application has been temporaly installed into a Google Cloud Kubernetes Cluster
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
├── deploy.sh
├── docker-compose.yaml
├── k8s
│   ├── api-cluster-ip-service.yaml
│   ├── api-deployment.yaml
│   └── ingress-service.yaml
└── services
    └── api
        ├── Dockerfile
        ├── manage.py
        ├── src
        │   ├── app.py
        │   ├── handlers
        │   │   └── routes.py
        │   ├── resources
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
## Services Folder:
The "services" folder contains the application components/services that the application requires. In this case only one component exits: 
  - The "api" service.
 
While organizing the components into the "services" folder is possible to scale up the application easily by adding different services in the future. Each service folder may represent a docker container.
  Example:
  - Front-end service.
  - Static web content service.
  - Data base service.

## K8s Folder:
The "k8s" folder contains the Kubernetes cluster configuration files. The Cluster is configured to have 3 api deployment replicas and an ingress-nginx services that acts as a load balancer. 
Each "api" pod has a WSGI Gunicorn server that can be scaled up to serve the requests from the clients.



