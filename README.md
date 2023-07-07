# Product CRUD rest api

## Product table

| feild | type | description |
| --- | --- | --- |
| id | int | product id |
| name | string | product name |
| price | int | product price |
| quantity | int | product quantity |
| description | string | product description |
| created_at | datetime | product created time |
| updated_at | datetime | product updated time |

## Endpoints

| method | path | description |
| --- | --- | --- |
| GET | /api/products | get all products |
| GET | /api/products/{id} | get product by id |
| POST | /api/products | create new product |
| PUT | /api/products/{id} | update product by id |
| DELETE | /api/products/{id} | delete product by id |
