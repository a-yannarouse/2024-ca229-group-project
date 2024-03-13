# simple_test_root/pages/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from . models import Page
from .contact import ContactForm

def index(request, pagename=''):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        'pagename': pg.title,
    }
    return render(request, 'pages/page.html', context)

def contact(request):
	submitted = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@dcu.ie'),
				['ayanna.rouse2@dcu.ie'], # change this
				connection=con
			)
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted
	}
	return render(request, 'pages/contact.html', context)


workout_vids = {
	(10,20) : 'https://www.youtube.com/embed/pj4TVbnIEgk',
	(21,30) : 'https://www.youtube.com/embed/ge1ALhE-Fqs',
	(31,40) : 'https://www.youtube.com/embed/StN0-7XLuR4',
	(41,60) : 'https://www.youtube.com/embed/RNxDmXdG8C0',
	(61,70) : 'https://www.youtube.com/embed/Ev6yE55kYGw',
}

def magic_page(request, num1, num2, num3):
	result = num1 + num2 + num3
	age = result

	workout_video_url = None
	for age_range, video_url in workout_vids.items():
		if age_range[0] <= age <= age_range[1]:
			workout_video_url = video_url
			break

	context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'result': age,
		'workout_video_url': workout_video_url,
		'page_list': Page.objects.all(),
    }
	return render(request, 'pages/magic.html', context)
