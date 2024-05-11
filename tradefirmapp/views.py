from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from .models import *

def home(request):
    return render(request, "index.html")

def create_order(request):
    if request.method == 'POST':
        # Extract cleaned data from the form
        order_date = request.POST["orderdate"]
        client_id = request.POST["clientid"]
        client_name = request.POST["clientname"]
        ordered_via = request.POST["orderedvia"]
        remark = request.POST["remark"]
        item_name = request.POST["itemname"]
        quantity = request.POST["itemqty"]

        # Create a new order object
        order = Order_Parent(
            order_date=order_date,
            client_id=client_id,
            client_name=client_name,
            ordered_via=ordered_via,
            remark=remark
        )

        print(order)

        # Save the order to the database
        order.save()

        # Redirect to a success page or display a confirmation message
        return render(request, 'create_order.html')
    
    return render(request, 'create_order.html')

def create_client(request):
    if request.method == 'POST':
        return render(request,'index.html')
        # Process form data and save order
        # Redirect to success page or display confirmation message
    else:
        return render(request, 'create_client.html')

def create_item(request):
    if request.method == 'POST':
        return render(request,'index.html')
        # Process form data and save order
        # Redirect to success page or display confirmation message
    else:
        return render(request, 'create_item.html')
    
def create_dispatch(request):
    if request.method == 'POST':
        return render(request,'index.html')
        # Process form data and save order
        # Redirect to success page or display confirmation message
    else:
        return render(request, 'create_dispatch.html')
    
def create_inward(request):
    if request.method == 'POST':
        return render(request,'index.html')
        # Process form data and save order
        # Redirect to success page or display confirmation message
    else:
        return render(request, 'create_inward.html')
    
def report_orders(request):
    return render(request, 'report_orders.html')

def test(request):
    order_details = {
        'order_id': 1,
        'customer_name': 'John Doe',  # Example data, replace with actual data
        'order_date': '2024-04-01',   # Example data, replace with actual data
        # Add more fields as needed
    }
    return render(request, 'edit_order.html')