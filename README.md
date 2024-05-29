
# Order CRUD api





## Features

- CREATE
- READ
- UPDATE
- DELETE


## Tech Stack

**Server:** Python, Django, DRF, SQLite


## Installation

Clone the repository:

```bash
  [https://github.com/fahadfoysal/movie-rating](https://github.com/fahadfoysal/order)

```
Install dependencies:
```bash
  pip install -r requirements.txt

``` 
Apply database migrations:

```bash
  python manage.py migrate

```
Run the development server:
```bash
  python manage.py runserver

``` 
## Usage/Examples

```
Access the Django admin panel at http://localhost:8000/admin/

Use the provided APIs for crud


## API Endpoints

- GET: http://localhost:8000/api/orders/ to list all orders.
- POST: http://localhost:8000/api/orders/ to create a new order with JSON payload.
- PUT/PATCH: http://localhost:8000/api/orders/{id}/ to update an order with JSON payload.
- DELETE: http://localhost:8000/api/orders/{id}/ to delete an order.



