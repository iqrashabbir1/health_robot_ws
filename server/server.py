from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Health Robot Assistant System")

# patient/robot state simulation
system_state = {
    "patient_01": {
        "heart_rate": 78,
        "status": "stable"
    }
}

class Request(BaseModel):
    patient_id: str
    message: str


@app.get("/health")
def health():
    return {"system": "running", "type": "healthcare_robot_system"}


@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    return system_state.get(patient_id, {"error": "not found"})


@app.post("/assist")
def assist(data: Request):

    if data.patient_id not in system_state:
        return {"error": "patient not found"}

    # simple rule-based logic (important for PhD foundation)
    if "help" in data.message.lower():
        system_state[data.patient_id]["status"] = "alert"

    return {
        "patient_id": data.patient_id,
        "message_received": data.message,
        "status": system_state[data.patient_id]["status"],
        "action": "notified_caregiver"
    }