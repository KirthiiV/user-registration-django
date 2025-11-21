from django.shortcuts import render, redirect
from userpage.forms import UserForm
from .models import UserRegister
import json


def register_view(request):
    user_data = None

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            # Convert cleaned data to a serializable dict
            cleaned = form.cleaned_data.copy()

            if cleaned.get("dob"):
                cleaned["dob"] = cleaned["dob"].strftime("%Y-%m-%d")  # Convert date to string

            # Format JSON
            user_data = json.dumps(cleaned, indent=4)

            # Save in session (optional)
            request.session["user_data"] = user_data

            return render(request, "register.html", {
                "form": UserForm(),
                "user_data": user_data,
                "success": True
            })

    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})


def success_view(request):
    user_data = request.session.get("user_data")
    if not user_data:
        return redirect("register")

    return render(request, "success.html", {"user_data": user_data})


def view_users(request):
    users = UserRegister.objects.all()
    return render(request, "view_users.html", {"users": users})
