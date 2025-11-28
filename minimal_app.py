#!/usr/bin/env python3
"""
Minimal FastAPI app for Railway deployment testing
This helps isolate startup issues
"""

import os
from fastapi import FastAPI
from datetime import datetime

# Create minimal FastAPI app
app = FastAPI(title="AI Fact-Checker API - Minimal")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "status": "online",
        "service": "AI Fact-Checker API",
        "version": "1.0.0",
        "message": "Minimal version running successfully"
    }

@app.get("/health")
async def health_check():
    """Simple health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "port": os.environ.get('PORT', 'unknown'),
        "environment": "railway"
    }

@app.get("/env")
async def check_env():
    """Check environment variables (for debugging)"""
    env_vars = {}
    for key in ['PORT', 'MONGODB_URI', 'REDIS_URL', 'GOOGLE_FACTCHECK_KEY']:
        value = os.environ.get(key)
        env_vars[key] = "SET" if value else "NOT SET"
    
    return {
        "environment_variables": env_vars,
        "total_env_vars": len(os.environ)
    }

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.environ.get('PORT', 8000))
    print(f"🚀 Starting minimal app on port {port}")
    
    uvicorn.run(
        "minimal_app:app",
        host="0.0.0.0",
        port=port,
        log_level="info"
    )