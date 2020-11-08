## Add table with API

```
curl -d '{
  "name":"sample_table",
  "rows":[
    {
      "columns":[
        {
          "name":"column1",
          "value":"data11"
        },
        {
          "name":"column2",
          "value":"data12"
        }
      ]
    },
    {
      "columns":[
        {
          "name":"column1",
          "value":"data21"
        },
        {
          "name":"column2",
          "value":"data22"
        }
      ]
    }
  ]
}' -H "Content-Type: application/json" -X POST http://$CONTAINER_IP:8000/api/tables/
```

## Remove table with API

```
curl -X "DELETE" http://$CONTAINER_IP:8000/api/tables/sample_table/
```

## Build image

```
docker build -t my-image-name .
```

## Run the image and access the app in browser

There are no variables. Access the app or rest api using 8000 port with container ip.
