# ⚡ Quick Render Deploy

## 🚀 Deploy in 5 Minutes!

### **Step 1: MongoDB Atlas Setup (2 minutes)**
1. Go to https://mongodb.com/atlas → Sign up free
2. Create cluster: M0 Sandbox (free)
3. Database User: `dealership` / `strong-password`
4. Network: Allow 0.0.0.0/0
5. Get connection string: `mongodb+srv://dealership:PASSWORD@cluster.mongodb.net/dealershipsDB`

### **Step 2: Update render.yaml (30 seconds)**
Replace line 33 in `render.yaml`:
```yaml
value: mongodb+srv://dealership:YOUR_PASSWORD@your-cluster.mongodb.net/dealershipsDB
```

### **Step 3: Deploy to Render (2 minutes)**
1. Go to https://render.com → Login with GitHub
2. New → Web Service → Connect `xrwvm-fullstack_developer_capstone`
3. Choose "Use Blueprint" (detects render.yaml)
4. Deploy! 🚀

### **Step 4: Import Data (30 seconds)**
```bash
mongoimport --uri "your-connection-string" --collection dealerships --file server/database/data/dealerships.json --jsonArray
mongoimport --uri "your-connection-string" --collection reviews --file server/database/data/reviews.json --jsonArray
```

### **Your Live URLs:**
- **Main App**: https://dealership-django.onrender.com
- **API**: https://dealership-nodejs.onrender.com
- **Sentiment**: https://dealership-sentiment.onrender.com

## ✅ That's it! Your full-stack app is live! 