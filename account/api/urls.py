from django.urls import path, include

urlpatterns = [
    path('v1/', include('account.api.v1.urls'))
]
