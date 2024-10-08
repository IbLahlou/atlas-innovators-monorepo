# Django Backend for Atlas Innovators (v1)

## Overview
This guide outlines the API endpoints and data structures for the Django Family Project. As a frontend engineer, you'll be interacting with these endpoints to create and retrieve family records.



## Features

- Create Parent and Child records

- Uses Factory pattern for object creation

- PostgreSQL database integration

## Prerequisites

- Python 3.8 or higher

- Git

- PostgreSQL

## Setup

1. Clone the repository:

   ```

   git clone https://github.com/IbLahlou/atlas-innovator-backend-ild.git

   cd atlas-innovator-backend-ild

   ```

2. Create and activate a virtual environment:

   ```

   python -m venv venv

   source venv/bin/activate  # On Windows, use venv\Scripts\activate

   ```

3. Install dependencies:

   ```

   pip install -r requirements.txt

   ```

4. Configure PostgreSQL database in settings.py

5. Run migrations: python manage.py migrate

6. Create superuser: python manage.py createsuperuser


## API Endpoints

### 1. Create Family
- **URL:** `/create_family/`
- **Method:** POST
- **Data Params:**
  ```json
  {
    "parent": {
      "first_name": "string",
      "last_name": "string",
      "age": integer
    },
    "child": {
      "first_name": "string",
      "last_name": "string",
      "age": integer,
      "score": integer,
      "level": integer
    }
  }
  ```
- **Success Response:**
  - **Code:** 201
  - **Content:** `{ "message": "Family created successfully", "parent_id": integer, "child_id": integer }`

### 2. Get Family
- **URL:** `/family/<int:parent_id>/`
- **Method:** GET
- **Success Response:**
  - **Code:** 200
  - **Content:** 
    ```json
    {
      "parent": {
        "id": integer,
        "first_name": "string",
        "last_name": "string",
        "age": integer,
        "child_id": integer
      },
      "child": {
        "id": integer,
        "first_name": "string",
        "last_name": "string",
        "age": integer,
        "score": integer,
        "level": integer
      }
    }
    ```

## Data Models

### Parent
- id: Integer
- first_name: String
- last_name: String
- age: Integer
- child_id: Integer (Foreign Key to Child)

### Child
- id: Integer
- first_name: String
- last_name: String
- age: Integer
- score: Integer
- level: Integer
- parent_id: Integer (Foreign Key to Parent)

## Implementation Notes
1. Use a state management solution (e.g., Redux, MobX) to store family data fetched from the API.
2. Implement form validation on the frontend before sending data to the API.
3. Handle API errors gracefully and display user-friendly error messages.
4. Consider implementing a loading state while waiting for API responses.

## Example API Usage (JavaScript)
```javascript
// Creating a family
async function createFamily(parentData, childData) {
  const response = await fetch('/create_family/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ parent: parentData, child: childData }),
  });
  return response.json();
}

// Fetching a family
async function getFamily(parentId) {
  const response = await fetch(`/family/${parentId}/`);
  return response.json();
}
```

## Next Steps
1. Implement a user interface for creating and viewing families.
2. Add error handling and loading states in your frontend application.
3. Consider adding authentication to protect these endpoints.
