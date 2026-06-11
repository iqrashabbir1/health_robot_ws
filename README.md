Health Robot Assistant System

This is a simple project where I built a basic client-server system
using FastAPI and Python to simulate a healthcare robot assistant.

The idea is to show how a robot or assistant system can receive requests
from a user and respond based on simple logic.

What this project does

-   A server runs using FastAPI
-   A client sends a request (like a patient asking for help)
-   The server processes the request
-   The system updates and returns a response

Simple idea behind it

Think of it like this:

-   Client = Patient or user
-   Server = Robot assistant system
-   Communication = HTTP requests

The client sends a message like “I need help”, and the server responds
with a status update.

Project structure

health_robot_ws/ client/ server/ myenv/

How to run

Step 1: Activate environment source myenv/bin/activate

Step 2: Run server uvicorn server.server:app –reload

Step 3: Run client python client/client.py

API endpoints

/health -> checks if server is running /patient/{patient_id} -> shows
patient status /assist -> sends help request

What I learned

-   Client-server communication
-   FastAPI basics
-   JSON data exchange
-   Basic system design for robotics/healthcare

Author: Iqra Shabbir
