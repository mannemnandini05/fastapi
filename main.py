from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title="Doctor and Patient API",
    description="API for managing doctor and patient records",
    version="1.0.0"
)

doctors = []
patients = []


class Doctor(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str


@app.post("/doctors")
def create_doctor(doctor: Doctor):

    new_doctor = {
        "id": len(doctors) + 1,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "email": doctor.email,
        "is_active": doctor.is_active
    }

    doctors.append(new_doctor)

    return {
        "message": "Doctor information added successfully",
        "doctor": new_doctor
    }


@app.get("/doctors")
def get_doctors():

    return doctors


@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):

    for doctor in doctors:

        if doctor["id"] == doctor_id:
            return doctor

    raise HTTPException(
        status_code=404,
        detail="Requested doctor was not found"
    )


@app.post("/patients")
def create_patient(patient: Patient):

    new_patient = {
        "id": len(patients) + 1,
        "name": patient.name,
        "age": patient.age,
        "phone": patient.phone
    }

    patients.append(new_patient)

    return {
        "message": "Patient details saved successfully",
        "patient": new_patient
    }


@app.get("/patients")
def get_patients():

    return patients


@app.get("/")
def home():

    return {
        "message": "Doctor and Patient service is up and running"
    }