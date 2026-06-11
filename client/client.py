import requests

BASE_URL = "http://127.0.0.1:8000"

payload = {
    "patient_id": "patient_01",
    "message": "I need help"
}

# send assistance request
res = requests.post(f"{BASE_URL}/assist", json=payload)
print("Assist Response:", res.json())

# check patient status
res2 = requests.get(f"{BASE_URL}/patient/patient_01")
print("Patient State:", res2.json())