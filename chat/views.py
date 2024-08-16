
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.method == 'POST': # die funktion wird nur ausgeführt, wenn man ein POST reqeust ausführt
        print("Received data" + request.POST['textmessage']) # ist die variable aus der index html des inputs
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user) # erstellt eine neue Nachricht
    chatMessages = Message.objects.filter(chat__id=1)  # wir holen die nachrichten wo die chat id 1 ist   
    return render(request, 'chat/index.html', {'messages': chatMessages }) # Variable an die Index.html weitergegeben

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username') , password=request.POST.get('password'))
        if user:
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True} )
    return render(request, 'auth/login.html')