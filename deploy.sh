docker build -t cristiangarciav/pokemonapi:latest -t cristiangarciav/pokemonapi:$SHA -f ./services/api/Dockerfile ./services/api
docker push cristiangarciav/pokemonapi:latest
docker push cristiangarciav/pokemonapi:$SHA

kubectl apply -f k8s
kubectl set image deployments/api-deployment api=cristiangarciav/pokemonapi:$SHA