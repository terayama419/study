from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/memo/', permanent=False)),
    path('memo/', include('app.urls.memo_urls')),
    path('category/', include('app.urls.category_urls')),
    path('signup/', include('app.urls.signup_urls')),
]