from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from auth_example                   import views
from drf_spectacular.views          import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/',                     admin.site.urls),
    path('api/schema/',                SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',     SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',          SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('login/',                     TokenObtainPairView.as_view()),
    path('refresh/',                   TokenRefreshView.as_view()),
    path('verifyToken/',               views.VerifyTokenView.as_view()),
    path('user/',                      views.UserCreateView.as_view()),
    path('user/<int:pk>/',             views.UserDetailView.as_view()),
    path('user/update/<int:pk>/',      views.UserUpdateView.as_view()), 

    path('prenda/',                    views.PrendaCreateView.as_view()),
    path('prendaList/',                views.PrendaListView.as_view()),
    path('prendaActualizar/<int:pk>/', views.PrendaUpdateView.as_view()),
    path('prendaBorrar/<int:pk>/',     views.PrendaDeleteView.as_view()),

]