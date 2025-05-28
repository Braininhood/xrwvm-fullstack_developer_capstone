# 🚗 Full Stack Dealership Application

[![CI/CD Pipeline](https://github.com/Braininhood/xrwvm-fullstack_developer_capstone/actions/workflows/main.yml/badge.svg)](https://github.com/Braininhood/xrwvm-fullstack_developer_capstone/actions/workflows/main.yml)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Available-brightgreen)](https://braininhood.github.io/xrwvm-fullstack_developer_capstone/)

A comprehensive full-stack web application for car dealership management with review system, sentiment analysis, and modern CI/CD pipeline.

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

## 🌐 Live Demo

**🚀 [View Live Application](https://braininhood.github.io/xrwvm-fullstack_developer_capstone/)**

The application is automatically deployed to GitHub Pages through our CI/CD pipeline. Share this link with anyone to showcase the project!

## ��️ Architecture

### **Frontend**
- **React** - Modern SPA with responsive design
- **Bootstrap** - UI components and styling
- **React Router** - Client-side routing

### **Backend**
- **Django** - RESTful API with authentication
- **Django REST Framework** - API serialization
- **SQLite** - Development database

### **Database Layer**
- **Node.js** - API server for dealership data
- **MongoDB** - NoSQL database for reviews and dealers
- **Express.js** - Web framework

### **Microservices**
- **Flask** - Sentiment analysis service
- **NLTK** - Natural language processing
- **Docker** - Containerization

### **DevOps & Deployment**
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Kubernetes** - Container orchestration
- **Nginx** - Reverse proxy (production)

## 🚀 CI/CD Pipeline

Our automated pipeline includes:

### 1. **Code Quality** 🔍
- Python linting with `flake8`
- JavaScript linting with `jshint`
- Code style enforcement

### 2. **Testing** 🧪
- Django backend tests
- Database migration checks
- API endpoint validation

### 3. **Build** 📦
- React frontend compilation
- Static asset optimization
- Artifact generation

### 4. **Deploy** 🌐
- Automatic deployment to GitHub Pages
- Demo website generation
- Live URL provisioning

## 🛠️ Local Development

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker & Docker Compose

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Braininhood/xrwvm-fullstack_developer_capstone.git
   cd xrwvm-fullstack_developer_capstone
   ```

2. **Start the database services**
   ```bash
   cd server/database
   docker-compose up -d
   ```

3. **Start Django backend**
   ```bash
   cd server
   pip install django djangorestframework requests python-dotenv
   python manage.py migrate
   python manage.py runserver
   ```

4. **Start React frontend**
   ```bash
   cd server/frontend
   npm install
   npm start
   ```

5. **Start sentiment analysis service**
   ```bash
   cd server/djangoapp/microservices
   docker build -t senti_analyzer .
   docker run -d -p 5050:5000 senti_analyzer
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

## 🐳 Docker Deployment

The application includes Docker configurations for all services:

```bash
# Database services
cd server/database
docker-compose up -d

# Sentiment analysis
cd server/djangoapp/microservices
docker build -t senti_analyzer .
docker run -d -p 5050:5000 senti_analyzer
```

## 📈 Monitoring & Analytics

- **GitHub Actions** - CI/CD pipeline monitoring
- **Automated testing** - Quality assurance
- **Deployment tracking** - Release management
- **Error handling** - Graceful failure recovery

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests locally
5. Submit a pull request

The CI/CD pipeline will automatically:
- Run code quality checks
- Execute tests
- Build the application
- Deploy to staging (on PR)
- Deploy to production (on merge to main)

## 📝 License

This project is part of the IBM Full Stack Developer Capstone course.

## 🎯 Project Highlights

- **Full Stack Development** - Complete end-to-end application
- **Microservices Architecture** - Scalable and maintainable
- **CI/CD Pipeline** - Automated testing and deployment
- **Cloud Deployment** - GitHub Pages hosting
- **Modern UI/UX** - Responsive and accessible design
- **AI Integration** - Sentiment analysis capabilities
- **Containerization** - Docker-based deployment
- **API Design** - RESTful services

---

**🌟 Star this repository if you found it helpful!**

**🔗 [Live Demo](https://braininhood.github.io/xrwvm-fullstack_developer_capstone/) | [GitHub Repository](https://github.com/Braininhood/xrwvm-fullstack_developer_capstone)**

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