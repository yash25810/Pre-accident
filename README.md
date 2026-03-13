
# Smart Accident Alert System

Welcome to the Smart Accident Alert System! This project is designed to provide rapid, automated accident detection and emergency alerting using a combination of hardware sensors, microcontrollers, and a robust Python backend. The system aims to save lives by instantly notifying the nearest hospital, police, and emergency contacts when a severe accident is detected.

**Key Features:**
- Real-time accident detection using G-force and tilt sensors (MPU6050) on vehicles.
- GPS-based location tracking (NEO-6M) for precise accident site reporting.
- Automated SMS/HTTP alerts sent via SIM800L and backend FastAPI server.
- Dynamic lookup of the nearest hospital using live APIs.
- Modular backend for easy integration, logging, and future AI-based analysis.

This repository contains all backend code, documentation, and sample data required to deploy and extend the system. Whether you are a developer, researcher, or emergency response professional, you will find this project easy to understand, customize, and contribute to.

---

================================================================================
                    SMART ACCIDENT ALERT SYSTEM WORKFLOW
================================================================================

[ VEHICLE SIDE - HARDWARE ] (Offline / Cellular)
------------------------------------------------
       
   +-----------------------+          +--------------------------+
   |   MPU6050 SENSOR      |          |    NEO-6M GPS MODULE     |
   | (Accel + Gyroscope)   |          | (Satellites Connection)   |
   +-----------+-----------+          +------------+-------------+
               |                                   |
               | [G-Force / Tilt Data]             | [Lat / Long Coordinates]
               v                                   v
   +-----------+-----------------------------------+-------------+
   |                        ESP32 BOARD                          |
   |           (The Brain - Runs Collision Algorithm)            |
   |                                                             |
   |  LOGIC: IF (G-Force > 5G) AND (Tilt > 60°) AND (No Cancel)  |
   +----------------------------+--------------------------------+
                                |
                                | [Trigger Command]
                                v
                   +------------+------------+
                   |     SIM800L MODULE      |
                   |  (Sends SMS via 2G/GSM) |
                   +------------+------------+
                                |
                                |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ CLOUD SIDE - BACKEND ] (Online / Internet)    | [SMS Data Packet]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                |
                                v
                   +------------+------------+
                   |      SMS GATEWAY        |
                   | (Receives SMS & Forwards)|
                   +------------+------------+
                                |
                                | [HTTP POST]
                                v
                   +------------+------------+      +-----------------------+
                   |  FASTAPI PYTHON SERVER  |----->|  SQLITE / POSTGRES    |
                   |                         |      |    (Database Storage) |
                   |   (Processing Engine)   |      | (Log for AI Training) |
                   +------------+------------+      +-----------------------+
                                |
          +---------------------+---------------------+
          |                     |                     |
          v                     v                     v
+-------------------+ +-------------------+ +-------------------------+
|  NEAREST HOSPITAL | | POLICE CONTROL ROOM| |    EMERGENCY CONTACT    |
| (Based on the     | |  (City Records)    | |    (Family Member)      |
| location)         | | [Accident Log]     | | [Google Maps Location]  |
+-------------------+ +-------------------+ +-------------------------+

================================================================================


# Project workflow & architecture:

## Project Structure Overview

Below is a concise description of each file and folder in this project:

- **backend/**: Contains all backend server logic, API endpoints, models, and utilities.
  - **main.py**: Main FastAPI server entry point. Handles accident report API, processes incoming data, and triggers alert logic.
  - **models.py**: Defines the Pydantic data models (e.g., AccidentReport) for request validation and data structure.
  - **utils.py**: Utility functions, including dynamic nearest hospital lookup using LOCATION_API.
  - **__pycache__/**: Python bytecode cache (auto-generated).
- **documentations/**: Folder for documenting all changes, features, and file/folder updates in the project.
- **hospitals.CSV**: Sample dataset of hospitals with name, category, location, and coordinates (used for reference/testing).
- **requirements.txt**: Lists all Python dependencies and libraries required for the backend.
- **README.md**: Project overview, setup guide, structure, and workflow documentation (this file).

## Architectural Flow (ASCII Diagram)

```
┌─────────────────────────────┐
│        VEHICLE SIDE        │
└────────────┬───────────────┘
         │
   [Sensor Data: G-Force, Tilt, GPS]
         │
      ┌────▼────┐
      │  ESP32  │
      └────┬────┘
         │
   [Trigger Accident Alert]
         │
      ┌────▼────┐
      │ SIM800L │
      └────┬────┘
         │
   [SMS Data Packet]
         │
      ┌────▼────┐
      │ SMS GW  │
      └────┬────┘
         │
   [HTTP POST to Backend]
         │
      ┌────▼────┐
      │ FastAPI │
      │ Server  │
      └────┬────┘
         │
   [Process, Find Nearest Hospital]
         │
      ┌────▼────┐
      │ DB/API  │
      └────┬────┘
         │
   [Alert: Hospital, Police, Family]
```

---
