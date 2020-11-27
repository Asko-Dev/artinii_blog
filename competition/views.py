from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, FileResponse
from .models import AmateurCompetition
from .forms import AmateurCompetitionForm
from users.models import Profile


class CompetitionDetailViewUser(LoginRequiredMixin, DetailView):
    model = AmateurCompetition

class CompetitionCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = AmateurCompetition
    fields = ['title', 'link', 'plot', 'poster', 'letter']
    template_name = 'competition/amateur_competition.html'

    def get_success_message(self, cleaned_data):
        return f'Thank you {self.request.user}! We will review your submission.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponse("ERROR: Only one submission per account!")


# SECOND OPTION FOR COMPETITION FORM VIA METHOD
# @login_required
# def amateur_competition_form(request):
#     if request.method == 'POST':
#         a_form = AmateurCompetitionForm(request.POST, request.FILES)
#         if a_form.is_valid():
#             a_form.instance.user = request.user
#             a_form.save(commit=True)
#             messages.success(request, f'Thank you {request.user}. Your application has been received and will be reviewed shortly.')
#             return redirect ('post-user')
#     else:
#         a_form = AmateurCompetitionForm()
#
#     context = {
#         'a_form': a_form,
#     }
#     return render(request, 'competition/amateur_competition.html', context)
