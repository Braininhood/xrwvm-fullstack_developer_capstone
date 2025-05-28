# PostReview Troubleshooting Guide

## Issue: Cannot Post Reviews on Render Deployment

### What We Fixed

1. **API URL Configuration**: Updated `server/frontend/src/config.js` to use the correct API URL for production:
   ```javascript
   DJANGO_API_URL: process.env.REACT_APP_DJANGO_API_URL || 
     (process.env.NODE_ENV === 'production' ? '' : 'http://localhost:8000')
   ```

2. **Enhanced PostReview Component**: Added better error handling, CSRF token support, and authentication:
   - Added loading state to prevent double submissions
   - Added proper error handling with detailed error messages
   - Added CSRF token support for Django
   - Added `credentials: 'include'` for authentication cookies

### Current Status

The deployment is still showing some issues:
- API endpoints returning 502 errors
- Frontend not loading expected content

### Troubleshooting Steps

#### 1. Check Render Deployment Status
1. Go to your Render dashboard
2. Check if the deployment is still in progress
3. Look at the build logs for any errors

#### 2. Common Issues and Solutions

**502 Bad Gateway Errors:**
- Usually means the Django backend is not running properly
- Check Render logs for Python/Django errors
- Verify that all dependencies are installed correctly

**Frontend Not Loading:**
- Check if the React build completed successfully
- Verify that static files are being served correctly
- Check WhiteNoise configuration in Django settings

**Authentication Issues:**
- Verify CORS settings are correct
- Check CSRF configuration
- Ensure session cookies are working

#### 3. Manual Testing Steps

Once the deployment is working:

1. **Register a New User:**
   ```
   Go to: https://xrwvm-fullstack-developer-capstone-4q3s.onrender.com/
   Click "Register" and create a new account
   ```

2. **Navigate to Dealers:**
   ```
   Click "Browse Dealers"
   Select any dealer
   ```

3. **Post a Review:**
   ```
   Click the "Post Review" icon (📝)
   Fill out all required fields:
   - Review text
   - Purchase date
   - Car make/model
   - Car year
   Click "Post Review"
   ```

#### 4. Debug Information

If posting reviews still fails, check browser console for:
- Network errors
- API response codes
- JavaScript errors

Common error messages and solutions:

**"All details are mandatory":**
- Make sure all form fields are filled
- Check that car make/model is selected

**"Error posting review: 403":**
- User not authenticated
- Try logging out and logging back in

**"Error posting review: 500":**
- Server error
- Check Render logs for Django errors

**"Network error":**
- API endpoint not reachable
- Check if Django backend is running

#### 5. Environment Variables

Make sure these are set in Render:
- `DJANGO_SETTINGS_MODULE=djangoproj.production_settings`
- `DEBUG=False`
- Any database connection strings if using external DB

#### 6. Build Commands

Verify these commands in Render:
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn djangoproj.wsgi:application`

### Expected Behavior

When working correctly:
1. User can register and login
2. User can browse dealers
3. User can click "Post Review" icon on dealer page
4. Review form loads with car models populated
5. User can submit review and see success message
6. User is redirected back to dealer page with new review

### Contact Information

If issues persist:
1. Check Render deployment logs
2. Verify all files were committed and pushed to GitHub
3. Wait 5-10 minutes for deployment to complete
4. Try the manual testing steps above 