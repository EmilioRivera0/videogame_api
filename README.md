
# Videogame API

Python developed API that has the CRUD functions and a search engine to interact with a PostgreSQL database containing information about videogames. This API was designed to interact with a Javascript Front-End web page developed by Carlos Cancino Escobar.

## API Reference

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

# Deployed API

- https://videogame-api-kouw.onrender.com

## Tech Stack

**Server:** Flask and PostgreSQL

# Authors

- [@EmilioRivera0](https://github.com/EmilioRivera0)
