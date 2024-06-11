**E-commerce Application**

**Overview**
-----------

This is a comprehensive e-commerce application built using Flask, Flask-SQLAlchemy, and Postman. The application provides CRUD (Create, Read, Update, Delete) endpoints for managing customers, customer accounts, products, and orders.

**Getting Started**
-------------------

1. **Clone the repository**: Clone this repository to your local machine using `git clone`.
2. **Install dependencies**: Install the required dependencies by running `pip install -r requirements.txt`.
3. **Create a database**: Create a MySQL database named `ecommerce` and configure the database connection details in the `config.py` file.
4. **Run the application**: Run the application by executing `python app.py`.
5. **Test the application**: Use Postman to test the application's endpoints. You can find the API documentation in the `postman` folder.

**API Documentation**
--------------------

The API documentation is available in the `postman` folder. The documentation includes detailed information on each endpoint, including request methods, request bodies, and response formats.

**Endpoints**
------------

### Customers

* **Create Customer**: `POST /customers`
	+ Request Body: JSON object with `name`, `email`, and `phone_number` fields
	+ Response: JSON object with a success message
* **Read Customer**: `GET /customers/<int:customer_id>`
	+ Request Parameter: `customer_id` (integer)
	+ Response: JSON object with customer details
* **Update Customer**: `PUT /customers/<int:customer_id>`
	+ Request Body: JSON object with updated customer details
	+ Response: JSON object with a success message
* **Delete Customer**: `DELETE /customers/<int:customer_id>`
	+ Request Parameter: `customer_id` (integer)
	+ Response: JSON object with a success message

### Products

* **Create Product**: `POST /products`
	+ Request Body: JSON object with `name` and `price` fields
	+ Response: JSON object with a success message
* **Read Product**: `GET /products/<int:product_id>`
	+ Request Parameter: `product_id` (integer)
	+ Response: JSON object with product details
* **Update Product**: `PUT /products/<int:product_id>`
	+ Request Body: JSON object with updated product details
	+ Response: JSON object with a success message
* **Delete Product**: `DELETE /products/<int:product_id>`
	+ Request Parameter: `product_id` (integer)
	+ Response: JSON object with a success message

### Orders

* **Place Order**: `POST /orders`
	+ Request Body: JSON object with order details (including product IDs and quantities)
	+ Response: JSON object with an order ID and order details
* **Read Order**: `GET /orders/<int:order_id>`
	+ Request Parameter: `order_id` (integer)
	+ Response: JSON object with order details
* **Track Order**: `GET /orders/<int:order_id>/track`
	+ Request Parameter: `order_id` (integer)
	+ Response: JSON object with order tracking information

### Bonus Features

* **View and Manage Product Stock Levels**: `GET /products/<int:product_id>/stock`
	+ Request Parameter: `product_id` (integer)
	+ Response: JSON object with product stock levels
* **Restock Products When Low**: N/A (this feature is implemented automatically)
* **Manage Order History**: `GET /orders/<int:customer_id>/history`
	+ Request Parameter: `customer_id` (integer)
	+ Response: JSON object with order history
* **Cancel Order**: `POST /orders/<int:order_id>/cancel`
	+ Request Parameter: `order_id` (integer)
	+ Response: JSON object with a success message
* **Calculate Order Total Price**: N/A (this feature is implemented automatically)