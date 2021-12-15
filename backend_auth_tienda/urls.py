from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from auth_example                   import views
from drf_spectacular.views          import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/',                               admin.site.urls),
    path('api/schema/',                          SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',               SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',                    SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('login/',                               TokenObtainPairView.as_view()),
    path('refresh/',                             TokenRefreshView.as_view()),
    path('verifyToken/',                         views.VerifyTokenView.as_view()),
    path('user/',                                views.UserCreateView.as_view()),
    path('user/<int:pk>/',                       views.UserDetailView.as_view()),
    path('user/update/<int:pk>/',                views.UserUpdateView.as_view()), 

    #path('cuenta/',                              views.AccountCreateView.as_view()),
    path('cuenta/<int:pk>/',                     views.ListAccountsView.as_view()),

    path('prendaInventario/',                    views.PrendaInventarioCreateView.as_view()),
    path('prendaInventarioList/<int:pk>/',       views.PrendaInventarioListView.as_view()),
    path('prendaInventarioActualizar/<int:pk>/', views.PrendaInventarioUpdateView.as_view()),
    path('prendaInventarioBorrar/<int:pk>/',     views.PrendaInventarioDeleteView.as_view()),

]