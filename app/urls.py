from django.urls import include, path

urlpatterns = [
    path('memo/', include('app.urls.memo_urls')),
    path('category/', include('app.urls.category_urls')),
    path('signup/', include('app.urls.signup_urls')),
]