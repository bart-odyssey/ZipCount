# ZipCount

A simple API the serves one endpoint that returns the number of addresses that are present for a given zip code.

## run api directly

Execute this in the projects app dir

```
 fastapi dev main.py
```

### Run tests

Execute this in the projects app dir

```
 pytest
```

## Requirements

- see app/requirements.txt

## Docker 

### Build
Execute this in the projects root dir

```
 docker image build --no-cache  -f docker/Dockerfile -t zip_count:latest .
```

#### Running the docker file
```
 docker run -p 8000:8000 zip_count:latest
```
