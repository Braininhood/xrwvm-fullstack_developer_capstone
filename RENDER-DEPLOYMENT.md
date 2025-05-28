# 🎨 Render Deployment Guide

## 🚀 Quick Deployment Steps

### **Step 1: Prepare Your Repository**
Your repository is already configured with:
- ✅ `Dockerfile` in root (for Django backend)
- ✅ `render.yaml` configuration file
- ✅ Production-ready settings

### **Step 2: Deploy to Render**

1. **Go to [render.com](https://render.com)**
2. **Sign up/Login** with your GitHub account
3. **Connect Repository**:
   - Click "New +"
   - Select "Blueprint"
   - Connect your GitHub repository: `xrwvm-fullstack_developer_capstone`
   - Render will automatically detect the `render.yaml` file

4. **Review Configuration**:
   - Service Name: `dealership-backend`
   - Environment: `Docker`
   - Health Check: `/djangoapp/get_dealers/`
   - Database: PostgreSQL (automatically created)

5. **Deploy**:
   - Click "Apply"
   - Render will build and deploy your application
   - Wait for deployment to complete (5-10 minutes)

### **Step 3: Access Your Application**

Your app will be available at:
```
https://dealership-backend.onrender.com
```

Test the API endpoints:
- **Dealers**: `https://dealership-backend.onrender.com/djangoapp/get_dealers/`
- **Cars**: `https://dealership-backend.onrender.com/djangoapp/get_cars`

## 🔧 **Alternative: Manual Service Creation**

If the Blueprint doesn't work, create services manually:

### **Django Backend Service**
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - **Name**: `dealership-backend`
   - **Environment**: `Docker`
   - **Build Command**: (leave empty - Docker handles this)
   - **Start Command**: (leave empty - Docker handles this)
   - **Health Check Path**: `/djangoapp/get_dealers/`

### **Environment Variables**
Add these in the Render dashboard:
```
DJANGO_SETTINGS_MODULE=djangoproj.settings
PYTHONUNBUFFERED=1
```

### **Database Setup**
1. Click "New +" → "PostgreSQL"
2. Configure:
   - **Name**: `dealership-db`
   - **Database Name**: `dealership`
   - **User**: `dealership_user`
3. Connect to your web service

## 🐳 **Docker Configuration**

The root `Dockerfile` is configured to:
- ✅ Use Python 3.12 slim image
- ✅ Install all dependencies
- ✅ Copy Django project
- ✅ Collect static files
- ✅ Run with Gunicorn (production server)
- ✅ Health checks enabled
- ✅ Security: non-root user

## 🔍 **Troubleshooting**

### **Common Issues:**

1. **Build Fails**:
   - Check that `server/requirements.txt` exists
   - Verify all dependencies are listed

2. **Health Check Fails**:
   - Wait for full startup (Django takes time)
   - Check logs in Render dashboard

3. **Database Connection**:
   - Ensure PostgreSQL database is created
   - Check environment variables

### **Viewing Logs**:
1. Go to your service in Render dashboard
2. Click "Logs" tab
3. Monitor deployment and runtime logs

## 🚀 **Next Steps**

Once the backend is deployed:

1. **Test API Endpoints**:
   ```bash
   curl https://your-app.onrender.com/djangoapp/get_dealers/
   ```

2. **Deploy Additional Services**:
   - Node.js API (separate service)
   - React Frontend (separate service)

3. **Custom Domain** (Optional):
   - Add custom domain in Render dashboard
   - Configure DNS settings

## 💡 **Pro Tips**

- **Free Tier**: 750 hours/month (enough for demos)
- **Auto-Deploy**: Pushes to main branch auto-deploy
- **SSL**: Automatic HTTPS certificates
- **Monitoring**: Built-in metrics and alerts
- **Scaling**: Easy horizontal scaling

## 🔗 **Useful Links**

- [Render Documentation](https://render.com/docs)
- [Docker on Render](https://render.com/docs/docker)
- [Environment Variables](https://render.com/docs/environment-variables)
- [Custom Domains](https://render.com/docs/custom-domains) 