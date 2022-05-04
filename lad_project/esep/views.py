 

# Create your views here.
from distutils.log import error
from django.shortcuts import render,redirect
from django.urls import reverse_lazy 
from .models import Tagam
from .models import Makal
from .models import Pikir
from .forms import TagamForm,UserRegistrationForm,LoginUserForm
from django.views.generic import DetailView, UpdateView, DeleteView,CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Create your views here.
def send_message(request): 
    
     send_mail("Welcome to testing page","My content","200103073@stu.sdu.edu.kz",["200103073@stu.sdu.edu.kz","200103057@stu.sdu.edu.kz"], 
               fail_silently=False,html_message="Сізді 2-мамыр күні болатын наурызға шақырамын" ) 
  
     
     return render (request,'esep/send.html')




     
     
     '''
    email = EmailMessage(
       'Hello',
       'Body goes here',
       '200103073@stu.sdu.edu.kz',
       ['2001030057@stu.sdu.edu.kz','2001030057@stu.sdu.edu.kz'],
       headers={'Message-ID':'foo'},
   )
    email.attach_file('/Users/Бибинур/Desktop/send.png')

    email.send(fail_silently=False)
    return render(request, 'esep/send.html')
'''
    






def home(request):
    tagam = Tagam.objects.all()
    return render(request,'esep/first.html',{'tagam': tagam})

class NewsDetailView(DetailView):
    model = Tagam
    template_name = 'esep/details_view.html'
    context_object_name = 'tagam'

class NewsUpdateView(UpdateView):
    model = Tagam
    success_url = '/esep/'
    template_name = 'esep/update.html'
    form_class = TagamForm

class NewsDeleteView(DeleteView):
    model = Tagam
    success_url = '/esep/'
    template_name = 'esep/news-delete.html'

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'esep/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

def pikir(request):
    pik = Pikir.objects.all()
    return render(request,'esep/pikir.html',{'title':'Пікірлер','pik': pik}) 

def makal(request):
    makal = Makal.objects.all()
    return render(request,'esep/third.html',{'title':'Мақал','makal': makal}) 

def create(request):
    if request.method == 'POST':
          form = TagamForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('home')

    form = TagamForm()
    data = {
      'form': form
    }
    return render(request,'esep/create.html', data)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'esep/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'esep/registor.html', {'user_form': user_form})