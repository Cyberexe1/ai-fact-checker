# 🔍 AI Fact-Checker

**An intelligent, multi-agent system for automated fact-checking using AI, authoritative sources, and web evidence.**

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen.svg)](https://www.mongodb.com/cloud/atlas)
[![Redis](https://img.shields.io/badge/Redis-Queue-red.svg)](https://redis.io/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

AI Fact-Checker is a production-ready system that automatically verifies claims through an 8-agent pipeline:

1. **Classify Agent** - Detects input type (text/URL/image)
2. **Extract Agent** - Extracts claims from various sources
3. **Format Agent** - Normalizes text with NLP
4. **Fact-Check Agent** - Queries authoritative fact-checking APIs
5. **Identify Agent** - Determines verification strategy
6. **Search Agent** - Collects web evidence
7. **Summarize Agent** - AI-powered analysis with confidence scoring
8. **Report Agent** - Generates professional HTML/PDF reports

### Key Capabilities

✅ **Multi-Input Support**: Text, URLs, and images (OCR)  
✅ **Authoritative Sources**: Google Fact Check API integration  
✅ **AI Analysis**: LLM-powered summarization (OpenRouter/OpenAI/Gemini)  
✅ **Web Interface**: Beautiful chatbot with real-time processing  
✅ **Professional Reports**: Automated HTML/PDF generation  
✅ **Production Ready**: Error handling, fallbacks, and monitoring  

---

## ✨ Features

### Input Processing
- **Text Claims**: Direct input with intelligent parsing
- **URL Processing**: Multi-method article extraction (newspaper3k, BeautifulSoup, Playwright)
- **Image Processing**: OCR.space integration for text extraction

### Verification System
- **Authoritative Fact-Checking**: Google Fact Check API with semantic matching
- **Web Evidence Collection**: Intelligent search with reliability scoring
- **Trusted Source Database**: Pre-configured reliability scores (Reuters 95%, FactCheck.org 98%, etc.)

### AI Analysis
- **Multi-Provider LLM**: OpenRouter, OpenAI, or Gemini support
- **Confidence Calculation**: Formula-based scoring with LLM validation
- **Hallucination Detection**: Validates LLM-cited sources

### Report Generation
- **HTML Reports**: Always generated (Windows compatible)
- **PDF Reports**: Generated when WeasyPrint available
- **Comprehensive Sections**: All evidence, sources, and methodology included

---

## 💻 System Requirements

### Required
- **Python**: 3.11 or 3.12 (⚠️ **NOT 3.13** - has MongoDB SSL issues)
- **Memory**: 4GB RAM minimum, 8GB recommended
- **Storage**: 2GB free space
- **Internet**: Required for API calls

### Operating Systems
- ✅ Windows 10/11
- ✅ macOS
- ✅ Linux

---

## 🚀 Installation

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd ai-fact-checker
```

### Step 2: Install Python Dependencies

```bash
# Use Python 3.11 if you have multiple versions
py -3.11 -m pip install -r requirements.txt

# Or on macOS/Linux
python3.11 -m pip install -r requirements.txt
```

### Step 3: Install NLP Model

```bash
py -3.11 -m spacy download en_core_web_sm
```

### Step 4: Install Playwright Browsers

```bash
py -3.11 -m playwright install chromium
```

### Step 5: Set Up MongoDB

**Option A: MongoDB Atlas (Recommended)**
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create free account and cluster
3. Create database user
4. Get connection string
5. Whitelist your IP (or use 0.0.0.0/0 for testing)

**Option B: Local MongoDB**
1. Download from [mongodb.com](https://www.mongodb.com/try/download/community)
2. Install and start MongoDB service
3. Use connection string: `mongodb://localhost:27017/`

### Step 6: Set Up Redis

**Option A: Redis Cloud (Recommended)**
1. Go to [Redis Cloud](https://redis.com/try-free/)
2. Create free account and database
3. Get connection string

**Option B: Local Redis**
1. Download from [redis.io](https://redis.io/download)
2. Install and start Redis service
3. Use connection string: `redis://localhost:6379`

### Step 7: Get API Keys

#### Google Fact Check Tools API (Required)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project or select existing
3. Enable "Fact Check Tools API"
4. Create credentials → API key
5. Copy API key

**Free Tier**: 1,000 requests/day

#### OCR.space API (Required for Images)
1. Go to [OCR.space](https://ocr.space/ocrapi)
2. Sign up for free account
3. Get API key from dashboard
4. Copy API key

**Free Tier**: 25,000 requests/month

#### OpenRouter API (Recommended for LLM)
1. Go to [OpenRouter](https://openrouter.ai/)
2. Sign up and get API key
3. Copy API key

**Free Models Available**: Several options with daily limits

#### SerpAPI (Optional - Better Search)
1. Go to [SerpAPI](https://serpapi.com/)
2. Sign up for account
3. Get API key

**Free Tier**: 100 searches/month

---

## ⚙️ Configuration

### Step 1: Create Environment File

```bash
# Copy example configuration
cp .env.example .env

# Edit with your settings
notepad .env  # Windows
nano .env     # macOS/Linux
```

### Step 2: Configure Environment Variables

Edit `.env` file with your settings:

```env
# MongoDB Configuration
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=false
MONGODB_DB=factchecker

# Redis Configuration
REDIS_URL=redis://:password@redis-server:port

# API Keys
GOOGLE_FACTCHECK_KEY=your_google_factcheck_key_here
OCR_SPACE_KEY=your_ocr_space_key_here
SERPAPI_KEY=your_serpapi_key_here  # Optional

# LLM Configuration (Choose one)
OPENROUTER_API_KEY=your_openrouter_key_here
OPENROUTER_MODEL=openai/gpt-4o-mini:free

# OR use OpenAI
# OPENAI_API_KEY=your_openai_key_here

# OR use Gemini
# GEMINI_API_KEY=your_gemini_key_here

# Storage Configuration
STORAGE_MODE=local
LOCAL_STORAGE_PATH=./storage

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
```

### Step 3: Test Connections

```bash
# Test MongoDB connection
py -3.11 -c "from app.database import test_connection; test_connection()"

# Test Redis connection
py -3.11 test_redis_connection.py

# Test LLM connection
py -3.11 test_free_llm.py
```

**Expected Output**:
```
✅ MongoDB connection successful!
✅ Redis connection successful!
✅ LLM connection successful!
```

---

## 🎮 Running the Application

You need to run **3 services** in separate terminal windows:

### Terminal 1: Start Worker

```bash
py -3.11 -m app.worker
```

**Expected Output**:
```
============================================================
🚀 Starting Custom Worker (Windows Compatible)
============================================================
📡 Redis: redis://:password@redis-server...
📋 Queues: default, high, low
============================================================

✓ Worker started successfully
✓ Listening for jobs...
```

### Terminal 2: Start API Server

```bash
py -3.11 -m uvicorn app.main:app --reload
```

**Expected Output**:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Terminal 3: Start Frontend

```bash
cd frontend
py -3.11 serve.py
```

**Expected Output**:
```
Server running at: http://localhost:3001
Press Ctrl+C to stop the server
```

### Access the Application

- **Web Interface**: http://localhost:3001
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

---

## 📱 Usage

### Web Interface (Recommended)

1. **Open Browser**: Navigate to http://localhost:3001
2. **Submit Claim**: Type text, paste URL, or upload image
3. **Wait for Processing**: Takes 45-60 seconds
4. **View Results**: See confidence score and explanation
5. **Download Report**: Click download button for full report

#### Input Examples

**Text Claims**:
```
COVID vaccines contain microchips
Government announces new policy
Study shows coffee prevents cancer
```

**URLs**:
```
https://www.bbc.com/news/health-12345678
https://www.reuters.com/article/...
https://www.factcheck.org/...
```

**Images**:
- Click paperclip icon (📎)
- Select image file (PNG, JPG, etc.)
- Click send to process

#### Understanding Results

**Confidence Levels**:
- 🟢 **High (70-100%)**: Strong evidence, reliable sources
- 🟡 **Medium (40-70%)**: Some evidence, mixed sources
- 🔴 **Low (0-40%)**: Weak evidence, unreliable sources

### API Usage

See [POSTMAN_API_GUIDE.md](POSTMAN_API_GUIDE.md) for detailed API documentation.

#### Quick API Examples

**Submit Text Claim**:
```bash
curl -X POST http://localhost:8000/check \
  -F "text=COVID vaccines contain microchips"
```

**Submit URL**:
```bash
curl -X POST http://localhost:8000/check \
  -F "url=https://www.bbc.com/news/health-12345678"
```

**Submit Image**:
```bash
curl -X POST http://localhost:8000/check \
  -F "file=@image.png"
```

**Get Results**:
```bash
curl http://localhost:8000/result/{submission_id}
```

**Download Report**:
```bash
curl http://localhost:8000/report/{submission_id} --output report.html
```

---

## 📡 API Documentation

### Endpoints

#### GET /health
System health check

**Response**:
```json
{
    "status": "healthy",
    "database": "connected",
    "storage": "local",
    "timestamp": "2025-11-20T12:00:00.000000"
}
```

#### POST /check
Submit claim for fact-checking

**Parameters**:
- `text` (string): Plain text claim
- `url` (string): URL to article
- `file` (file): Image file for OCR

**Response**:
```json
{
    "submission_id": "691f326087526dc3df693362",
    "status": "queued",
    "estimated_time": 60
}
```

#### GET /result/{submission_id}
Get fact-checking result

**Response**:
```json
{
    "status": "completed",
    "claim": "COVID vaccines contain microchips",
    "confidence": 0.6624,
    "explanation": "The claim is false...",
    "report_url": "./storage/reports/report_xxx.html"
}
```

#### GET /report/{submission_id}
Download HTML/PDF report

**Response**: Binary file (HTML or PDF)

For complete API documentation with Postman collection, see [POSTMAN_API_GUIDE.md](POSTMAN_API_GUIDE.md)

---

## 📁 Project Structure

```
ai-fact-checker/
├── app/
│   ├── agents/              # 8 Agent implementations
│   │   ├── classify.py      # Agent 1: Input classification
│   │   ├── extract.py       # Agent 2: Claim extraction
│   │   ├── format.py        # Agent 3: Text normalization
│   │   ├── factcheck.py     # Agent 4: Authoritative fact-checking
│   │   ├── identify.py      # Agent 5: Verification strategy
│   │   ├── search.py        # Agent 6: Web evidence collection
│   │   ├── summarize.py     # Agent 7: AI analysis
│   │   └── report.py        # Agent 8: Report generation
│   ├── config.py            # Configuration management
│   ├── database.py          # MongoDB operations
│   ├── llm_client.py        # LLM integration
│   ├── main.py              # FastAPI application
│   ├── models.py            # Data models
│   ├── orchestrator.py      # Agent coordination
│   ├── storage.py           # File storage
│   └── worker.py            # Background worker
├── frontend/
│   ├── index.html           # Web interface
│   ├── script.js            # Frontend logic
│   ├── style.css            # Styling
│   └── serve.py             # Development server
├── storage/
│   └── reports/             # Generated reports
├── templates/
│   └── report_template.html # Report template
├── .env                     # Environment variables (create from .env.example)
├── .env.example             # Example configuration
├── requirements.txt         # Python dependencies
├── README.md                # This file
├── POSTMAN_API_GUIDE.md     # API documentation
└── FINAL_PROJECT_DOCUMENTATION.md  # Complete documentation
```

---

## 🐛 Troubleshooting

### MongoDB Connection Failed

**Error**: `SSL handshake failed`

**Solution**: Use Python 3.11 or 3.12 (NOT 3.13)

```bash
# Check Python version
python --version

# If 3.13, install 3.11 from python.org
# Then use:
py -3.11 -m pip install -r requirements.txt
```

### Worker Not Processing Jobs

**Error**: `SIGALRM attribute error`

**Solution**: Already fixed with custom worker implementation

**Verify**:
```bash
py -3.11 -m app.worker
# Should show: ✓ Worker started successfully
```

### Frontend Connection Refused

**Error**: `Fetch error: Connection refused`

**Solution**: Ensure API server is running

```bash
# Check API health
curl http://localhost:8000/health

# Start API if not running
py -3.11 -m uvicorn app.main:app --reload
```

### No Fact-Checks Found

**Error**: `fact_checks_count: 0`

**Solutions**:
1. Check `GOOGLE_FACTCHECK_KEY` in `.env`
2. Verify API key is valid
3. Check API quotas (1,000/day free)
4. Test API manually:
```bash
curl "https://factchecktools.googleapis.com/v1alpha1/claims:search?query=COVID&key=YOUR_KEY"
```

### URL Extraction Fails

**Error**: `Unable to extract content from URL`

**How URL Extractor Works**:

The system uses a **3-tier fallback approach** to extract article content from URLs:

**Method 1: newspaper3k (Primary)**
- Fast, specialized article extraction library
- Automatically identifies article content, title, authors, publish date
- Uses custom browser headers to avoid 403 errors
- Best for news sites and blogs

**Method 2: BeautifulSoup (Fallback)**
- Direct HTTP request with browser-like headers
- Tries common article selectors (article, main, .article-content, etc.)
- Removes navigation, scripts, ads automatically
- Works for most standard websites

**Method 3: Playwright (Last Resort)**
- Full browser automation with JavaScript rendering
- Waits for dynamic content to load
- Executes JavaScript to extract article text
- Best for JavaScript-heavy sites (React, Vue, etc.)

**Solutions if extraction fails**:
1. Check if URL is accessible in browser
2. Some sites block automated access (403/429 errors)
3. Try copying article text directly instead
4. Verify Playwright is installed: `py -3.11 -m playwright install chromium`

**Supported Sites**:
- ✅ News sites (BBC, Reuters, CNN, etc.)
- ✅ Fact-checking sites (FactCheck.org, Snopes, etc.)
- ✅ Blogs and articles
- ✅ Most public websites
- ❌ Paywalled content
- ❌ Sites with aggressive bot protection

### OCR Not Working

**Error**: `OCR extraction failed`

**Solutions**:
1. Check `OCR_SPACE_KEY` in `.env`
2. Verify image format (PNG, JPG, JPEG, BMP, GIF)
3. Check file size (<1MB for free tier)
4. Verify API quotas (25,000/month free)

### LLM Analysis Fails

**Error**: `LLM call failed`

**Solutions**:
1. Check LLM API key in `.env`
2. Verify model name is correct
3. Check API credits/quota
4. System uses fallback rule-based analysis

### PDF Generation Fails

**Error**: `cannot load library 'libgobject-2.0-0'`

**Solution**: This is normal on Windows - HTML reports work perfectly

For PDF support:
- Use Docker with Linux
- Install system libraries
- HTML reports contain all the same information

### Port Already in Use

**Error**: `Address already in use`

**Solutions**:

```bash
# Windows - Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux - Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

---

## 📊 Performance Metrics

### Processing Times

| Component | Typical Time | Max Time |
|-----------|--------------|----------|
| Complete Pipeline | 35-60s | 120s |
| Text Extraction | 1-2s | 5s |
| URL Extraction | 2-5s | 10s |
| Image OCR | 3-6s | 15s |
| Fact-Checking | 5-10s | 20s |
| Web Search | 20-30s | 60s |
| AI Analysis | 5-10s | 30s |
| Report Generation | 2-5s | 10s |

### Resource Usage

| Resource | Typical | Peak |
|----------|---------|------|
| Memory (Worker) | 200MB | 500MB |
| Memory (API) | 100MB | 200MB |
| CPU | 30-50% | 80% |
| Disk per Report | 1MB | 5MB |

---

## 📚 Additional Documentation

- **[POSTMAN_API_GUIDE.md](POSTMAN_API_GUIDE.md)** - Complete API documentation with Postman collection
- **[FINAL_PROJECT_DOCUMENTATION.md](FINAL_PROJECT_DOCUMENTATION.md)** - Comprehensive technical documentation
- **[QUICK_START.md](QUICK_START.md)** - Quick start guide
- **[MONGODB_FIX.md](MONGODB_FIX.md)** - MongoDB troubleshooting

---

## 🎉 Success Checklist

Before using the system, verify:

- ✅ Python 3.11 or 3.12 installed
- ✅ All dependencies installed (`pip install -r requirements.txt`)
- ✅ spaCy model downloaded
- ✅ Playwright browsers installed
- ✅ MongoDB connected (test with `test_connection()`)
- ✅ Redis connected (test with `test_redis_connection.py`)
- ✅ API keys configured in `.env`
- ✅ Worker running (Terminal 1)
- ✅ API server running (Terminal 2)
- ✅ Frontend running (Terminal 3)
- ✅ Can access http://localhost:3001

---

## 🚀 Quick Start Summary

```bash
# 1. Install dependencies
py -3.11 -m pip install -r requirements.txt
py -3.11 -m spacy download en_core_web_sm
py -3.11 -m playwright install chromium

# 2. Configure environment
cp .env.example .env
# Edit .env with your API keys

# 3. Start services (3 terminals)
# Terminal 1
py -3.11 -m app.worker

# Terminal 2
py -3.11 -m uvicorn app.main:app --reload

# Terminal 3
cd frontend && py -3.11 serve.py

# 4. Open browser
# http://localhost:3001
```

---

## 📞 Support

For issues and questions:
1. Check [Troubleshooting](#troubleshooting) section
2. Review [FINAL_PROJECT_DOCUMENTATION.md](FINAL_PROJECT_DOCUMENTATION.md)
3. Check API documentation in [POSTMAN_API_GUIDE.md](POSTMAN_API_GUIDE.md)

---

**Version**: 1.0.0  
**Status**: Production Ready ✅  
**Last Updated**: November 20, 2025

**Built with ❤️ using Python, FastAPI, MongoDB, Redis, and AI**
