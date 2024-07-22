from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    IndexView, Index2View, Index3View, Index4View, Index5View, Index6View, Index7View, Index8View,
    AboutView, ServiceView, TeamView, FaqView, LoginView, ShopView, ShopListView, ShopDetailsView,
    CartView, CheckoutView, WishlistView, BlogView, BlogListView, BlogGridView, BlogGridSidebarView,
    BlogMasonryView, BlogDetailsView, ErrorView, ContactView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('index2/', Index2View.as_view(), name='index2'),
    path('index3/', Index3View.as_view(), name='index3'),
    path('index4/', Index4View.as_view(), name='index4'),
    path('index5/', Index5View.as_view(), name='index5'),
    path('index6/', Index6View.as_view(), name='index6'),
    path('index7/', Index7View.as_view(), name='index7'),
    path('index8/', Index8View.as_view(), name='index8'),

    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServiceView.as_view(), name='service'),
    path('team/', TeamView.as_view(), name='team'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('login-register/', LoginView.as_view(), name='login-register'),
    path('logout/', LogoutView.as_view(next_page='login-register'), name='logout'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop-list/', ShopListView.as_view(), name='shop-list'),
    path('shop-details/', ShopDetailsView.as_view(), name='shop-details'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-list/', BlogListView.as_view(), name='blog-list'),
    path('blog-grid/', BlogGridView.as_view(), name='blog-grid'),
    path('blog-grid-sidebar/', BlogGridSidebarView.as_view(), name='blog-grid-sidebar'),
    path('blog-masonry/', BlogMasonryView.as_view(), name='blog-masonry'),
    path('blog-details/', BlogDetailsView.as_view(), name='blog-details'),
    path('error/', ErrorView.as_view(), name='error'),
    path('contact/', ContactView.as_view(), name='contact'),
]

