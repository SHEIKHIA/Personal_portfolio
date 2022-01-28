from django.contrib import admin
from django.urls import path, include
#from quote_generator import views as quoteView
#from portfolio import views as portfolioView
from portfolio import views 
#from exchange_rate import views as exchangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #path('exchange/', exchangeView.index, name = "exchangeView"),
    #path('', quoteView.index, name = "index"),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)