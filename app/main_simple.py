from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from datetime import datetime
import os

# Create FastAPI app
app = FastAPI(
    title="AI Fact-Checker API",
    description="8-Agent fact-checking system",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    print("🚀 Starting AI Fact-Checker API...")
    print("✅ API ready!")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "status": "online",
        "service": "AI Fact-Checker",
        "version": "1.0.0",
        "message": "Welcome to the AI Fact-Checking System"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    try:
        # Test basic functionality
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "port": os.environ.get('PORT', 'unknown'),
            "environment": "railway"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }

@app.get("/env")
async def check_env():
    """Check environment variables"""
    env_vars = {}
    for key in ['PORT', 'MONGODB_URI', 'REDIS_URL', 'GOOGLE_FACTCHECK_KEY', 'OCR_SPACE_KEY', 'OPENROUTER_API_KEY']:
        value = os.environ.get(key)
        env_vars[key] = "SET" if value else "NOT SET"
    
    return {
        "environment_variables": env_vars,
        "total_env_vars": len(os.environ)
    }

@app.post("/check")
async def check_claim_placeholder():
    """Placeholder for fact-checking endpoint"""
    return {
        "message": "Fact-checking endpoint - coming soon!",
        "status": "not_implemented"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run("app.main_simple:app", host="0.0.0.0", port=port)