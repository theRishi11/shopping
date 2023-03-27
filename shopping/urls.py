from django.contrib import admin
from django.urls import path
from ecommerce.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('category/<slug>/',category,name='category'),
    path('search/',search,name="search"),
    path('product/<slug>/',viewproduct,name="viewproduct"),
    path('login/',login,name="login"),
    path('register/',register,name="register"),
    path('logout/',user_logout,name='logout'),
    path("add-to-cart/<slug>/",addToCart, name="addCart"),
    path("remove-from-cart/<slug>/",removeFromCart, name="removeCart"),
    path("cart/",myCart,name="cart"),
    path("add-coupon/",addCoupon,name="addCoupon"),
    path("remove-coupon/",removeCoupon,name="removeCoupon"),
    path("checkout/",checkout,name="checkout"),
    path('check-with-Save/',checkWithSave,name="checkwithsave"),

]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

