# Pokemon API project

This is a sample rest API that provides information for the Pokemon Battle!

## App Description

The app is written in Python with Flask Restful as the web framework. And has been validated with the Open API v 2.0 specification. 
> File: pokemonapi_spec.json

## App Architecture

The app is deployed into a Kubernetes Cluster. It uses Kubernetes Deployments, which will allow the application to be scaled. Deployments also provide additional features to control how new image updates are deployed and are handled on failures.

### - gUnicorn Application Server
In order to run the Flask API an application server is required and gUnicorn is used in this implementation. The Kubernetes cluster is being configured to use 3 replicas of the gUnicorn server

### - NGINX Web Server
A web server will handle all incoming requests, and then reverse proxy them to the application server. While the container could run the application server alone, a web server provides more control over the traffic hitting the Flask API.

NGINX is a highly efficient, event-driven web server that is capable of handling high volumes of traffic.


## Remote Access

The Application has been temporarily installed into a Google Cloud Kubernetes Cluster
and can be accessed through the below URL:

  https://35.192.16.221/

> NOTE: This deployment is just temporal and will be disabled soon to avoid extra costs.

## Local Installation

You can clone the repository to your machine in order to run the API locally:
  ```bash
  $ git clone https://github.com/cristiangarciav/pokemonapi.git
  ```
Once the project is in your machine you can run it using the Docker Command line tools.

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

## Cleanup

To stop Docker Compose, on your terminal window, press **Ctrl + C**. 

To remove the produced images run:

```console
docker-compose rm
```
For more information see the [Docker Compose
documentation](https://docs.docker.com/compose/gettingstarted/).

## Project Structure:

```console
├── deploy.sh
├── docker-compose.yaml
├── k8s
│   ├── api-cluster-ip-service.yaml
│   ├── api-deployment.yaml
│   └── ingress-service.yaml
└── services
    └── api
        ├── Dockerfile
        ├── manage.py
        ├── src
        │   ├── app.py
        │   ├── handlers
        │   │   └── routes.py
        │   ├── resources
        │   │   ├── pokemon.py
        │   │   └── pokeresources.py
        │   └── templates
        │       └── index.html
        └── test
            ├── get_mock_data.py
            ├── mock_data
            │   ├── language_es_mock.json
            │   ├── move_attract_mock.json
            │   ├── move_brick-break_mock.json
            │   ├── move_bulldoze_mock.json
            │   ├── pokemon_arceus_mock.json
            │   ├── pokemon_charmander_mock.json
            │   ├── pokemon_drapion_mock.json
            │   ├── pokemon_grumpig_mock.json
            │   ├── pokemon_pikachu_mock.json
            │   ├── type_dark_mock.json
            │   ├── type_electric_mock.json
            │   └── type_poison_mock.json
            ├── mock_data.py
            └── test_pokemonapi.py      
```
## Services Folder:
The "services" folder contains the application components/services that the application requires. In this case only one component exits: 
  
  - The "api" service.
 
By organizing the components into the "services" folder it is possible to scale up the application easily by adding different services in the future. Each service folder may represent a docker container.

  Example:
  - Front-end service.
  - Static web content service.
  - Database service.

## K8s Folder:

The "k8s" folder contains the Kubernetes cluster configuration files. The Cluster is configured to have 3 api deployment replicas and an ingress-nginx service that acts as a load balancer. 
Each "api" pod has a WSGI Gunicorn server that can be scaled up to attend the requests from the clients.

  ```console
  ├── k8s
  │   ├── api-cluster-ip-service.yaml
  │   ├── api-deployment.yaml
  │   └── ingress-service.yaml
  ```
Each yaml file represents a component insid inside the Kubernetes Cluster.

## Deployment:

The app has been deployed into Google Cloud infrastructure, by making use of the Kubernetes service. 3 Nodes has been setup hosting the 3 replica "api" pods. 
The ingress service specifies the configuration of the NGINX Ingress Controller. For more information see the [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/).


## Continuous Integration:

The app has been set up to make use of a CI automated pipeline by using the Travis CI service.  Travis CI is integrated with Github with below flow:

  1. Push to Git;
  2. A CI process is triggered;
  3. The branch is pulled, the app is built, and tests are run;
  4. The results of this process are sent to the Cloud provider.

The building process is specified by the .travis.yml configuration file. If the build is successful and merged into the "main" branch, it is automatically deployed into the Google Cloud infrastructure.


# API and SDK Documentation

## End-Point specification:

## 'Common moves' end-point: 
    From a given list of pokemon names/ids it compares the moves between the pokemons and returns the common (intersaction) moves between them
  ```console
  /common_moves
  ```
## Methods:

    POST:
    /common_moves

Parameters:
  Body parameters

  Description:
  ```console
   {
      Required: pokemonList
      pokemonList:	
        [
          type: string
          example: pikachu
        ]
      language:	
          type: string
          description: valid language ISO code
          example: es
      limit:	
          type: integer (int32)
          description: limits the number of output elements
          example: 10
    }
  ```
### Headers:
  ```console
    "Content-Type: application/json"
  ```

### Sample POST Body:
  ```console
     {
        "pokemonList":
            ["pikachu",
            "drapion"
            ],
        "language" : "es",
        "limit" : 5
    }
  ```
## Responses:

Status: 200 - successful operation

Schema:
  ```console
   {
    commonMoves:	
    [
      type: string
      example: Atraccion, Electrico
    ]
  }
  ```
 ### Sample 200 response:
  ```console
  {
      "commonMoves": [
          "Atracción",
          "Demolición",
          "Seducción",
          "Confidencia",
          "Excavar"
      ]
  }
  ```
Status: 404 - Invalid resource parameter

Status: 405 - Malformed request

Status: 424 - External resource not responding

## Usage and SDK Sample:

### Curl Sample:
  ```console
    curl --insecure --header "Content-Type: application/json" \
  --request POST \
  --data '{"pokemonList": ["pikachu", "drapion"], "language" : "es", "limit" : 5}' \
  https://35.192.16.221/common_moves
  ```
  > Note: it is necessary to pass the --insecure option because the SSL certificate is not valid.


## Compare Damage End-Point: 
    Compare the deal and received damage from two given Pokemon names/ids. It will compare the fighter likelihood to deal or receive damage (0x, 1x, 2x) to the contender based on the fighter's pokemon type(s)


## Methods:

    POST:
    /compare_damage

Parameters:
  Body parameters

  Description:
  
  ```console
   {
    Required: 
      - fighter
      - contender
      fighter:	
          type: string
          description: Pokemon (fighter) name/id
          example: pikachu
      contender:	
          type: string
          description: Pokemon (contender) name/id
          example: charmander
    }
  ```
### Headers:
  ```console
    "Content-Type: application/json"
  ```

### Sample POST Body:
  ```console
    {
      "fighter" : "pikachu",
      "contender" : "drapion"
    }
  ```

## Responses:

Status: 200 - successful operation

Schema:
```console
      {
        fighter: {
          name:	
            type: string
            description: Pokemon name
            example: pikachu
          id:	
            type: integer (int32)
            description: Pokemon id
            example: 25
          types:	
            [
            type: string
            description: Pokemon type
            example: electric
            ]
          deal_damage:	
            type: integer (int32)
            description: deal damage multiplier (0x, 1x, 2x)
            example: 2
          receive_damage:	
            type: integer (int32)
            description: receive damage multiplier (0x, 1x, 2x)
            example: 1
        }
      }
```
### Sample 200 response:
  ```console
  {
      "fighter": {
          "name": "pikachu",
          "id": 25,
          "types": [
              "electric"
          ],
          "deal_damage": 1,
          "receive_damage": 1
      }
  }
  ```
Status: 404 - Invalid resource parameter

Status: 405 - Malformed request

Status: 424 - External resource not responding

## Usage and SDK Sample:

### Curl Sample:
  ```console
    curl --insecure --header "Content-Type: application/json" \
      --request POST \
      --data '{"fighter" : "pikachu", "contender" : "drapion"}' \
      https://35.192.16.221/compare_damage
  ```
  > Note: it is necessary to pass the --insecure option because the SSL certificate is not valid.
