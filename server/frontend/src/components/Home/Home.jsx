import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
  return (
    <div className="home-container">
      <div className="hero-section">
        <h1>🚗 Welcome to Dealership Management System</h1>
        <p>Your comprehensive solution for car dealership management</p>
        <div className="cta-buttons">
          <Link to="/dealers" className="btn btn-primary">Browse Dealers</Link>
          <Link to="/login" className="btn btn-secondary">Login</Link>
        </div>
      </div>
      
      <div className="features-section">
        <h2>Features</h2>
        <div className="features-grid">
          <div className="feature-card">
            <h3>🏪 Dealer Management</h3>
            <p>Browse and manage dealerships across multiple states</p>
          </div>
          <div className="feature-card">
            <h3>📝 Review System</h3>
            <p>Customer reviews with AI-powered sentiment analysis</p>
          </div>
          <div className="feature-card">
            <h3>🚗 Car Database</h3>
            <p>Comprehensive car inventory management</p>
          </div>
          <div className="feature-card">
            <h3>🔐 User Authentication</h3>
            <p>Secure login and registration system</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home; 