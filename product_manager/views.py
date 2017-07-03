from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import DetailView,ListView,View

from product_manager.forms import RegisterForm, AddRemoveProductToCartForm
from product_manager.models import Product, Cart


class ProductListView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    model = Product


class ProductDetailView(DetailView):
    template_name = 'product-detail.html'
    model = Product

#@login_required
class CartView(View):
    def get(self, request):
        cart = get_object_or_404(Cart,owner__id=request.user.id)
        context = {'cart':cart}
        return render(request, 'cart-detail.html',context)

    def post(self,request):
        form = AddRemoveProductToCartForm(request.POST)
        if form.is_valid():
            cart = get_object_or_404(Cart, owner__id=request.user.id)
            product_id = form.cleaned_data['id']
            product = Product.objects.get(pk=product_id)
            print form.cleaned_data['action']
            if form.cleaned_data['action'] == 'add':
                if product.quantity > 0:
                    cart.products.add(product)
                    cart.total += product.price
                    product.quantity -= 1;

            else:
                cart.products.remove(product)
                cart.total -= product.price
                product.quantity += 1;
            product.save()
            cart.save()
        return redirect('cart-detail')

class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            cart = Cart(owner = user)
            cart.save()
            login(request, user)
            return redirect('products')

        return render(request, 'register.html', {'form': form})


