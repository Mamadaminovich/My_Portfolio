from django.conf import settings
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import get_connection

def home(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "portfolio-details.html", {})

def home2(request):
    return render(request, "inner-page.html", {})

@csrf_exempt
def send_email(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get("email"), ]
        message = request.POST.get("message")

        try:
            with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
            ) as connection:
                email = EmailMessage(subject, message, email_from, recipient_list, connection=connection)
                email.send()

                return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
