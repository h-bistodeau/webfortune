# webfortune

## Clone repository
```
git clone https://github.com/kaylacoats/webfortune
cd webfortune
```

## Create a virtual environment
```
python3 -m venv env
source env/bin/activate
```

## Build docker
```
docker build -t [name]/webfortune .
docker run -dp [port]:5000 [name]/webfortune
```

## Run flask
```
flask run
```

## Websites
```
http://localhost:[port]/
- reroutes to fortune

http://localhost:[port]/fortune
- displays a random fortune

http://localhost:[port]/cowsay/[message]
- displays a message you input inside a cow

http://localhost:[port]/cowfortune
-displays a random fortune inside a cow
```

## Run Tests
```
pytest
```

## Remove docker container & Deactivate virtual environment
```
docker ps
docker rm -f [containername associated with port]

deactivate
```
