# 🚀 Render Deployment Guide

## Quick Deploy to Render (Complete Setup)

Your app is now fully working locally with Docker! Here's how to deploy it to Render:

### **Step 1: Set Up MongoDB Atlas (Free)**

1. **Create MongoDB Atlas Account**:
   - Go to https://www.mongodb.com/atlas
   - Sign up for free account
   - Verify your email

2. **Create Free Cluster**:
   - Click "Build a Database"
   - Choose "M0 Sandbox" (FREE)
   - Choose your preferred cloud provider & region
   - Cluster Name: `dealership-cluster`

3. **Set Up Database Access**:
   - Go to "Database Access" → "Add New Database User"
   - Username: `dealership`
   - Password: Generate a secure password (save it!)
   - Database User Privileges: "Read and write to any database"

4. **Set Up Network Access**:
   - Go to "Network Access" → "Add IP Address"
   - Choose "Allow Access from Anywhere" (0.0.0.0/0)
   - (For production, you'd restrict this to Render's IPs)

5. **Get Connection String**:
   - Go to "Database" → Click "Connect" on your cluster
   - Choose "Connect your application"
   - Choose "Node.js" and version "4.1 or later"
   - Copy the connection string:
   ```
   mongodb+srv://dealership:<password>@dealership-cluster.xxxxx.mongodb.net/dealershipsDB
   ```
   - Replace `<password>` with your actual password

### **Step 2: Update render.yaml**

Replace the placeholder in `render.yaml` line 33:
```yaml
- key: MONGODB_URL
  value: mongodb+srv://dealership:YOUR_ACTUAL_PASSWORD@dealership-cluster.xxxxx.mongodb.net/dealershipsDB
```

### **Step 3: Deploy to Render**

1. **Go to Render Dashboard**:
   - Visit https://render.com
   - Sign up/login with your GitHub account

2. **Create New Web Service**:
   - Click "New" → "Web Service"
   - Connect your GitHub repository: `xrwvm-fullstack_developer_capstone`
   - Render will detect your `render.yaml` file

3. **Deploy with Blueprint**:
   - Choose "Use Blueprint"
   - Render will create all 3 services automatically:
     - `dealership-django` (main app)
     - `dealership-nodejs` (API)
     - `dealership-sentiment` (AI service)

4. **Monitor Deployment**:
   - Watch the build logs for each service
   - All 3 services should deploy successfully
   - Main app will be available at: `https://dealership-django.onrender.com`

### **Step 4: Import Data to MongoDB Atlas**

Once deployed, you need to populate your MongoDB with data:

1. **Connect to MongoDB Atlas**:
   - Use MongoDB Compass or mongosh
   - Connection string: your Atlas connection string

2. **Import Data**:
   ```bash
   # Import dealers
   mongoimport --uri "your-connection-string" --collection dealerships --file server/database/data/dealerships.json --jsonArray

   # Import reviews  
   mongoimport --uri "your-connection-string" --collection reviews --file server/database/data/reviews.json --jsonArray
   ```

### **Step 5: Test Your Live Application**

Visit your deployed app and test:
- ✅ Homepage loads
- ✅ Dealers page shows 50 dealers
- ✅ Individual dealer pages load
- ✅ Reviews display with sentiment analysis
- ✅ User registration/login works
- ✅ Review posting works (when logged in)

## 🎯 Alternative: Quick Deploy Script

If you prefer, you can use our deployment scripts:

```bash
# Windows
.\deploy-microservices.bat

# Linux/Mac
./deploy-microservices.sh
```

Choose option 1 for Render deployment with guided setup.

## 🔧 Troubleshooting

### Common Issues:

1. **MongoDB Connection Error**:
   - Check your Atlas connection string
   - Ensure IP whitelist includes 0.0.0.0/0
   - Verify username/password

2. **Build Failures**:
   - Check Render build logs
   - Ensure all dependencies are in requirements.txt/package.json

3. **Service Communication**:
   - Verify environment variables in Render dashboard
   - Check service names match in render.yaml

### **Environment Variables to Verify**:

**Django Service**:
- `backend_url`: https://dealership-nodejs.onrender.com
- `sentiment_analyzer_url`: https://dealership-sentiment.onrender.com

**Node.js Service**:
- `MONGODB_URL`: Your Atlas connection string

## 📞 Need Help?

If you encounter issues:
1. Check Render service logs
2. Verify MongoDB Atlas setup
3. Test endpoints individually
4. Review environment variables

Your app is production-ready! 🚀 