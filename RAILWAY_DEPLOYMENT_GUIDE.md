# 🚀 Railway Deployment Guide - AI Fact-Checker API

**Deploy your complete 8-agent fact-checking API system to Railway for FREE**

---

## 📋 Prerequisites

Before starting, ensure you have:
- ✅ GitHub account
- ✅ Railway account (free)
- ✅ MongoDB Atlas account (free)
- ✅ API keys ready (Google Fact Check, OCR.space, OpenRouter)

## 📁 Required Files in Your Project

Your project folder should contain these essential files:

```
ai-fact-checker/
├── app/                           # Main application code
│   ├── agents/                   # All 8 agent implementations
│   │   ├── classify.py          # Agent 1: Input classification
│   │   ├── extract.py           # Agent 2: Claim extraction
│   │   ├── format.py            # Agent 3: Text formatting
│   │   ├── factcheck.py         # Agent 4: Authoritative fact-checking
│   │   ├── identify.py          # Agent 5: Verification strategy
│   │   ├── search.py            # Agent 6: Web evidence search
│   │   ├── summarize.py         # Agent 7: AI summarization
│   │   └── report.py            # Agent 8: Report generation
│   ├── data/
│   │   └── narrative_templates.json  # Report templates data
│   ├── config.py                # Configuration management
│   ├── database.py              # MongoDB operations
│   ├── llm_client.py            # LLM integration
│   ├── main.py                  # FastAPI application
│   ├── orchestrator.py          # Agent coordination
│   ├── storage.py               # File storage
│   └── worker.py                # Background worker
├── templates/                    # HTML report templates
│   └── report_template.html     # Main report template
├── .env.example                  # Environment variables template
├── requirements.txt              # Python dependencies
├── Procfile                     # Railway process configuration ✨
├── railway.json                 # Railway deployment settings ✨
└── runtime.txt                  # Python version specification ✨
```

**✨ Files created for Railway deployment**:
- `Procfile` - Defines web and worker processes
- `railway.json` - Railway-specific deployment configuration
- `runtime.txt` - Specifies Python version
- `templates/report_template.html` - HTML report template
- `requirements-minimal.txt` - Lightweight dependencies for Railway
- `.dockerignore` - Excludes heavy files from build

**Files NOT needed for deployment**:
- ❌ `frontend/` folder (remove entirely)
- ❌ `test_*.py` files (optional, can remove)
- ❌ `*_TEST_*.md` files (optional, can remove)
- ❌ `.env` file (use Railway environment variables instead)

---

## 🎯 Step 1: Prepare Your Repository

### 1.1 Create GitHub Repository

```bash
# If not already done, initialize git in your project
git init
git add .
git commit -m "Initial commit: AI Fact-Checker"

# Create repository on GitHub and push
git remote add origin https://github.com/yourusername/ai-fact-checker.git
git branch -M main
git push -u origin main
```

### 1.2 Create Required Deployment Files

Create these files in your project root:

**File 1: `Procfile`**
```
web: python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
worker: python -m app.worker
```

**File 2: `railway.json`**
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT",
    "healthcheckPath": "/health",
    "healthcheckTimeout": 100,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

**File 3: `runtime.txt`**
```
python-3.11.9
```

### 1.3 Clean Up Project (Remove Frontend)

**Remove unnecessary files for API-only deployment**:
```bash
# Remove frontend folder entirely
rm -rf frontend/

# Remove test files (optional)
rm -f test_*.py
rm -f *_TEST_*.md
rm -f URL_EXTRACTOR_TEST_REPORT.md

# Keep only essential files
```

### 1.4 Optimize for Railway's 4GB Limit

**Problem**: Your current `requirements.txt` creates an 8.8GB image (too large for free tier)

**Solution**: Use lightweight dependencies

**Replace your `requirements.txt` with `requirements-minimal.txt`**:
```bash
# Rename current requirements
mv requirements.txt requirements-full.txt

# Use minimal requirements for Railway
mv requirements-minimal.txt requirements.txt
```

**What's removed to save space**:
- ❌ `playwright` (1.5GB) - Use newspaper3k + BeautifulSoup only
- ❌ `spacy` + models (800MB) - Use basic text processing
- ❌ `weasyprint` (500MB) - HTML reports only (no PDF)
- ❌ `sentence-transformers` (400MB) - Use basic similarity
- ❌ Heavy ML libraries

**What's kept (lightweight)**:
- ✅ FastAPI + uvicorn (web server)
- ✅ MongoDB + Redis (databases)
- ✅ newspaper3k + BeautifulSoup (web scraping)
- ✅ Basic NLP and search
- ✅ HTML report generation

---

## 🎯 Step 2: Set Up External Services

### 2.1 MongoDB Atlas (Database)

1. **Go to MongoDB Atlas**: https://cloud.mongodb.com/
2. **Create Account** (if not done)
3. **Create Free Cluster**:
   - Choose "M0 Sandbox" (Free)
   - Select region closest to you
   - Name: `factchecker-cluster`
4. **Create Database User**:
   - Database Access → Add New Database User
   - Username: `factchecker`
   - Password: Generate secure password
   - Role: `Atlas Admin`
5. **Whitelist IP Addresses**:
   - Network Access → Add IP Address
   - Add: `0.0.0.0/0` (Allow access from anywhere)
   - **Note**: For production, use specific IPs
6. **Get Connection String**:
   - Clusters → Connect → Connect your application
   - Copy connection string
   - Replace `<password>` with your database password

**Example Connection String**:
```
mongodb+srv://factchecker:<password>@factchecker-cluster.abc123.mongodb.net/?retryWrites=true&w=majority
```

### 2.2 Get API Keys

**Google Fact Check Tools API**:
1. Go to: https://console.cloud.google.com/
2. Create new project: `ai-fact-checker`
3. Enable "Fact Check Tools API"
4. Create credentials → API key
5. Copy API key

**OCR.space API**:
1. Go to: https://ocr.space/ocrapi
2. Sign up for free account
3. Get API key from dashboard
4. Copy API key

**OpenRouter API** (for LLM):
1. Go to: https://openrouter.ai/
2. Sign up and get API key
3. Copy API key

---

## 🎯 Step 3: Deploy to Railway

### 3.1 Create Railway Account

1. **Go to Railway**: https://railway.app/
2. **Sign up** with GitHub account
3. **Verify email** if required

### 3.2 Create New Project

1. **Click "New Project"**
2. **Select "Deploy from GitHub repo"**
3. **Connect GitHub** (if not connected)
4. **Select your repository**: `ai-fact-checker`
5. **Click "Deploy Now"**

### 3.3 Configure Services

Railway will create one service. You need to add a worker service:

1. **Add Worker Service**:
   - Click "+" → "Empty Service"
   - Name: `worker`
   - Source: Same GitHub repo
   - Start Command: `python -m app.worker`

2. **Add Redis Service**:
   - Click "+" → "Database" → "Redis"
   - Railway will provision Redis automatically

### 3.4 Set Environment Variables

For **both services** (web and worker), add these environment variables:

**In Railway Dashboard → Service → Variables**:

```bash
# MongoDB Configuration
MONGODB_URI=mongodb+srv://factchecker:<password>@factchecker-cluster.abc123.mongodb.net/?retryWrites=true&w=majority
MONGODB_DB=factchecker

# Redis Configuration (Railway provides this automatically)
REDIS_URL=${{Redis.REDIS_URL}}

# API Keys
GOOGLE_FACTCHECK_KEY=your_google_factcheck_key_here
OCR_SPACE_KEY=your_ocr_space_key_here
OPENROUTER_API_KEY=your_openrouter_key_here
OPENROUTER_MODEL=openai/gpt-4o-mini:free

# Storage Configuration
STORAGE_MODE=local
LOCAL_STORAGE_PATH=./storage

# API Configuration
API_HOST=0.0.0.0
API_PORT=$PORT
DEBUG=False
```

**Important Notes**:
- Replace `<password>` in MongoDB URI with your actual password
- Replace API keys with your actual keys
- `${{Redis.REDIS_URL}}` automatically uses Railway's Redis
- `$PORT` is automatically provided by Railway

---

## 🎯 Step 4: Deploy and Test

### 4.1 Deploy Services

1. **Push to GitHub**:
```bash
git add .
git commit -m "Add Railway deployment files"
git push origin main
```

2. **Railway Auto-Deploy**:
   - Railway detects changes and deploys automatically
   - Watch deployment logs in Railway dashboard
   - Wait for both services to show "Active"

### 4.2 Install Dependencies

Railway will automatically:
1. Detect Python project
2. Install requirements.txt
3. Download spaCy model (if in requirements)
4. Start services

### 4.3 Get Your API URL

1. **In Railway Dashboard**:
   - Go to your web service
   - Click "Settings" → "Domains"
   - Copy the generated URL (e.g., `https://your-app.railway.app`)

---

## 🎯 Step 5: Test Your Deployment

### 5.1 Health Check

Test if your API is running:
```bash
curl https://your-app.railway.app/health
```

**Expected Response**:
```json
{
    "status": "healthy",
    "database": "connected",
    "storage": "local",
    "timestamp": "2025-11-29T12:00:00.000000"
}
```

### 5.2 Test Fact-Checking

**Submit a claim**:
```bash
curl -X POST https://your-app.railway.app/check \
  -F "text=COVID vaccines contain microchips"
```

**Expected Response**:
```json
{
    "submission_id": "507f1f77bcf86cd799439011",
    "status": "queued",
    "estimated_time": 60
}
```

**Get results**:
```bash
curl https://your-app.railway.app/result/507f1f77bcf86cd799439011
```

### 5.3 Test All Endpoints

**Available API Endpoints**:
- `GET /` - Welcome message
- `GET /health` - System health check
- `POST /check` - Submit claim (text/url/file)
- `GET /result/{id}` - Get fact-checking results
- `GET /report/{id}` - Download HTML report
- `GET /docs` - Interactive API documentation

**API Documentation**:
Visit: `https://your-app.railway.app/docs` for interactive testing

---

## 🎯 Step 6: Monitor and Maintain

### 6.1 Monitor Usage

**Railway Dashboard**:
- **Metrics**: CPU, Memory, Network usage
- **Logs**: Real-time application logs
- **Deployments**: Deployment history
- **Usage**: Credit consumption

### 6.2 Check Logs

**View Logs**:
1. Railway Dashboard → Service → "Logs"
2. Filter by service (web/worker)
3. Monitor for errors

**Common Log Messages**:
```
✅ MongoDB connection successful
✅ Redis connection established
✅ All 8 Agents Complete!
⚠️  LLM call failed: Check API key
❌ MongoDB connection failed: Check connection string
```

### 6.3 Scale if Needed

**Free Tier Limits**:
- **Memory**: 512MB per service
- **CPU**: Shared
- **Bandwidth**: 100GB/month
- **Credit**: $5/month

**If you exceed limits**:
- Upgrade to Pro plan ($5/month per service)
- Optimize code for better performance
- Use external services (Redis Cloud, etc.)

---

## 🎯 Step 7: Troubleshooting

### 7.1 Common Issues

**Issue 1: Service Won't Start**
```
Error: Module not found
```
**Solution**: Check requirements.txt includes all dependencies

**Issue 2: MongoDB Connection Failed**
```
Error: ServerSelectionTimeoutError
```
**Solution**: 
- Check MongoDB URI is correct
- Verify IP whitelist includes 0.0.0.0/0
- Ensure MongoDB cluster is not paused

**Issue 3: Build Image Too Large (8.8GB > 4GB)**
```
Error: Image size exceeded limit
```
**Solution**: 
- Use `requirements-minimal.txt` instead of `requirements.txt`
- Remove heavy dependencies (Playwright, spaCy, WeasyPrint)
- Add `.dockerignore` to exclude unnecessary files

**Issue 4: Health Check Failing (Service Unavailable)**
```
Error: 1/1 replicas never became healthy!
Attempt #X failed with service unavailable
```

**This means the app is crashing before it can respond to health checks.**

**Debugging Steps**:

1. **Check Railway Logs**:
   - Go to Railway Dashboard → Your Service → "Logs"
   - Look for Python errors, import failures, or crashes

2. **Test with Minimal App**:
   ```bash
   # Temporarily use minimal app to test Railway setup
   mv requirements.txt requirements-full.txt
   mv requirements-test.txt requirements.txt
   
   # Update Procfile
   echo "web: python minimal_app.py" > Procfile
   
   # Commit and push
   git add . && git commit -m "Test minimal app" && git push
   ```

3. **Common Causes**:
   - **Missing environment variables** (MongoDB URI, Redis URL, API keys)
   - **Import errors** (missing dependencies)
   - **Database connection failures** (MongoDB Atlas paused/unreachable)
   - **Port binding issues** (app not listening on $PORT)

4. **Check Environment Variables**:
   - Railway Dashboard → Service → "Variables"
   - Ensure all required variables are set:
     - `MONGODB_URI`
     - `REDIS_URL` 
     - `GOOGLE_FACTCHECK_KEY`
     - `OCR_SPACE_KEY`
     - `OPENROUTER_API_KEY`

5. **Test Endpoints** (once minimal app works):
   - `GET /health` - Should return 200 OK
   - `GET /env` - Shows which environment variables are set

**Issue 4: Worker Not Processing Jobs**
```
Error: Redis connection failed
```
**Solution**: 
- Verify Redis service is running
- Check REDIS_URL environment variable
- Restart worker service

**Issue 4: API Keys Not Working**
```
Error: 401 Unauthorized
```
**Solution**:
- Verify API keys are correct
- Check environment variables are set
- Test API keys manually

### 7.2 Debug Commands

**Check Environment Variables**:
```bash
# In Railway service logs, you'll see:
✅ MongoDB URI: mongodb+srv://...
✅ Redis URL: redis://...
✅ API Keys: SET/NOT SET
```

**Test Individual Components**:
```bash
# Test MongoDB
curl https://your-app.railway.app/health

# Test specific agent
curl -X POST https://your-app.railway.app/check -F "text=test claim"
```

---

## 🎯 Step 8: Production Optimization

### 8.1 Performance Improvements

**Add to requirements.txt**:
```
gunicorn==21.2.0
```

**Update Procfile**:
```
web: gunicorn app.main:app -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
worker: python -m app.worker
```

### 8.2 Security Enhancements

**Environment Variables**:
```bash
# Add security settings
ALLOWED_HOSTS=your-app.railway.app
CORS_ORIGINS=https://your-frontend-domain.com
DEBUG=False
```

### 8.3 Monitoring Setup

**Add Health Checks**:
- Railway automatically monitors `/health` endpoint
- Set up alerts for service downtime
- Monitor credit usage

---

## 🎉 Success Checklist

Before going live, verify:

- ✅ Both services (web + worker) are "Active"
- ✅ Health check returns 200 OK
- ✅ Can submit claims via API
- ✅ Worker processes jobs successfully
- ✅ All 8 agents execute properly
- ✅ Reports are generated
- ✅ API documentation accessible
- ✅ Environment variables set correctly
- ✅ MongoDB connection working
- ✅ Redis connection working
- ✅ API keys valid and working

---

## 📞 Support Resources

**Railway Documentation**: https://docs.railway.app/
**MongoDB Atlas Docs**: https://docs.atlas.mongodb.com/
**API Documentation**: `https://your-app.railway.app/docs`

**Common URLs After Deployment**:
- **API Base**: `https://your-app.railway.app`
- **Health Check**: `https://your-app.railway.app/health`
- **API Docs**: `https://your-app.railway.app/docs`
- **Submit Claim**: `POST https://your-app.railway.app/check`

---

## 💡 Next Steps

1. **Custom Domain**: Add your own domain in Railway settings
2. **API Integration**: Use your API in mobile apps, websites, or other services
3. **Monitoring**: Set up external monitoring (UptimeRobot, etc.)
4. **Scaling**: Monitor usage and upgrade if needed
5. **Security**: Implement rate limiting and authentication
6. **Documentation**: Share your API docs with users

---

## 🔗 Using Your Deployed API

**Base URL**: `https://your-app.railway.app`

**Example API Calls**:
```bash
# Check a text claim
curl -X POST https://your-app.railway.app/check \
  -F "text=COVID vaccines are safe and effective"

# Check a URL
curl -X POST https://your-app.railway.app/check \
  -F "url=https://www.bbc.com/news/health-12345678"

# Get results
curl https://your-app.railway.app/result/SUBMISSION_ID

# Download report
curl https://your-app.railway.app/report/SUBMISSION_ID -o report.html
```

---

**🎯 Your AI Fact-Checker API is now live and accessible worldwide!**

**Estimated Setup Time**: 20-30 minutes  
**Monthly Cost**: $0 (within free limits)  
**Scalability**: Handles 100s of API requests/day on free tier  
**Access**: Public API endpoints for integration anywhere
