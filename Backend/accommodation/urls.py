from django.urls import include, path

from accommodation import views

urlpatterns = [
    path(
        "accommodations/", views.AccommodationList.as_view(), name="accommodations-list"
    ),
    path(
        "accommodations/<int:pk>/",
        views.AccommmodationDetail.as_view(),
        name="accommodation-detail",
    ),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("", views.api_root),
    path("login/", views.UserLogin.as_view(), name="user-login"),
    path("logout/", views.UserLogout.as_view(), name="user-logout"),
    path("register/", views.UserRegister.as_view(), name="user-register"),
    path("token/", views.GetCSRFToken.as_view(), name="get-token"),
]
