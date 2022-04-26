from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Category, Product, Email, Number

class IndexView(ListView):
    template_name = "index.html"
    model = Product
    context_object_name = "products"
    paginate_by = 16
    queryset = Product.objects.filter(active=True).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by("-id")
        context['email'] = Email.objects.order_by("-id").first()
        context['number'] = Number.objects.order_by("-id").first()
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(active=True).order_by('-id')
        category = self.request.GET.get('category')
        title = self.request.GET.get('title')
        if category:
            queryset = queryset.filter(category__title=category)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class WishListView(TemplateView):
    template_name = 'wishlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = Email.objects.order_by("-id").first()
        context['number'] = Number.objects.order_by("-id").first()
        return context