#!/usr/bin/env python3
"""
Railway startup script for AI Fact-Checker
Handles environment setup and graceful startup
"""

import os
import sys
import time
from app.config import settings

def check_environment():
    """Check if all required environment variables are set"""
    required_vars = [
        'MONGODB_URI',
        'REDIS_URL',
        'GOOGLE_FACTCHECK_KEY'
    ]
    
    missing = []
    for var in required_vars:
        if not getattr(settings, var.lower().replace('_', '_'), None):
            missing.append(var)
    
    if missing:
        print(f"❌ Missing environment variables: {', '.join(missing)}")
        return False
    
    print("✅ All required environment variables are set")
    return True

def test_connections():
    """Test database and Redis connections"""
    try:
        from app.database import test_connection
        if not test_connection():
            print("❌ MongoDB connection failed")
            return False
        print("✅ MongoDB connection successful")
    except Exception as e:
        print(f"❌ MongoDB connection error: {e}")
        return False
    
    try:
        import redis
        redis_conn = redis.from_url(settings.redis_url)
        redis_conn.ping()
        print("✅ Redis connection successful")
    except Exception as e:
        print(f"❌ Redis connection error: {e}")
        return False
    
    return True

def start_server():
    """Start the FastAPI server"""
    import uvicorn
    
    print("🚀 Starting AI Fact-Checker API...")
    
    # Get port from environment (Railway sets this)
    port = int(os.environ.get('PORT', 8000))
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        log_level="info"
    )

if __name__ == "__main__":
    print("=" * 60)
    print("🔍 AI Fact-Checker - Railway Deployment")
    print("=" * 60)
    
    # Check environment
    if not check_environment():
        print("❌ Environment check failed")
        sys.exit(1)
    
    # Test connections with retry
    max_retries = 3
    for attempt in range(max_retries):
        if test_connections():
            break
        
        if attempt < max_retries - 1:
            print(f"⚠️  Connection test failed, retrying in 5 seconds... ({attempt + 1}/{max_retries})")
            time.sleep(5)
        else:
            print("❌ Connection tests failed after all retries")
            sys.exit(1)
    
    # Start server
    start_server()