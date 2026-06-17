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

This is not an application error, but a behavior of the API returning an empty response body with HTTP 200.
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

Example of an invalid JSON (causes HTTP 400 due to parsing failure):

```text
{"price": 39,87}
```
This is not a business validation error, but a JSON parsing error handled by the server before request processing.

---

### PUT /products/{id}

PUT requests behave similarly to POST:

* Accept invalid business data
* Accept missing fields
* Only fail on malformed JSON payloads

---

## Testing Strategy

All API tests in this framework follow a consistent 3-step validation approach:

### 1. Status Code Validation
Each test first asserts the HTTP status code to validate the correctness of the API response at the protocol level.

### 2. Schema Validation (when applicable)
If the response contains a body, it is validated using Pydantic models to ensure the response structure matches the expected schema.

### 3. Business Rules Validation
When applicable, tests assert business logic based on the API response data (e.g., field values, relationships, or state changes).

This approach ensures a clear separation between:
- HTTP protocol validation
- Data contract validation
- Business logic validation

---

## Negative Testing Strategy

Negative tests focus on malformed JSON scenarios due to lack of business validation in the API.

* The API does not implement business validation
* Only JSON parsing errors return HTTP 400

Example tests:

* POST malformed JSON → 400
* PUT malformed JSON → 400

---

## Key Design Decisions

* ProductClient provides a thin abstraction over HTTP operations for the Products endpoint.
  Business validation is not enforced at client level.
* Malformed JSON tests bypass the client layer intentionally
* Pydantic is used only for valid request/response modeling
* Exploratory findings are documented rather than assumed

---

## CI Execution

GitHub Actions integration was evaluated during development.

Execution against Fake Store API currently receives HTTP 403 responses from GitHub-hosted runners, preventing reliable CI execution.

Since this behavior is external to the framework implementation, CI configuration was intentionally excluded from this repository.

---

## Conclusion

This framework demonstrates:

* API automation best practices
* Separation between business validation and protocol validation
* Exploratory testing applied to real API behavior
* Model-driven validation using Pydantic
