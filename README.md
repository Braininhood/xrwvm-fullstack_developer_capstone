# 🚗 Dealership Application - Full Stack Developer Capstone

A comprehensive full-stack web application for car dealership management with review system, sentiment analysis, and modern UI/UX.

## 🌟 Features

### 🏪 **Dealership Management**
- Browse 50+ dealerships across multiple states
- Filter dealerships by state
- View detailed dealership information
- Interactive dealer listings with modern UI

### 📝 **Review System**
- Post authenticated reviews for dealerships
- Real-time sentiment analysis (Positive/Negative/Neutral)
- View all reviews with sentiment indicators
- Secure review posting (authentication required)

### 🚗 **Car Database**
- 15+ car models from 5 major manufacturers
- Complete car specifications (year, type, engine, etc.)
- Admin panel for car management
- Dynamic car selection in review forms

### 🔐 **User Authentication**
- User registration and login
- Session management
- Protected routes and API endpoints
- Django admin panel access

### 🤖 **AI-Powered Features**
- NLTK-based sentiment analysis microservice
- Real-time sentiment scoring for reviews
- Visual sentiment indicators in UI

## 🏗️ Architecture

### **Frontend**
- **React.js** - Modern component-based UI
- **Bootstrap** - Responsive design framework
- **React Router** - Client-side routing
- **Modern ES6+** - Latest JavaScript features

### **Backend**
- **Django** - Python web framework
- **Django REST Framework** - API development
- **SQLite** - Development database
- **Gunicorn** - Production WSGI server

### **Microservices**
- **Node.js API** - Dealership and review data service
- **Flask Sentiment Analyzer** - AI-powered sentiment analysis
- **MongoDB** - NoSQL database for reviews

### **DevOps & Deployment**
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Kubernetes** - Container orchestration
- **Nginx** - Reverse proxy (production)

## 🚀 Quick Start

### **Option 1: Docker Deployment (Recommended)**

```bash
# Clone the repository
git clone <repository-url>
cd xrwvm-fullstack_developer_capstone

# Start all services
cd server
docker-compose up -d

# Build and run the main application
docker build -t dealership-local .
docker run -p 8000:8000 dealership-local
```

### **Option 2: Kubernetes Deployment**

```bash
# Ensure Kubernetes is running (Docker Desktop)
kubectl cluster-info

# Deploy the application
cd server
kubectl apply -f deployment.yaml

# Set up port forwarding
kubectl port-forward deployment.apps/dealership 8000:8000
```

### **Option 3: Development Setup**

```bash
# Backend setup
cd server
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend setup (separate terminal)
cd server/frontend
npm install
npm run build

# Start external services
cd server/database
docker-compose up -d
```

## 📦 Services & Ports

| Service | Port | Description |
|---------|------|-------------|
| Django App | 8000 | Main web application |
| Node.js API | 3030 | Dealership/review backend |
| MongoDB | 27017 | Review database |
| Sentiment Analyzer | 5050 | AI sentiment analysis |
| Kubernetes NodePort | 30000 | Alternative access point |

## 🗄️ Database Schema

### **Django Models**
- **CarMake**: Manufacturer information
- **CarModel**: Vehicle specifications
- **User**: Django authentication

### **MongoDB Collections**
- **Dealerships**: Dealer information and locations
- **Reviews**: Customer reviews with metadata

## 🔧 API Endpoints

### **Django REST API**
```
GET  /djangoapp/get_dealers/          # All dealerships
GET  /djangoapp/get_dealers/<state>/  # Dealerships by state
GET  /djangoapp/dealer/<id>/          # Specific dealer
GET  /djangoapp/reviews/dealer/<id>/  # Dealer reviews
POST /djangoapp/add_review/           # Add new review
GET  /djangoapp/get_cars/             # Car models
```

### **Node.js Backend API**
```
GET  /fetchDealers                    # All dealers
GET  /fetchDealers/<state>            # Dealers by state
GET  /fetchDealer/<id>                # Specific dealer
GET  /fetchReviews/dealer/<id>        # Dealer reviews
POST /insert_review                   # Insert review
```

### **Sentiment Analysis API**
```
POST /analyze/<text>                  # Analyze sentiment
```

## 🛠️ Development

### **Project Structure**
```
xrwvm-fullstack_developer_capstone/
├── server/
│   ├── djangoapp/              # Django application
│   │   ├── models.py           # Database models
│   │   ├── views.py            # API views
│   │   ├── urls.py             # URL routing
│   │   ├── restapis.py         # External API integration
│   │   ├── populate.py         # Database population
│   │   └── microservices/      # Sentiment analysis
│   ├── frontend/               # React application
│   │   ├── src/
│   │   │   ├── components/     # React components
│   │   │   └── App.js          # Main app component
│   │   └── build/              # Production build
│   ├── database/               # Node.js backend
│   │   ├── app.js              # Express server
│   │   ├── data/               # JSON data files
│   │   └── docker-compose.yml  # Multi-container setup
│   ├── Dockerfile              # Django container
│   ├── deployment.yaml         # Kubernetes config
│   └── requirements.txt        # Python dependencies
└── README.md                   # This file
```

### **Adding New Features**

1. **Backend**: Add views in `djangoapp/views.py`
2. **Frontend**: Create components in `frontend/src/components/`
3. **Database**: Update models in `djangoapp/models.py`
4. **API**: Extend `restapis.py` for external integrations

### **Running Tests**
```bash
# Django tests
python manage.py test

# Frontend tests
cd frontend && npm test
```

## 🐳 Docker Configuration

### **Multi-Container Setup**
- **MongoDB**: Document database for reviews
- **Node.js**: RESTful API backend
- **Django**: Main web application
- **Sentiment Analyzer**: AI microservice

### **Environment Variables**
```bash
backend_url=http://host.docker.internal:3030
sentiment_analyzer_url=http://host.docker.internal:5050/
```

## ☸️ Kubernetes Deployment

### **Resources Created**
- **Deployment**: `dealership` (1 replica)
- **Service**: `dealership-service` (NodePort)
- **ConfigMap**: Environment variables
- **Persistent Volume**: Database storage (if needed)

### **Scaling**
```bash
kubectl scale deployment dealership --replicas=3
```

## 🔒 Security Features

- **CSRF Protection**: Django CSRF middleware
- **Authentication Required**: Protected review posting
- **Input Validation**: Form and API validation
- **SQL Injection Prevention**: Django ORM
- **XSS Protection**: Template escaping

## 🎨 UI/UX Features

- **Responsive Design**: Mobile-first approach
- **Modern Bootstrap**: Clean, professional interface
- **Interactive Elements**: Hover effects, smooth transitions
- **Accessibility**: ARIA labels, keyboard navigation
- **Loading States**: User feedback during API calls

## 📊 Data Sources

- **Dealerships**: 50 dealers across 21 states
- **Car Models**: 15 models from 5 manufacturers
- **Reviews**: User-generated content with sentiment
- **Sentiment Analysis**: NLTK VADER lexicon

## 🚀 Production Deployment

### **Performance Optimizations**
- **Static File Serving**: Nginx/CDN
- **Database Indexing**: Optimized queries
- **Caching**: Redis/Memcached
- **Compression**: Gzip/Brotli

### **Monitoring**
- **Health Checks**: Kubernetes probes
- **Logging**: Centralized log aggregation
- **Metrics**: Application performance monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## 📝 License

This project is part of a Full Stack Developer Capstone course.

## 🆘 Troubleshooting

### **Common Issues**

**Port Already in Use**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

**Docker Issues**
```bash
# Reset Docker
docker system prune -a
docker-compose down && docker-compose up -d
```

**Kubernetes Issues**
```bash
# Check pod status
kubectl get pods
kubectl logs deployment/dealership
```

**Database Connection**
```bash
# Verify external services
docker ps
curl http://localhost:3030/fetchDealers
```

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review application logs
3. Verify all services are running
4. Check network connectivity

---

**Built with ❤️ using Django, React, Node.js, and modern DevOps practices**