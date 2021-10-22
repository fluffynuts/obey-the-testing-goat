from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page(req: HttpRequest) -> HttpResponse:
    return render(req, "home.html", {
        "new_item_text": req.POST.get("item_text", "")
    })
