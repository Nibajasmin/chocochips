from django.shortcuts import render, redirect
from .models import Order

def home(request):
    if request.method == "POST":
        Order.objects.create(
            name=request.POST.get("name"),
            address=request.POST.get("address"),
            phone=request.POST.get("phone"),

            cake=request.POST.get("cake") or "",
            cake_quantity=int(request.POST.get("cake_quantity") or 0),

            brownie=request.POST.get("brownie") or "",
            brownie_quantity=int(request.POST.get("brownie_quantity") or 0),

            payment_method=request.POST.get("payment")
        )

        request.session["order_success"] = True
        return redirect("home")

    success = request.session.pop("order_success", False)
    return render(request, "index.html", {"success": success})