import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
#View dataframes headers
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

#Merge vists and cart using a left merge
visits_cart = pd.merge(visits, cart, how="left").reset_index()
print(visits_cart)

#Check length of merged dataframe
visits_cart_rows = len(visits_cart)
print(visits_cart_rows)

#Count number of Null in merged dataframe
count_nat = visits_cart[visits_cart.cart_time.isnull()].count()
print(count_nat)

#Percentage visited website but didn't add to cart
percentage_nocart = 1-((visits_cart_rows - count_nat) / visits_cart_rows)
print("Percentage users who visited website but did not add to cart is "+str(percentage_nocart)+"%")

cart_checkout = pd.merge(cart, checkout, how="left").reset_index()
print(cart_checkout)

#Length of cart_checkout
cart_checkout_rows = len(cart_checkout)
print(cart_checkout_rows)

#Count Cart Checkout NaT
cart_checkout_nat = cart_checkout[cart_checkout.checkout_time.isnull()].count()
print(cart_checkout_nat)

#Percentage add to cart but did not checkout
percentage_nocheckout = cart_checkout_nat / cart_checkout_rows 
print("Percentage users who added to cart but did not checkout is "+str(percentage_nocheckout)+"%")

#Combine all data in one dataframe
all_data = pd.merge(visits, cart, how="left").merge(checkout, how="left").merge( purchase, how="left")
print(all_data)

all_data_rows = len(all_data)
print(all_data_rows)

#Number of users who did not purchase
nopurchase = pd.merge(checkout, purchase, how="left")
nopurchase_rows = len(nopurchase)

#Percentage of users who did not purchase
nopurchase_nat = nopurchase[nopurchase.purchase_time.isnull()].count()
percentage_nopurchase = nopurchase_nat / nopurchase_rows
print("Percentage users who clicked on checkout but did not purchase is "+str(percentage_nopurchase)+"%")

#weakest funnel step
weakest_funnel_step = "The weakest funnel step is the top Funnel at "+str(percentage_nocart)+" % dropoff"
print(weakest_funnel_step)

#Calculate time to purchase
all_data['time_to_purchase'] = (all_data.purchase_time - all_data.visit_time)
print(all_data.time_to_purchase.reset_index())

#Show average time to purchase
avg_time_to_purchase = all_data.time_to_purchase.mean()
print("The avergae time to purchase is "+str(avg_time_to_purchase)+" minutes.")