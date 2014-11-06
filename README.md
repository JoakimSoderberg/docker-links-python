
## Docker Links Environment Parser (Python version)

This is a Python rewrite of [docker-links](https://github.com/brotchie/docker-links) for nodejs by @brotchie.

[Docker](http://www.docker.io/) has a feature where you can [link containers together by name](http://docs.docker.io/en/latest/use/working_with_links_names/). For example, you start a redis-server in a docker container and expose the default redis port 6379:

    $ docker run -p 6379 -d -name redis vagrant/redis-server

You then start another containiner running a Django web service that needs to access this redis server:

    $ docker run --link redis:db -d vagrant/django
  
Docker will internally hook up these the two containers and pass host and port information to the Django web service via environment variables:

    DB_NAME=/romantic_lumiere/db
    DB_PORT=tcp://172.17.0.5:6379
    DB_PORT_6379_TCP=tcp://172.17.0.5:6379
    DB_PORT_6379_TCP_ADDR=172.17.0.5
    DB_PORT_6379_TCP_PORT=6379
    DB_PORT_6379_TCP_PROTO=tcp
    
This library provides a helper `parse_links` that will parse these environment variables into easily navigable Python dictionaries.

### Install

TODO...

### Example Usage

Consider a container that accesses three external services on two other containers. The first container exposes redis on port 6379 and postgres on 6500. The second container exposes redis on port 6379.

    DB_NAME=/romantic_lumiere/db
    DB_PORT=tcp://172.17.0.5:6379
    DB_PORT_6379_TCP=tcp://172.17.0.5:6379
    DB_PORT_6379_TCP_ADDR=172.17.0.5
    DB_PORT_6379_TCP_PORT=6379
    DB_PORT_6379_TCP_PROTO=tcp
    DB_PORT_6500_TCP=tcp://172.17.0.5:6500
    DB_PORT_6500_TCP_ADDR=172.17.0.5
    DB_PORT_6500_TCP_PORT=6500
    DB_PORT_6500_TCP_PROTO=tcp
    DB_REDIS_NAME=/romantic_lumiere/db_redis
    DB_REDIS_PORT=tcp://172.17.0.2:6379
    DB_REDIS_PORT_6379_TCP=tcp://172.17.0.2:6379
    DB_REDIS_PORT_6379_TCP_ADDR=172.17.0.2
    DB_REDIS_PORT_6379_TCP_PORT=6379
    DB_REDIS_PORT_6379_TCP_PROTO=tcp
    
Parse with `docker-links`:

```python
>> import docker_links
>> import os
>> links = docker_links.parse_links(os.environ)
```
    
Links is then the following object:

```python
>> print json.dumps(links, indent=4)
{
    "db": {
        "name": "romantic_lumiere/db",
        "proto": "tcp",
        "url": "tcp://172.17.0.5:6379",
        "hostname": "172.17.0.5",
        "tcp": {
            "6379": {
                "url": "tcp://172.17.0.5:6379",
                "hostname": "172.17.0.5"
            },
            "6500": {
                "url": "tcp://172.17.0.5:6500",
                "hostname": "172.17.0.5"
            }
        },
        "port": 6379
    },
    "db_redis": {
        "name": "romantic_lumiere/db_redis",
        "proto": "tcp",
        "url": "tcp://172.17.0.2:6379",
        "hostname": "172.17.0.2",
        "tcp": {
            "6379": {
                "url": "tcp://172.17.0.2:6379",
                "hostname": "172.17.0.2"
            }
        },
        "port": 6379
    }
}
```



