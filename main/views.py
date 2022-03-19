import email
from msilib.schema import Class
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action, authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework import viewsets
from main.serializer import *
from main.models import *

class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    http_method_names = ['get']

    def list(self, request):
        slider = Slider.objects.all().order_by('-id')[0:3]
        ser = SliderSerializer(slider, many=True)
        return Response(ser.data)




class CategoriesView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

    def list(self, request):
        categories = Categories.objects.all().order_by('-id')[0:3]
        cat = CategoriesSerializer(categories, many=True)
        return Response(cat.data)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    http_method_names = ['get']
    def list(self, request):
        product = Product.objects.all()
        prod = ProductSerializer(product, many=True)
        return Response(prod.data)


class InfoView(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_name=['get']
    def list(self, request):
        user = request.user
        if user.typee == 1 or 2:
            info = Info.objects.last()
            inf = InfoSerializer(info)
            return Response(inf.data)

    http_method_name=['post']
    def create(self, request):
        try: 
            user = request.user
            if user.typee == 1:
                phone = request.POST.get('phone')
                address = request.POST.get('address')
                email = request.POST.get('email')
                map = request.POST.get('map')
                Info.objects.create(phone=phone, address=address,email=email,map=map)
                return Response({"message":"Created"})
        except Exception as arr:
            data = {
                'status': False,
                'error': f"{arr}"
            }
            return Response(data)

    http_method_name=['put']
    def create(self, request):
        try: 
            user = request.user
            if user.typee == 1:
                phone = request.POST.get('phone')
                address = request.POST.get('address')
                email = request.POST.get('email')
                map = request.POST.get('map')
                Info.objects.create(phone=phone, address=address,email=email,map=map)
                return Response({"message":"Created"})
        except Exception as arr:
            data = {
                'status': False,
                'error': f"{arr}"
            }
            return Response(data)
        


class NewslettersView(viewsets.ModelViewSet):
    queryset = Newsletters.objects.all()
    serializer_class = NewslettersSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_name=['post']
    def create(self, request):
        try:
            user = request.user
            if user.typee == 2:
                email = request.POST.get('email')
                Newsletters.objects.create(email=email)
                return Response({'message':'Email Created'})
        except Exception as arr:
            data = {
                "status":False,
                'error':f"{arr}"
            }    
            return Response(data)

    http_method_name=['get']
    def list(self, request):
        try:
            user = request.user
            if user.typee == 1:
                news = Newsletters.objects.all()
                new = NewslettersSerializer(news, many=True)
                return Response(new.data)
        except Exception as arr:
            data = {
                "status":False,
                'error':f"{arr}"
            }    
            return Response(data)

    
class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_name=['get']
    def list(self, request):
        user = request.user
        if user.typee == 1 or 2:
            blog = Blog.objects.all()
            bl = BlogSerializer(blog, many=True)
            return Response(bl.data)

    http_method_name=['post']
    def crete(self, request):
        try:
            user = request.user
            if user.typee == 1:
                img = request.FILES['img']
                title = request.POST['title']
                text = request.POST['text']
                Blog.objects.create(img=img, title=title, text=text)
                return Response({"message":"BlogFile Created"})
            
            else:
                return Response("Afsus :(")
        except Exception as arr:
            data = {
                "status":False,
                'error':f"{arr}"
            }    
            return Response(data)
            

class AboutView(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_name=['post']
    def create(self, request):
        try:
            user = request.user
            if user.typee == 1:
                img = request.FILES.get('img')
                text1 = request.POST.get('text1')
                text2 = request.POST.get('text2')
                About.objects.create(img=img,text1=text1,text2=text2)
                return Response({'message':'File Created'})
            else:
                return Response({'Afsus :('})
        except Exception as arr:
            data = {
                "status":False,
                'error':f"{arr}"
            }    
            return Response(data)
    http_method_name=['post']
    def list(self, request):
        try:
            user = request.user
            if user.typee == 2:
                about = About.objects.last()
                ab = AboutSerializer(about)
                return Response(ab.data)
            else:
                return Response({'Afsus :('})
        except Exception as arr:
            data = {
                'status':False,
                'error': f"{arr}"
            }
            return Response(data)

class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_name=['post']
    def create(self, request):
        try:
            user = request.user
            if user.typee == 2:
                email = request.POST.get("email")
                msg = request.POST.get("msg")
                Contact.objects.create(email=email, msg=msg)
                return Response({'message':'Contact Added'})
        except Exception as arr:
            data = {
                "status":False,
                'error':f"{arr}"
            }    
            return Response(data)

    http_method_name=['get']
    def list(self, request):
        user = request.user
        if user.typee == 1:
            contact = Contact.objects.all()
            con = ContactSerializer(contact, many=True)
            return Response(con.data)
    
class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_name=['post']
    def create(self, request):
        try:
            user = request.user
            if user.typee == 2:
                product_id = request.POST.get("product")
                Cart.objects.create(product_id=product_id)
                return Response({'message':'Added'})
            else:
                return Response({'Afsus :('})
        except Exception as arr:
            data = {
                "status":False,
                'error':f"{arr}"
            }    
            return Response(data)

    http_method_name=['get']
    def list(self, request):
        user = request.user
        if user.typee == 2:
            cart = Cart.objects.filter(user_id=user)
            ca = CartSerializer(cart, many=True)
            return Response(ca.data)
        elif user.typee == 1:
            cart = Cart.objects.all()
            ca = CartSerializer(cart, many=True)
            return Response(ca.data)
    
class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_name=['post']
    def create(self, request):
        try:
            user = request.user
            if user.typee == 2:
                product_id = request.POST.get("product")
                Wishlist.objects.create(product_id=product_id)
                return Response({'message':'Added'})
        except Exception as arr:
            data = {
                "status":False,
                'error':f"{arr}"
            }    
            return Response(data)

    http_method_name=['get']
    def list(self, request):
        user = request.user
        if user.typee == 2:
            cart = Wishlist.objects.filter(user_id=user)
            ca = WishlistSerializer(cart, many=True)
            return Response(ca.data)
        elif user.typee == 1:
            cart = Wishlist.objects.all()
            ca = WishlistSerializer(cart, many=True)
            return Response(ca.data)







































    # def list(self, request):
    #     try:
    #         user=request.user
    #         index = Index.objects.all()
    #         if user.is_superuser:
    #             ind = IndexSerializer(index, many=True)
    #             return Response(ind.data)
    #         else:
    #             return Response({"I'm sorry!"})
    #     except Exception as err:
    #         data = {
    #             'data':f'{err}'
    #         } 
    #         return Response(data)


