# fast_alpr_http_api_wrapper
A simple wrapper for  fast_alpr https://github.com/ankandrew/fast-alpr/blob/master/README.md?plain=1

# Build the project
```docker build -t fast_alpr https://github.com/luisenriqueflores/fast_alpr_http_api_wrapper.git```

# To run 
```docker run -d -p 8000:8000 --name fast_alpr-container fast_alpr```

# Docker.yaml
```services:
  open-alpr-http-wrapper:
    container_name: fast-alpr-container
    restart: unless-stopped
    image: fast-alpr-http-wrapper:latest
    ports:
      - "2000:2000"```
