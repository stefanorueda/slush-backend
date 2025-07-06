# File: backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Dict

app = FastAPI()

class SplitRequest(BaseModel):
    total: float = Field(..., gt=0, description="Total bill amount")
    splits: Dict[str, float] = Field(..., description="Mapping of participant names to amounts")

@app.post("/validate-split")
def validate_split(data: SplitRequest):
    total_split = sum(data.splits.values())
    if round(total_split, 2) != round(data.total, 2):
        return {
            "valid": False,
            "message": f"Split does not match total ({total_split} ≠ {data.total})"
        }
    return {
        "valid": True,
        "message": "Split is valid"
    }