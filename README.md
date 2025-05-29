# FastAPI Redis Microservices

Microservices backend using **FastAPI**, **RedisJSON** for persistence, and **Redis Streams** for event-driven communication.

This project includes the following services:

- 📦 **Inventory Service** – Manage product data (name, price, quantity)
- 💳 **Payment Service** – Process purchases with markup and order tracking
- 📊 **Analytics Service** – Track product sales, revenue, and popularity (integrated into the codebase)
- 💾 **RedisJSON** – Structured storage for products and orders
- 🔁 **Redis Streams** – Async, event-driven communication between services

This project **does not include a frontend** and is focused entirely on backend logic and architecture.

---

## 🧪 API Documentation

You can test all available endpoints using the included Postman collection.

### 👉 [Postman Collection: FastAPI Microservices](FastAPI%20Microservices.postman_collection.json)

---

## 🚀 API Endpoints by Service

### 📦 Inventory Service (Port: `8001`)

| Method | Endpoint                                 | Description                  |
|--------|------------------------------------------|------------------------------|
| GET    | `/api/v1/products`                       | Get all products             |
| GET    | `/api/v1/products/{product_id}`          | Get product by ID            |
| POST   | `/api/v1/products`                       | Create a new product         |
| DELETE | `/products/{product_id}`                 | Delete a product by ID       |

---

### 💳 Payment Service (Port: `8002`)

| Method | Endpoint                    | Description            |
|--------|-----------------------------|------------------------|
| GET    | `/api/v1/orders`            | List all orders        |
| POST   | `/api/v1/orders`            | Create a new order     |
| GET    | `/api/v1/orders/{order_id}` | Get order by ID *(TBD)* |

---

### 📊 Analytics Service (Port: `8003`)

| Method | Endpoint                                      | Description                           |
|--------|-----------------------------------------------|---------------------------------------|
| POST   | `/api/v1/analytics/update`                    | Update analytics (called on order)    |
| GET    | `/api/v1/analytics/sales`                     | Get product-wise sales volume         |
| GET    | `/api/v1/analytics/revenue`                   | Get total revenue generated           |
| GET    | `/api/v1/analytics/popular-products?limit=N`  | Get top N popular products by sales   |

---

## 🛠 Getting Started

Make sure Redis is installed and running with RedisJSON and Redis Streams support.

Run each microservice in a separate terminal:

```bash
# Inventory Service
fastapi run inventory:app --port 8001 --reload

# Payment Service

fastapi run payment:app --port 8002 --reload

# Analytics Service
fastapi run analytics:app --port 8003 --reload
```
