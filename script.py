import codecademylib
import pandas as pd
from decimal import Decimal

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

#Combine visits and cart dataframes
visits_cart = pd.merge(visits, cart, how="left")
print(visits_cart)

visits_cart_row = len(visits_cart)
print(visits_cart_row)

visits_cart_nat = len(visits_cart[visits_cart.cart_time.isnull()])
print(visits_cart_nat)

#Calculate dropoff at visit and cart pages
percentage_visits_cart_dropoff = float(visits_cart_nat) / visits_cart_row
print("Percentage of users that dropoff from the visit page to cart page is "+str(round(percentage_visits_cart_dropoff*100, 2))+"%.")

#Merge cart checkout dataframes
cart_checkout = pd.merge(cart, checkout, how = "left")
print(cart_checkout)

cart_checkout_rows = len(cart_checkout)
print(cart_checkout_rows)

cart_checkout_nat = len(cart_checkout[cart_checkout.checkout_time.isnull()])
print(cart_checkout_nat)

percentage_cart_checkout_dropoff = float(cart_checkout_nat) / cart_checkout_rows
print("Percentage of users that dropff from the cart page to checkout page is "+str(round(percentage_cart_checkout_dropoff*100, 2))+"%.")

#Merge visits, cart, checkout and purchase dataframes
all_data = pd.merge(visits, cart, how="left").merge(checkout, how="left").merge(purchase, how="left")
print(all_data)

#Merge checkout and purchase dataframes
checkout_purchase = pd.merge(checkout, purchase, how="left")
print(checkout_purchase)

checkout_purchase_rows = len(checkout_purchase)
print(checkout_purchase_rows)

checkout_purchase_nat = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
print(checkout_purchase_nat)

#Calculate the drop off form the checkout page and purchase page
percentage_checkout_purchase = float(checkout_purchase_nat) / checkout_purchase_rows
print("Percentage of users that dropoff from the checkout page to purchase page is "+str(round(percentage_checkout_purchase*100, 2))+"%.")

#Weakest part of the funnel
weakest_funnel = "The weakest part of the funnel is the top funnel."
print(weakest_funnel)

#Add time to purchase column to dataframe
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)

#Show avergae time to purchase
print("The average time to purchase is "+str(all_data.time_to_purchase.mean())+" minutes.")