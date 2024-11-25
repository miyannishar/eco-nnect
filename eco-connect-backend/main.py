from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# router
from report_analysis_and_storage import report_analysis
from eco_agent import eco_agent

app = FastAPI()

# Add all possible origins that might access your API
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://10.0.0.201:3000",
    "http://10.0.0.201:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://10.0.0.201",
    "http://localhost",
    # Add the exact origin that's making the request
    "http://10.0.0.201:3000"
]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    expose_headers=["*"],
    max_age=3600,
)

# including routers
app.include_router(report_analysis.router)
app.include_router(eco_agent.router)