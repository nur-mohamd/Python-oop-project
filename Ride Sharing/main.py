from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

# Create Company
niye_jao = RideSharing("Niye Jao")

# Create Rider
rahim = Rider(
    "Rahim Uddin",
    "rahim@gmail.com",
    1234,
    "Mohakhali",
    1200
)

# Add Rider
niye_jao.add_rider(rahim)

# Create Drivers
kolimuddin = Driver(
    "Kolim Uddin",
    "kolim@gmail.com",
    1256,
    "Gulshan"
)

karim = Driver(
    "Karim",
    "karim@gmail.com",
    5678,
    "Banani"
)

# Add Drivers
niye_jao.add_driver(kolimuddin)
niye_jao.add_driver(karim)

# Load More Cash
rahim.load_cash(500)

# Request Ride
rahim.request_ride(
    niye_jao,
    "Uttara",
    "car"
)

# Complete Ride
rahim.current_ride.driver.reach_destination(
    rahim.current_ride
)

# Show Ride Details
rahim.show_current_ride()

# Wallet Information
print("\nWallet Information:")
print("Rider Wallet :", rahim.wallet)

print(
    "Driver Wallet :",
    rahim.current_ride.driver.wallet
)

# Company Information
print(niye_jao)