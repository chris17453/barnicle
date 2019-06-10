# barnicle
A Dynamic API for RPC 


## How
- Create endpoints dynamically
- Endpoints connect to scripts
- Scripts are calles with endpoint parameters
- The results of the script is passed as the result of the api call


## template
```
endpoints:
    - endpoint: dns
      parameters:
        - ip
        - range
      script: dns.py
    - endpoint: time
      script: time.py
    - endpoint: heartbeat
      script: heartbeat.py
    - endpoint: date
      script: date.py


```