from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (
    ListView, 
    CreateView, 
    DeleteView, 
    DetailView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Order, Book
from django.urls import reverse_lazy



#EDIT


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'library/profile_orders_list.html'



class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name= 'library/order_create.html'
    fields = ['book', 'street_name', 'num_building', 'num_door', 'post_code', 'city', 'country']
    success_url = reverse_lazy('profile-orders-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Udało Ci się zamówić książke!', extra_tags='order')
        return super().form_valid(form)




class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    template_name = 'library/order_delete.html'
    success_url = reverse_lazy('profile-orders-list')
    success_message = 'Udało Ci się usunąć zamówienie!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message, extra_tags='order')
        return super(OrderDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False



class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False



class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    fields = ['book', 'street_name', 'num_building', 'num_door', 'post_code', 'city', 'country']
    template_name = 'library/order_update.html'
    success_url = reverse_lazy('profile-orders-list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Udało Ci się zaktualizowac zamowienie!', extra_tags='order')
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False


def home(request):
    return render(request, 'library/home.html')

def about(request):
    return render(request, 'library/about.html')

def gallery(request):

    context = { 'books': Book.objects.all() }

    return render(request, 'library/gallery.html', context)