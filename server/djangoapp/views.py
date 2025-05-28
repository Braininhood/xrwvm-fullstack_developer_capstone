# Uncomment the required imports before adding the code

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel, Dealer, Review
from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


# Create a `logout_request` view to handle sign out request
@csrf_exempt
def logout_request(request):
    try:
        if request.user.is_authenticated:
            username = request.user.username
            logout(request)  # Terminate user session
            data = {"userName": "",
                    "message": f"User {username} logged out successfully"}
        else:
            data = {"userName": "", "message": "No user was logged in"}
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    try:
        # Load JSON data from the request body
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        first_name = data['firstName']
        last_name = data['lastName']
        email = data['email']

        # Validate required fields
        if not username or not password or not email:
            return JsonResponse(
                {"error": "Username, password, and email are required"},
                status=400
            )

        username_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            username_exist = True
        except User.DoesNotExist:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))

        # If it is a new user
        if not username_exist:
            # Create user in auth_user table
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email
            )
            # Login the user and redirect to list page
            login(request, user)
            data = {"userName": username, "status": "Authenticated"}
            return JsonResponse(data)
        else:
            data = {"userName": username, "error": "Already Registered"}
            return JsonResponse(data)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
    except KeyError as e:
        return JsonResponse(
            {"error": f"Missing required field: {str(e)}"}, status=400
        )
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        return JsonResponse({"error": "Registration failed"}, status=500)


# Update the `get_dealerships` render list of dealerships all by default,
# particular state if state is passed
def get_dealerships(request, state="All"):
    try:
        if state == "All":
            dealers = Dealer.objects.all()
        else:
            dealers = Dealer.objects.filter(state=state)
        
        dealers_list = []
        for dealer in dealers:
            dealers_list.append({
                "id": dealer.id,
                "full_name": dealer.full_name,
                "city": dealer.city,
                "state": dealer.state,
                "address": dealer.address,
                "zip": dealer.zip_code,
                "lat": dealer.lat,
                "long": dealer.long,
                "short_name": dealer.short_name,
                "st": dealer.st
            })
        
        return JsonResponse({"status": 200, "dealers": dealers_list})
    except Exception as e:
        logger.error(f"Error fetching dealers: {str(e)}")
        return JsonResponse({"status": 500, "dealers": []})


# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)
        dealer_data = {
            "id": dealer.id,
            "full_name": dealer.full_name,
            "city": dealer.city,
            "state": dealer.state,
            "address": dealer.address,
            "zip": dealer.zip_code,
            "lat": dealer.lat,
            "long": dealer.long,
            "short_name": dealer.short_name,
            "st": dealer.st
        }
        return JsonResponse({"status": 200, "dealer": dealer_data})
    except Dealer.DoesNotExist:
        return JsonResponse({"status": 404, "message": "Dealer not found"})
    except Exception as e:
        logger.error(f"Error fetching dealer details: {str(e)}")
        return JsonResponse({"status": 500, "message": "Internal server error"})


# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)
        reviews = Review.objects.filter(dealer=dealer)
        
        reviews_list = []
        for review in reviews:
            reviews_list.append({
                "id": review.id,
                "name": review.name,
                "dealership": dealer_id,
                "review": review.review,
                "purchase": review.purchase,
                "purchase_date": review.purchase_date.strftime("%Y-%m-%d"),
                "car_make": review.car_make,
                "car_model": review.car_model,
                "car_year": review.car_year,
                "sentiment": review.sentiment or "neutral"
            })
        
        return JsonResponse({"status": 200, "reviews": reviews_list})
    except Dealer.DoesNotExist:
        return JsonResponse({"status": 404, "message": "Dealer not found"})
    except Exception as e:
        logger.error(f"Error fetching reviews: {str(e)}")
        return JsonResponse({"status": 500, "reviews": []})


# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request):
    if not request.user.is_anonymous:
        try:
            data = json.loads(request.body)
            
            # Get the dealer
            dealer = Dealer.objects.get(id=data['dealership'])
            
            # Create the review
            review = Review.objects.create(
                dealer=dealer,
                name=data['name'],
                review=data['review'],
                purchase=data.get('purchase', True),
                purchase_date=data['purchase_date'],
                car_make=data['car_make'],
                car_model=data['car_model'],
                car_year=data['car_year'],
                sentiment="neutral"  # Default sentiment since we don't have the microservice
            )
            
            return JsonResponse({"status": 200, "message": "Review added successfully"})
        except Dealer.DoesNotExist:
            return JsonResponse({
                "status": 404,
                "message": "Dealer not found"
            })
        except Exception as e:
            logger.error(f"Error adding review: {str(e)}")
            return JsonResponse({
                "status": 500,
                "message": "Error in posting review"
            })
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})


def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if (count == 0):
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name
        })
    return JsonResponse({"CarModels": cars})
