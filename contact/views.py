from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Messages
from resume.models import Education, Experience, Awards

# Create your views here.
@csrf_exempt
def IndexView(request):
    # @csrf_protect
    if request.method == "POST":
        s = request.POST
        form = Messages.objects.create(
            name=s["name"],
            phone=s.get("phone"),
            message=s.get("message")
        )

        return redirect('index')

    return render(request, 'index.html',context=({'education': Education.objects.all(), 'experience': Experience.objects.all(),'awards': Awards.objects.all()}))