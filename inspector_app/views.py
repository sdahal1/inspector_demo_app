# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages

def index(request):
    return render(request, "index.html")


def login_view(request):
    print("logging in", request.POST.get("username"), request.POST.get("password"))
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        query = f"SELECT * FROM inspector_app_user WHERE username = '{username}' AND password = '{password}'"

        print(query)
        with connection.cursor() as cursor:
            # Simulating a SQL injection attack
            # Password input: ' OR 1=1 --
            # This would make the query always return the first user in the table
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                return redirect("success")
            else:
                messages.error(request, 'Invalid username or password.')
            return redirect('index')
def success(request):
    return render(request, 'success.html')
