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
}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/tables/
```

## Remove table with API

```
curl -X "DELETE" http://127.0.0.1:8000/api/tables/sample_table/
```

## Build image

```
docker build -t my-image-name .
```
