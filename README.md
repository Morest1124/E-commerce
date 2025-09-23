# E-commerce API

A Django Rest Framework API for a simple e-commerce platform. It provides endpoints for managing products, categories, and user profiles.

## Features

- Product and Category Management (Create, Read, Update, Delete)
- User Profile Viewing
- Django Admin Interface

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd E-commerce
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv myenv
    .\myenv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
      pip install -r requirements.txt
    ```

4.  **Navigate to the project directory:**
    ```bash
    cd tutorial
    ```

5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create an administrator account:**
    ```bash
    python manage.py createsuperuser
    ```
    You will be prompted to set a username, email, and password.

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints Guide

### Authentication

Some endpoints require authentication. An easy way to test these is to first log in to the Django Admin at `/admin/` in your browser, and then navigate to the API endpoint in a new tab.

---


### Categories

#### List Categories

- **Method:** `GET`
- **URL:** `/api/products/categories/`
- **Description:** Retrieves a list of all product categories.

#### Create Category

- **Method:** `POST`
- **URL:** `/api/products/categories/`
- **Description:** Creates a new product category.
- **Body:**
  ```json
  {
      "name": "New Category Name",
      "slug": "new-category-slug"
  }
  ```
- **Example `curl`:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/products/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Video Games", "slug": "video-games"}'
  ```

#### Manage a Category

- **Method:** `GET`, `PUT`, `PATCH`, `DELETE`
- **URL:** `/api/products/categories/<id>/
- **Description:** Retrieves, updates, or deletes a specific category by its ID.

---


### Products

#### List Products

- **Method:** `GET`
- **URL:** `/api/products/`
- **Description:** Retrieves a list of all products.

#### Create Product

- **Method:** `POST`
- **URL:** `/api/products/`
- **Description:** Creates a new product.
- **Body:**
  ```json
  {
      "category": 1,
      "name": "New Product Name",
      "slug": "new-product-slug",
      "description": "A description of the new product.",
      "price": "99.99"
  }
  ```

#### Manage a Product

- **Method:** `GET`, `PUT`, `PATCH`, `DELETE`
- **URL:** `/api/products/<id>/
- **Description:** Retrieves, updates, or deletes a single product by its ID.

---


### Profiles

#### Manage Your Profile

- **Method:** `GET`, `PUT`, `PATCH`
- **URL:** `/api/profiles/profile/`
- **Authentication:** Required.
- **Description:** Retrieves, creates, or updates the profile information for the currently logged-in user.
- **Body (for `PUT` or `PATCH`):**
  ```json
  {
      "address": "123 New Address St",
      "phone_number": "+1234567890"
  }
  ```


