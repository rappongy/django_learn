from django.contrib import admin
from django.urls import include, path

# You should always use include() when you include other URL patterns.
# admin.site.urls is the only exception to this.
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
