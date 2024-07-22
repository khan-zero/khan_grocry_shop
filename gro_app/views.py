from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
class IndexView(TemplateView):
    template_name = 'index.html'

class Index2View(TemplateView):
    template_name = 'index-2.html'

class Index3View(TemplateView):
    template_name = 'index-3.html'

class Index4View(TemplateView):
    template_name = 'index-4.html'

class Index5View(TemplateView):
    template_name = 'index-5.html'

class Index6View(TemplateView):
    template_name = 'index-6.html'

class Index7View(TemplateView):
    template_name = 'index-7.html'

class Index8View(TemplateView):
    template_name = 'index-8.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

class TeamView(TemplateView):
    template_name = 'team.html'

class FaqView(TemplateView):
    template_name = 'faq.html'

class LoginView(TemplateView):
    template_name = 'login-register.html'

class ShopView(TemplateView):
    template_name = 'shop.html'

class ShopListView(TemplateView):
    template_name = 'shop-list.html'

class ShopDetailsView(TemplateView):
    template_name = 'shop-details.html'

class CartView(TemplateView):
    template_name = 'cart.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

class WishlistView(TemplateView):
    template_name = 'wishlist.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

class BlogListView(TemplateView):
    template_name = 'blog-list.html'

class BlogGridView(TemplateView):
    template_name = 'blog-grid.html'

class BlogGridSidebarView(TemplateView):
    template_name = 'blog-grid-sidebar.html'

class BlogMasonryView(TemplateView):
    template_name = 'blog-masonry.html'

class BlogDetailsView(TemplateView):
    template_name = 'blog-details.html'

class ErrorView(TemplateView):
    template_name = 'error.html'

class ContactView(TemplateView):
    template_name = 'contact.html'