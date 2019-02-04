# image_resize_api

Default enter point is http://localhost:8080/

You can find some information there.

## How to run

You have to install ```docker``` and  ```docker-compose```

After this, you have to run the below command and wait.
```bash
$ docker-compose up -d
```

## API paths

*Important!!! Input data checking is not implemented yet*

There are 3 paths:

### ```/image/``` - POST for resizing JPEG and PNG images

Required fields:

```height=<1-9999px>```

```width=<1-9999px>```

```image=<Bytes like object>```

Return:

```
HTTP/1.1 200 OK
Content-Length: 51
Content-Type: application/json; charset=utf-8
Date: Mon, 04 Feb 2019 21:21:16 GMT
Server: Python/3.7 aiohttp/3.5.4

{
    "task_id": "e4e62a32-59ce-4f11-ba35-699e03a7cc56"
}
```

Example for [HTTPie](https://httpie.org/):
```bash
http -f POST localhost:8080/image/ height=128 width=128 image@~/test.jpeg
```
    
### ```/image/{id}``` - GET get resized image
Return:
```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/octet-stream
Date: Mon, 04 Feb 2019 21:23:38 GMT
Server: Python/3.7 aiohttp/3.5.4
```
### ```/image/{id}/status/``` - GET check resizing status
Return:
```
HTTP/1.1 200 OK
Content-Length: 67
Content-Type: application/json; charset=utf-8
Date: Mon, 04 Feb 2019 21:22:37 GMT
Server: Python/3.7 aiohttp/3.5.4

{
    "status": true,
    "task_id": "e4e62a32-59ce-4f11-ba35-699e03a7cc56"
}
```
