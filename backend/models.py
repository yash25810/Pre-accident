
# Importing BaseModel from pydantic to define data validation and serialization logic for API models
from pydantic import BaseModel
# Importing datetime to handle timestamp fields
from datetime import datetime
# Importing Optional to allow fields to be optional or have default values
from typing import Optional

# AccidentReport class defines the structure of the accident data received from the hardware or client
# Inherits from BaseModel to leverage Pydantic's data validation and parsing features
class AccidentReport(BaseModel):
    vehicle_id: str  # Unique identifier for the vehicle involved in the accident
    g_force: float  # The measured G-force at the time of the accident (used to detect collision severity)
    latitude: float  # Latitude coordinate where the accident occurred (from GPS)
    longitude: float  # Longitude coordinate where the accident occurred (from GPS)
    vehicle_type: str  # Type of vehicle, e.g., "two-wheeler" or "car" (used for analytics and alert logic)
    timestamp: datetime = datetime.now()  # Timestamp of when the accident was reported (defaults to current time)
    severity: Optional[str] = "Pending Analysis"  # Severity of the accident, initially set to 'Pending Analysis' until processed

# Note:
# - This model is used for request validation in FastAPI endpoints.
# - The timestamp defaults to the current time if not provided.
# - The severity field can be updated after further analysis.
# - All fields are explained above for clarity and maintainability.