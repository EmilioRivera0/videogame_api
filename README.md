
# Videogame API

Python developed API that has the CRUD functions and a search engine to interact with a PostgreSQL database containing information about videogames. This API was designed to interact with a Javascript Front-End web page developed by Carlos Cancino Escobar.

# API Reference

#### Get all videogames information

```http
  GET /api/videogames
```

#### Get one or more videogames information

```http
  GET /api/items/{search}
```

| Parameter | Type     | Description                                 |
| :-------- | :------- | :------------------------------------------ |
| `search`  | `string` | **Required**. title/developer to search for |

#### Post a new videogame

```http
  POST /api/videogames
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Required**. Name of the videogame |
| `description` | `string` | **Required**. Description of the videogame |
| `developer` | `string` | **Required**. Developer company |
| `release_year` | `date` | **Required**. Release year |
| `clasification` | `char[2]` | **Required**. clasification |
| `image` | `string` | **Required**. URL of the main videogame image |
| `banner` | `string` | **Required**. URL of the videogame banner |

#### Delete a specified videogame

```http
  DELETE /api/videogames
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | **Required**. ID of the videogame to be removed |

#### Update a specified videogame

```http
  PUT /api/videogames
```

| Parameter | Type     | Description                |
  | :-------- | :------- | :------------------------- |
  | `id` | `integer` | **Required**. ID of the videogame to be modified |
  | `title` | `string` | **Required**. Name of the videogame |
  | `description` | `string` | **Required**. Description of the videogame |
  | `developer` | `string` | **Required**. Developer company |
  | `release_year` | `date` | **Required**. Release year |
  | `clasification` | `char[2]` | **Required**. clasification |
  | `image` | `string` | **Required**. URL of the main videogame image |
  | `banner` | `string` | **Required**. URL of the videogame banner |

# Deployed API

- https://videogame-api-kouw.onrender.com

## Appendix

PostgreSQL database will expire on June 22, 2023

# Tech Stack

**Server:** Flask and PostgreSQL

# Front-End

- https://github.com/C4ncino/videogame_api_client

# Authors

- [@EmilioRivera0](https://github.com/EmilioRivera0)
