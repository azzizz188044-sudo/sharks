from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Teacher, Result

def home(request):
    teachers = Teacher.objects.all()
    results = Result.objects.all()
    form = ContactForm()

    # Faqat success=true bo‘lsa — success = True, aks holda False
    success = request.GET.get('success') == 'true'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            full_message = f"Yangi murojaat:\n\nIsm: {name}\nTelefon: {phone}\n\nXabar:\n{message}"

            send_mail(
                subject='Yangi contact xabari',
                message=full_message,
                from_email='your_email@gmail.com',
                recipient_list=['your_email@gmail.com'],
                fail_silently=False,
            )

            return redirect('/?success=true')  # Faqat yuborilganda bu URLga qaytadi

    return render(request, 'sharks/index.html', {
        'teachers': teachers,
        'results': results,
        'form': form,
        'success': success,
    })
