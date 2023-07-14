# Fetch Domain Ip 


## Usage
 
### For instance:

**server config as**
```ini
[http]
host = 127.0.0.1
port = 8082
```

host-list.txt(optional) as
``` 
github.com
``` 

**start the server ...**

request like `http://127.0.0.1:8082`

response will be like
```json
[
    ["github.com", "20.205.243.166"]
]
```

### params supported
* plain: Return plain text content, so you can paste it to host file conveniently
* urls: Joined with comma, specific urls to fetch


request like `http://127.0.0.1:8082?plain=1`

response will be like
```
20.205.243.166 github.com
```

request like `http://127.0.0.1:8082?urls=github.com,gist.github.com&plain=1`

response will be like
```
20.205.243.166 github.com
8.7.198.45 gist.github.com
```
