# 🚀 Deployment Guide - Dealership Management System

This guide covers multiple deployment options for your full-stack application, from free hosting to production-ready solutions.

## 🎯 **Quick Deployment Options**

### **Option 1: Free Hosting (Recommended for Demo)**
- **Frontend**: Vercel (Free)
- **Backend**: Railway (Free tier)
- **Database**: MongoDB Atlas (Free tier)
- **Total Cost**: $0/month

### **Option 2: Production Ready**
- **Frontend**: Vercel Pro
- **Backend**: Railway Pro / AWS ECS
- **Database**: MongoDB Atlas / AWS DocumentDB
- **Total Cost**: $20-50/month

### **Option 3: Enterprise**
- **All Services**: AWS / Google Cloud / Azure
- **Container Orchestration**: Kubernetes
- **Total Cost**: $100+/month

---

## 🌐 **Option 1: Free Hosting Setup**

### **Step 1: Deploy Frontend to Vercel**

1. **Create Vercel Account**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub

2. **Deploy React App**
   ```bash
   # Install Vercel CLI
   npm i -g vercel
   
   # Deploy from frontend directory
   cd server/frontend
   vercel --prod
   ```

3. **Configure Build Settings**
   - **Framework Preset**: Create React App
   - **Root Directory**: `server/frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`

4. **Environment Variables**
   ```
   REACT_APP_DJANGO_API_URL=https://your-backend-url.railway.app
   ```

### **Step 2: Deploy Backend to Railway**

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy Django App**
   ```bash
   # Install Railway CLI
   npm install -g @railway/cli
   
   # Login and deploy
   railway login
   railway init
   railway up
   ```

3. **Configure Railway**
   - **Root Directory**: `server`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn djangoproj.wsgi:application --bind 0.0.0.0:$PORT`

4. **Environment Variables**
   ```
   DEBUG=False
   ALLOWED_HOSTS=your-app.railway.app
   backend_url=https://your-nodejs-api.railway.app
   sentiment_analyzer_url=https://your-sentiment-api.railway.app
   ```

### **Step 3: Deploy Node.js API to Railway**

1. **Create New Railway Service**
   - Deploy `server/database` directory
   - **Start Command**: `node app.js`

2. **Environment Variables**
   ```
   MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/dealership
   PORT=3030
   ```

### **Step 4: Deploy Sentiment Analysis to Railway**

1. **Create New Railway Service**
   - Deploy `server/djangoapp/microservices` directory
   - **Start Command**: `python app.py`

2. **Environment Variables**
   ```
   PORT=5000
   ```

### **Step 5: Setup MongoDB Atlas**

1. **Create MongoDB Atlas Account**
   - Go to [mongodb.com/atlas](https://mongodb.com/atlas)
   - Create free cluster

2. **Configure Database**
   - **Cluster Name**: dealership-cluster
   - **Database Name**: dealership
   - **Collections**: dealers, reviews

3. **Get Connection String**
   ```
   mongodb+srv://username:password@cluster.mongodb.net/dealership
   ```

4. **Import Data**
   ```bash
   # Import dealers
   mongoimport --uri "your-connection-string" --collection dealers --file server/database/data/dealerships.json --jsonArray
   
   # Import reviews
   mongoimport --uri "your-connection-string" --collection reviews --file server/database/data/reviews.json --jsonArray
   ```

---

## 🔧 **Option 2: Production Deployment**

### **AWS Deployment**

#### **Frontend (S3 + CloudFront)**
```bash
# Build React app
cd server/frontend
npm run build

# Deploy to S3
aws s3 sync build/ s3://your-bucket-name --delete
aws cloudfront create-invalidation --distribution-id YOUR_DISTRIBUTION_ID --paths "/*"
```

#### **Backend (ECS + Fargate)**
```yaml
# docker-compose.prod.yml
version: '3.8'
services:
  django:
    build: ./server
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DATABASE_URL=postgresql://user:pass@rds-endpoint/db
    
  nodejs:
    build: ./server/database
    ports:
      - "3030:3030"
    environment:
      - MONGODB_URL=mongodb://atlas-connection
```

#### **Database (RDS + DocumentDB)**
- **PostgreSQL**: For Django user data
- **DocumentDB**: For dealers and reviews
- **Redis**: For caching and sessions

### **Google Cloud Deployment**

#### **Frontend (Firebase Hosting)**
```bash
# Install Firebase CLI
npm install -g firebase-tools

# Initialize and deploy
firebase init hosting
firebase deploy
```

#### **Backend (Cloud Run)**
```dockerfile
# Dockerfile.prod
FROM python:3.12-slim
WORKDIR /app
COPY server/requirements.txt .
RUN pip install -r requirements.txt
COPY server/ .
CMD ["gunicorn", "djangoproj.wsgi:application", "--bind", "0.0.0.0:8080"]
```

```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT_ID/dealership-backend
gcloud run deploy --image gcr.io/PROJECT_ID/dealership-backend --platform managed
```

---

## 🐳 **Option 3: Docker Deployment**

### **Complete Docker Setup**

1. **Production Docker Compose**
   ```yaml
   # docker-compose.prod.yml
   version: '3.8'
   services:
     nginx:
       image: nginx:alpine
       ports:
         - "80:80"
         - "443:443"
       volumes:
         - ./nginx.conf:/etc/nginx/nginx.conf
         - ./ssl:/etc/nginx/ssl
       depends_on:
         - django
     
     django:
       build: ./server
       environment:
         - DEBUG=False
         - DATABASE_URL=postgresql://user:pass@postgres/db
       depends_on:
         - postgres
         - redis
     
     nodejs:
       build: ./server/database
       environment:
         - MONGODB_URL=mongodb://mongo:27017/dealership
       depends_on:
         - mongo
     
     sentiment:
       build: ./server/djangoapp/microservices
       
     postgres:
       image: postgres:13
       environment:
         - POSTGRES_DB=dealership
         - POSTGRES_USER=user
         - POSTGRES_PASSWORD=password
       volumes:
         - postgres_data:/var/lib/postgresql/data
     
     mongo:
       image: mongo:latest
       volumes:
         - mongo_data:/data/db
     
     redis:
       image: redis:alpine
   
   volumes:
     postgres_data:
     mongo_data:
   ```

2. **Deploy with Docker Swarm**
   ```bash
   # Initialize swarm
   docker swarm init
   
   # Deploy stack
   docker stack deploy -c docker-compose.prod.yml dealership
   ```

3. **Deploy with Kubernetes**
   ```bash
   # Apply Kubernetes manifests
   kubectl apply -f k8s/
   
   # Check deployment
   kubectl get pods
   kubectl get services
   ```

---

## 🌍 **Domain and SSL Setup**

### **Custom Domain**
1. **Buy Domain** (Namecheap, GoDaddy, etc.)
2. **Configure DNS**
   ```
   A     @     your-server-ip
   CNAME www   your-app.vercel.app
   ```

### **SSL Certificate**
```bash
# Using Let's Encrypt
certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

---

## 📊 **Monitoring and Analytics**

### **Application Monitoring**
- **Sentry**: Error tracking
- **New Relic**: Performance monitoring
- **DataDog**: Infrastructure monitoring

### **Analytics**
- **Google Analytics**: User behavior
- **Mixpanel**: Event tracking
- **Hotjar**: User experience

---

## 🔒 **Security Checklist**

### **Frontend Security**
- ✅ HTTPS enabled
- ✅ Content Security Policy
- ✅ XSS protection
- ✅ Environment variables secured

### **Backend Security**
- ✅ Django security settings
- ✅ CORS properly configured
- ✅ Rate limiting
- ✅ Input validation
- ✅ SQL injection protection

### **Infrastructure Security**
- ✅ Firewall configured
- ✅ VPC/Network isolation
- ✅ Database encryption
- ✅ Backup strategy

---

## 🚀 **Quick Deploy Commands**

### **Vercel (Frontend)**
```bash
cd server/frontend
npm run build
vercel --prod
```

### **Railway (Backend)**
```bash
cd server
railway up
```

### **Heroku (Alternative)**
```bash
# Django
cd server
heroku create your-app-name
git push heroku main

# Node.js
cd server/database
heroku create your-api-name
git push heroku main
```

---

## 📈 **Performance Optimization**

### **Frontend Optimization**
- Code splitting with React.lazy()
- Image optimization
- CDN for static assets
- Service worker for caching

### **Backend Optimization**
- Database indexing
- Query optimization
- Redis caching
- Load balancing

### **Infrastructure Optimization**
- Auto-scaling
- CDN configuration
- Database read replicas
- Monitoring and alerting

---

## 🎯 **Recommended Deployment Flow**

1. **Development**: Local Docker setup
2. **Staging**: Railway/Heroku free tiers
3. **Production**: AWS/GCP with custom domain
4. **Enterprise**: Kubernetes with monitoring

---

## 📞 **Support and Troubleshooting**

### **Common Issues**
- **CORS errors**: Check Django settings
- **Database connection**: Verify connection strings
- **Build failures**: Check environment variables
- **SSL issues**: Verify certificate configuration

### **Debugging Commands**
```bash
# Check logs
docker logs container-name
kubectl logs pod-name
heroku logs --tail

# Health checks
curl https://your-api.com/health
curl https://your-frontend.com
```

---

## 🎉 **Your Application is Ready for the World!**

Choose the deployment option that best fits your needs:
- **Demo/Portfolio**: Option 1 (Free)
- **Small Business**: Option 2 (Production)
- **Enterprise**: Option 3 (Scalable)

**Share your live application with:**
- Portfolio websites
- LinkedIn posts
- GitHub README
- Job applications
- Technical interviews

**Your full-stack application showcases:**
- Modern web development skills
- Microservices architecture
- AI integration capabilities
- DevOps and deployment knowledge
- Production-ready code quality 