from django.shortcuts import render, HttpResponse, redirect
import random, datetime, time
  # the index function is called when root is visited
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0

    
    return render(request, 'ninjagambler/index.html')

def process(request):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not 'messages' in request.session:
        request.session['messages'] = []
    if request.POST['action'] == "farm":
        n = random.randint(10, 20)
        request.session['gold'] += n
        request.session['messages'].append(("Earned {} gold from the cave! ({})".format(n, timestamp), "green"))
    elif request.POST['action'] == "cave":
        n = random.randint(5, 10)
        request.session['gold'] += n 
        request.session['messages'].append(("Earned {} gold from the cave! ({})".format(n, timestamp), "green"))
    elif request.POST['action'] == "house":
        n = random.randint(2, 5)
        request.session['gold'] += n
        request.session['messages'].append(("Earned {} gold from the house! ({})".format(n, timestamp), "green"))
    elif request.POST['action'] == "casino":
        n = random.randint(-50, 50)
        request.session['gold'] += n
        if n < 0:
            request.session['messages'].append(("Entered a casino and lost {} gold... Ouch.. ({})".format(n, timestamp), "red"))
        else:
            request.session['messages'].append(("Earned {} gold from the Casino! ({})".format(n, timestamp), "green"))

    return redirect('/')

    