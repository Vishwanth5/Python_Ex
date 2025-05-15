from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from typing import Optional

app = FastAPI()

# Sample DataFrame for demonstration
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [23, 34, 45, 29, 33],
    "city": ["New York", "Los Angeles", "Chicago", "Miami", "Houston"]
}
df = pd.DataFrame(data)

# Pydantic model for POST request validation
class Person(BaseModel):
    name: str
    age: int
    city: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

# Endpoint 1: Return data as JSON
@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

# Endpoint 2: Filter data by age
@app.get("/filter-by-age")
def filter_by_age(min_age: Optional[int] = 0, max_age: Optional[int] = 100):
    filtered_df = df[(df["age"] >= min_age) & (df["age"] <= max_age)]
    return filtered_df.to_dict(orient="records")

# Endpoint 3: Get a single person's data by name
@app.get("/get-person")
def get_person(name: str):
    person = df[df["name"].str.lower() == name.lower()]
    if person.empty:
        return {"error": "Person not found"}
    return person.to_dict(orient="records")[0]

# POST Endpoint: Add a new person
@app.post("/add-person")
def add_person(person: Person):
    global df
    # Add the new record to the DataFrame
    new_record = pd.DataFrame([person.dict()])
    df = pd.concat([df, new_record], ignore_index=True)
    return {"message": f"Person {person.name} added successfully", "data": person.dict()}

# DELETE Endpoint: Delete a person by name
@app.delete("/delete-person")
def delete_person(name: str):
    global df
    # Remove the person from the DataFrame
    if name in df["name"].values:
        df = df[df["name"].str.lower() != name.lower()]
        return {"message": f"Person {name} deleted successfully"}
    return {"error": "Person not found"}