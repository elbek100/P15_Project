from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from main.models import Service, Image, ShoppingCart
from django.contrib import messages


class HomeTemplateView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        service_data = Service.objects.all()  # select * from main_service
        services_data = []
        for service in service_data:
            image = Image.objects.filter(service=service).first()  # select * from image where service_id=service_id
            service.image = image
            services_data.append(service)
        self.context.update({'service_data': services_data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        service_id = request.POST.get('service_id')
        if request.user is None:
            return redirect('/accounts/login')
        user = request.user
        print(user)
        if not ShoppingCart.objects.filter(Q(user=user) & Q(service_id=service_id)).exists():
            shopping_cart = ShoppingCart.objects.create(
                user=user,
                service_id=service_id
            )
            shopping_cart.save()
            messages.info(request, 'Product added to cart')
            return redirect('/shopping_cart')

        messages.error(request, 'This service already exists in cart!')
        return redirect('/')


class ShoppingCartTemplateView(View):
    template_name = 'shoping-cart.html'
    context = {}

    def get(self, request):
        if request.user.id is None:
            return redirect('/accounts/login')
        shopping_cart = ShoppingCart.objects.filter(user=request.user)
        data = []
        for index, value in enumerate(shopping_cart):
            image = Image.objects.filter(service=value.service).first()
            print(image)
            value.img = image
            value.index = index + 1
            data.append(value)
        self.context.update({'shopping_cart_products': data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        shopping_cart_id = request.POST.get('shopping_cart_id')
        ShoppingCart.objects.get(pk=shopping_cart_id).delete()
        return redirect('/shopping_cart')




def shop_grid(self,request):
        return render(request, self.template_name, self.context )


def blog(request):
    return render(request, 'blog.html')


def shop_details(request):
    return render(request, 'shop-details.html')


def contact(request):
    return render(request, 'contact.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def checkout(request):
    return render(request, 'checkout.html')

def sinov(request):
    return render(request,'')