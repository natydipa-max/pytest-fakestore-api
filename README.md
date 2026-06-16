# Pytest Fake Store API Framework

## Overview

This project is an API testing framework built with Pytest and Requests against the Fake Store API.

It focuses on:

* CRUD automation
* API client abstraction
* Model validation using Pydantic
* Exploratory testing and behavior documentation

---

## Tech Stack

* Python
* Pytest
* Requests
* Pydantic

---

## Architecture

The framework is structured in layers:

* **Clients layer**: Handles HTTP communication (`BaseClient`, `ProductsClient`)
* **Models layer**: Defines request/response schemas using Pydantic
* **Tests layer**: Validates API behavior and contracts

---

## API Coverage

### Products Endpoint

The framework covers full CRUD operations:

* GET /products
* GET /products/{id}
* POST /products
* PUT /products/{id}
* DELETE /products/{id}

---

## Exploratory Testing Findings

During exploratory testing of the Fake Store API, the following behaviors were observed.

### GET /products/{id}

Requests with invalid identifiers such as:

* `/products/AB`
* `/products/@abc`

return:

* HTTP 200 OK
* Empty response body

This behavior causes `response.json()` in Python Requests to raise a `JSONDecodeError`.

---

### POST /products

The API accepts:

* Missing required fields
* Empty strings
* Invalid data types
* Negative numeric values

Example:

```json
{
  "price": "a10"
}
```

Response:

* HTTP 201 Created

No business validation errors are returned.

---

### JSON Parsing Validation

The API returns HTTP 400 Bad Request only when the request body contains malformed JSON syntax.

Example (invalid JSON sent intentionally to trigger 400):

Payload:
{"price": 39,87}

---

### PUT /products/{id}

PUT requests behave similarly to POST:

* Accept invalid business data
* Accept missing fields
* Only fail on malformed JSON payloads

---

## Negative Testing Strategy

Negative tests are limited to malformed JSON scenarios because:

* The API does not implement business validation
* Only JSON parsing errors return HTTP 400

Example tests:

* POST malformed JSON → 400
* PUT malformed JSON → 400

---

## Key Design Decisions

* ProductClient only handles valid business operations
* Malformed JSON tests bypass the client layer intentionally
* Pydantic is used only for valid request/response modeling
* Exploratory findings are documented rather than assumed

---

## Conclusion

This framework demonstrates:

* API automation best practices
* Separation between business validation and protocol validation
* Exploratory testing applied to real API behavior
* Model-driven validation using Pydantic
