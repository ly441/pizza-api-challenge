# Pizza API Challenge

A RESTful API for managing restaurants, pizzas, and their relationships, built with Flask, SQLAlchemy, and PostgreSQL.

## Features

- CRUD operations for Restaurants, Pizzas, and RestaurantPizzas
- PostgreSQL database integration
- Flask-Migrate for database migrations
- Seed script for sample data
- Environment variable support via `.env`
- Modular structure using Flask Blueprints

## Project Structure

```
pizza-api-challenge/
├── server/
│   ├── app.py
│   ├── db/
│   │   ├── config.py
│   │   └── database.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_controller.py
│   ├── models/
│   │   ├── pizza.py
│   │   ├── restaurant.py
│   │   └── restaurant_pizza.py
│   ├── seed.py
│   └── set_up.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```sh
git clone <repo-url>
cd pizza-api-challenge
```

### 2. Create and activate a virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with the following (edit as needed):

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/pizza_db
SECRET_KEY=your-secret-key
DEBUG=True
```

### 5. Set up the database

- Create the database in PostgreSQL:
  ```sh
  psql -U postgres -h localhost
  CREATE DATABASE pizza_db;
  ```

- Run migrations:
  ```sh
  export FLASK_APP=server/app.py
  flask db init         # Only if not already initialized
  flask db migrate -m "Initial migration"
  flask db upgrade
  ```

### 6. Seed the database (optional)

```sh
python -m server.seed
```

### 7. Run the application

```sh
python server/app.py
```

The API will be available at `http://localhost:5555/`.

## API Endpoints

### Restaurants

- `GET /restaurants` — List all restaurants
- `GET /restaurants/<id>` — Get a specific restaurant
- `POST /restaurants` — Create a new restaurant
- `PUT /restaurants/<id>` — Update a restaurant
- `DELETE /restaurants/<id>` — Delete a restaurant

### Pizzas

- `GET /pizzas` — List all pizzas
- `GET /pizzas/<id>` — Get a specific pizza
- `POST /pizzas` — Create a new pizza
- `PUT /pizzas/<id>` — Update a pizza
- `DELETE /pizzas/<id>` — Delete a pizza

### RestaurantPizzas

- `GET /restaurant_pizzas` — List all restaurant-pizza relationships
- `GET /restaurant_pizzas/<id>` — Get a specific relationship
- `POST /restaurant_pizzas` — Create a new relationship
- `PUT /restaurant_pizzas/<id>` — Update a relationship
- `DELETE /restaurant_pizzas/<id>` — Delete a relationship

## Development

- Use `flask db migrate` and `flask db upgrade` to manage schema changes.
- Use `python -m server.seed` to reset and seed the database.
# Pizza Restaurant API

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=server/app.py
flask db upgrade
python server/seed.py
flask run --port=5555

## License

MIT
