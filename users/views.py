from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.urls import reverse_lazy


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/profile_delete.html'
    success_url = reverse_lazy('lib-home')
    success_message = 'Udało Ci się usunąc konto!'
    
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UserDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        user = self.get_object()
        if self.request.user == user: 
            return True
        return False


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Udało Ci się zarejestrować użytkownika {username}')
            return redirect('users-login')

        else:
            messages.error(request, f'Nie udało się zarejestrować użytkownika!')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', { 'form': form }) 

@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
                                instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Udało Ci się zaktualizować profil!', extra_tags='profile_update')
            return redirect('profile-orders-list')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_update.html', context)

