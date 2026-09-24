# Doctor and Patient Management System

# Description
Simple REST API using FastAPI for managing doctors and patients.

# Technologies Used
- Python
- FastAPI
- Pydantic
- Uvicorn

# Doctor APIs
- POST /doctors
- GET /doctors
- GET /doctors/{doctor_id}

# Patient APIs
- POST /patients
- GET /patients

# Validation
- Email must be valid
- Patient age must be greater than 0

##Installation
pip install -r requirements.txt

# Run
uvicorn main:app --reload

# Swagger Documentation
http://127.0.0.1:8000/docs

## Example Doctor Request

{
    "name": "Dr. Swami",
    "specialization": "Cardiology",
    "email": "swami@example.com",
    "is_active": true
}

## Example Patient Request

{
    "name": "nandu",
    "age": 23,
    "phone": "6302969760"
}


# Error Handling
If a doctor ID does not exist, the API returns a 404 error.
{
    "detail": "doctor not found"
}

