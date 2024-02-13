from django.core.mail import send_mail
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic 
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm

# CRUD+L - Create, Retrieve, Update, and Delete + List

class SignupView(generic.CreateView):
  template_name = "registration/signup.html"
  # form_class = UserCreationForm

  # our own custom user creation form
  form_class = CustomUserCreationForm
  def get_success_url(self):
    return reverse('login')

# class based view
class LandingPageView(generic.TemplateView):
  template_name = 'landing.html'

# function based view
# def landing_page(request):
#   return render(request, 'landing.html')


# class based view
class LeadListView(LoginRequiredMixin, generic.ListView):
  template_name = "leads/lead_list.html"  
  queryset = Lead.objects.all()
  # object_list is the default name of context
  # But you can customize the name of the context in this instance `leads`
  context_object_name = 'leads'

# function based view
# def lead_list(request):

#   leads = Lead.objects.all()
#   # return HttpResponse('hello world')
#   # return render(request, 'leads/home_page.html')

#   # direct call the templates on root djcrm
#   context = {"leads": leads, "name": "Joefrey", "age": 39}
#   # context = {
#   #   "name": "Joefrey",
#   #   "age": 39
#   # }
#   return render(request, 'leads/lead_list.html', context)


class LeadDetailView(generic.DetailView):
  template_name = "leads/lead_detail.html"
  queryset = Lead.objects.all()
  context_object_name = "lead"


# def lead_detail(request, pk):
#   # print(pk)
#   lead = Lead.objects.get(id=pk)
#   print(lead)
#   context = {
#     'lead': lead
#   }
#   return render(request, 'leads/lead_detail.html', context)


class LeadCreateView(generic.CreateView):
  template_name = "leads/lead_create.html"
  form_class = LeadModelForm
  def get_success_url(self):
    return reverse('leads:lead-list')
  def form_valid(self, form):
    # todo send email
    send_mail(
      subject="A lead has been created", 
      message="Go to the site to see the new lead",
      from_email="test@test.com",
      recipient_list=["test2@test.com"]
    )
    return super(LeadCreateView, self).form_valid(form)
  # context_object_name = "lead

# def lead_create(request):
#   form = LeadModelForm()
#   if request.method == "POST":
#     form = LeadModelForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect("/leads")
#   context = {
#     "form" : form
#   }
#   return render(request, "leads/lead_create.html", context)


class LeadUpdateView(generic.UpdateView):
  template_name = "leads/lead_update.html"
  queryset = Lead.objects.all()
  form_class = LeadModelForm
  def get_success_url(self):
    return reverse('leads:lead-list')
  
# def lead_update(request, pk):
#   lead = Lead.objects.get(id=pk)
#   form = LeadModelForm(instance=lead)
#   if request.method == "POST":
#     form = LeadModelForm(request.POST, instance=lead)
#     if form.is_valid():
#       form.save()
#       return redirect("/leads")
#   context = {
#     "form" : form,
#     "lead": lead
#   }
#   return render(request, 'leads/lead_update.html', context)

class LeadDeleteView(generic.DeleteView):
  template_name = "leads/lead_delete.html"
  queryset = Lead.objects.all()
  def get_success_url(self):
    return reverse('leads:lead-list')
  
# def lead_delete(request, pk):
#   lead = Lead.objects.get(id=pk)
#   lead.delete()
#   return redirect('/leads')

# def lead_update(request, pk):
#   lead = Lead.objects.get(id=pk)
#   form = LeadForm()
#   if request.method == "POST":
#     form = LeadForm(request.POST)
#     if form.is_valid():
#       print(form.cleaned_data)
#       first_name = form.cleaned_data['first_name']
#       last_name = form.cleaned_data['last_name']
#       age = form.cleaned_data['age']
      
#       lead.first_name = first_name
#       lead.last_name = last_name
#       lead.age = age
#       lead.save()
      
      
#       print("The lead has been created")
#       return redirect("/leads")
#   context = {
#     "form" : form,
#     "lead": lead
#   }
#   return render(request, 'leads/lead_update.html', context)

# def lead_create(request):
  # form = LeadForm()
  # if request.method == "POST":
  #   print("Reciving a post request")
  #   form = LeadForm(request.POST)
  #   if form.is_valid():
  #     print("The form is valid")
  #     print(form.cleaned_data)
  #     first_name = form.cleaned_data['first_name']
  #     last_name = form.cleaned_data['last_name']
  #     age = form.cleaned_data['age']
  #     agent = Agent.objects.first()
  #     Lead.objects.create(
  #       first_name=first_name,
  #       last_name=last_name,
  #       age=age,
  #       agent=agent,
  #     )
  #     print("The lead has been created")
  #     return redirect("/leads")
  # context = {
  #   "form" : LeadForm()
  # }
  # return render(request, "leads/lead_create.html", context)