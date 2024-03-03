from fastapi import FastAPI
from typing import List, Dict
import json

app = FastAPI()

# Function to load data from JSON file
def load_data(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Generic function to calculate the proportion of data based on a given key
def calculate_proportions(data: List[Dict[str, str]], key: str) -> Dict[str, float]:
    count_by_key = {}
    total_count_by_key = {}

    for item in data:
        value = item[key]
        osteoporosis = int(item["Osteoporosis"])

        if value not in count_by_key:
            count_by_key[value] = 0
            total_count_by_key[value] = 0

        total_count_by_key[value] += 1
        if osteoporosis:
            count_by_key[value] += 1
    
    # Calculate proportion of data for each key value
    proportions = {}
    for value, total_count in total_count_by_key.items():
        count = count_by_key[value]
        if total_count > 0:
            proportions[value] = count / total_count
        else:
            proportions[value] = 0

    return proportions

# Path to JSON file
json_file_path = "../data/osteoporosis.json"

# Load data from JSON file
data = load_data(json_file_path)

@app.get("/")
async def read_root():
    return {"message": "API for osteoporosis data analysis"}


@app.get("/patients/average_age")
async def get_average_age():
    total_age = sum(int(patient["Age"]) for patient in data)
    average_age = total_age / len(data)
    return {"average_age": average_age}

@app.get("/patients/race_ethnicity_risk")
async def get_race_ethnicity_risk():
    return {"race_ethnicity_risk": calculate_proportions(data, "Race/Ethnicity")}

@app.get("/patients/gender_risk")
async def get_gender_risk():
    return {"gender_risk": calculate_proportions(data, "Gender")}

@app.get("/patients/body_weight")
async def get_body_weight(): 
    return {"body_weight": calculate_proportions(data, 'Body Weight')}

@app.get("/patients/calcium_intake")
async def get_body_weight(): 
    return {"calcium_intake": calculate_proportions(data, 'Calcium Intake')}

@app.get("/patients/physical_activity")
async def get_body_weight(): 
    return {"physical_activity": calculate_proportions(data, 'Physical Activity')}


@app.get("/patients/", response_model=List[Dict[str, str]])
async def get_patients():
    return data

@app.get("/patients/{patient_id}", response_model=Dict[str, str])
async def get_patient(patient_id: str):
    for patient in data:
        if patient["Id"] == patient_id:
            return patient
    return {"error": "Patient not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
