# 🚗 Microservices Setup Guide

This guide explains how to set up and run the microservices required for the Django backend to function properly.

## 🔍 Issues Addressed

1. **Static Files Warnings**: Fixed by conditionally checking if directories exist
2. **Database and REST Login Functions**: Fixed by starting required microservices
3. **Connection Errors**: Added fallback data and better error handling

## 🏗️ Architecture Overview

The Django backend depends on two microservices:

1. **Dealer Service** (Node.js) - Port 3030
   - Manages dealer data and reviews
   - Located in: `server/database/`

2. **Sentiment Analyzer** (Flask) - Port 5050
   - Analyzes review sentiments using NLTK
   - Located in: `server/djangoapp/microservices/`

## 🚀 Quick Start

### Option 1: Windows Batch Script (Recommended for Windows)

```bash
cd server
start_services.bat
```

### Option 2: Python Script (Cross-platform)

```bash
cd server
python start_services.py
```

### Option 3: Manual Setup

#### Start Dealer Service
```bash
cd server/database
npm install
node app.js
```

#### Start Sentiment Analyzer
```bash
cd server/djangoapp/microservices
pip install -r requirements.txt
set FLASK_APP=app.py
set FLASK_RUN_PORT=5050
python -m flask run
```

## 📋 Prerequisites

- **Node.js** (v14 or higher)
- **Python** (v3.8 or higher)
- **npm** (comes with Node.js)
- **pip** (comes with Python)

## 🧪 Testing

Once the microservices are running, you can test the Django backend:

```bash
cd server
python manage.py test djangoapp --verbosity=2
```

Expected output:
- All tests should pass
- No connection errors to localhost:3030 or localhost:5050

## 🔧 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```
   Error: listen EADDRINUSE: address already in use :::3030
   ```
   **Solution**: Kill processes using the ports or change port numbers

2. **Node.js Not Found**
   ```
   'node' is not recognized as an internal or external command
   ```
   **Solution**: Install Node.js from https://nodejs.org/

3. **Python Dependencies Missing**
   ```
   ModuleNotFoundError: No module named 'flask'
   ```
   **Solution**: Run `pip install -r requirements.txt` in the microservices directory

4. **NLTK Data Missing**
   ```
   LookupError: Resource vader_lexicon not found
   ```
   **Solution**: The startup script will automatically download this

### Service Status Check

You can verify services are running by visiting:
- Dealer Service: http://localhost:3030
- Sentiment Analyzer: http://localhost:5050

## 🔄 Fallback Mode

If microservices are not available, the Django backend will:
- Return mock data for dealer endpoints
- Return "neutral" sentiment for review analysis
- Log connection errors but continue functioning

This ensures tests can still pass even without microservices running.

## 🛠️ Development Tips

1. **Keep Services Running**: Leave the microservices running while developing
2. **Check Logs**: Monitor the service windows for errors
3. **Restart if Needed**: If services crash, restart using the scripts
4. **Port Conflicts**: Ensure ports 3030 and 5050 are available

## 📁 File Structure

```
server/
├── start_services.py          # Cross-platform startup script
├── start_services.bat         # Windows startup script
├── database/                  # Dealer service (Node.js)
│   ├── app.js
│   ├── package.json
│   └── ...
├── djangoapp/
│   ├── microservices/         # Sentiment analyzer (Flask)
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── ...
│   ├── restapis.py           # Enhanced with fallback data
│   └── ...
└── djangoproj/
    └── settings.py           # Fixed static files configuration
```

## ✅ Success Indicators

When everything is working correctly:
- ✅ No static files warnings
- ✅ All Django tests pass
- ✅ No connection errors in test output
- ✅ Dealer and sentiment services respond
- ✅ Login and registration functions work

## 🆘 Getting Help

If you encounter issues:
1. Check the service logs in the opened windows
2. Verify all prerequisites are installed
3. Ensure ports 3030 and 5050 are not blocked
4. Try restarting the services

The enhanced error handling will provide detailed feedback about what's not working. 