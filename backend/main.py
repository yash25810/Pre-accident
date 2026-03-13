
# Import FastAPI to create the web application and define API endpoints
from fastapi import FastAPI
# Import AccidentReport model for request validation and data structure
from .models import AccidentReport
# Import utility function to find the nearest hospital based on coordinates
from .utils import get_nearest_hospital

# Initialize the FastAPI application with a custom title
app = FastAPI(title="Smart Accident Alert System")

# Define a POST endpoint '/report-accident' to receive accident reports from the hardware or client
# The endpoint expects a JSON body matching the AccidentReport model
@app.post("/report-accident")
async def report_accident(report: AccidentReport):
    """
    Receives accident data, finds the nearest hospital, and simulates alerting.
    Args:
        report (AccidentReport): Accident data sent from the hardware/client
    Returns:
        dict: Status, message, and nearest hospital info
    """
    # 1. Find the nearest hospital to the reported accident location using latitude and longitude
    hospital, distance = get_nearest_hospital(report.latitude, report.longitude)
    
    # 2. LOGIC: Simulated 'Act' (In production, this would trigger SMS/HTTP alerts)
    print(f"🚨 ALERT RECEIVED for Vehicle: {report.vehicle_id}")  # Log vehicle ID
    print(f"📍 Location: {report.latitude}, {report.longitude}")  # Log accident location
    print(f"🏥 Nearest Hospital: {hospital} ({distance:.2f} km away)")  # Log nearest hospital info
    
    # 3. Respond back to the sender (e.g., hardware or test client) with status and hospital info
    return {
        "status": "Success",  # Indicates the alert was processed
        "message": f"Alert sent to {hospital}",  # Confirmation message
        "data": {
            "hospital": hospital,  # Name of the nearest hospital
            "distance_km": round(distance, 2)  # Distance to the hospital in kilometers (rounded)
        }
    }

# Note:
# - This script acts as the main entry point for the backend FastAPI server.
# - It validates incoming accident data, finds the nearest hospital, and simulates alerting.
# - For real deployment, replace print statements with actual alerting mechanisms (SMS, HTTP, etc.).
# - All logic and variables are explained above for clarity and maintainability.