from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # spajanje sa blog/url
    path('blog/', include('blog.urls', namespace='blog')),

]
