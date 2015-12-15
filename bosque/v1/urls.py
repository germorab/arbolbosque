from rest_framework import routers

from django.conf.urls import patterns, url, include

from bosque.v1.views import CategoryViewSet, ArticleViewSet

# Routers
routers_forest = routers.DefaultRouter()
routers_forest.register(r'categories', CategoryViewSet)
routers_forest.register(r'articles', ArticleViewSet)

# Raw urls for complex services
complex_services_urls = patterns(
    '',
)

urlpatterns = patterns(
    '',
    url(r'^', include(complex_services_urls)),
)

urlpatterns += routers_forest.urls

# Without patterns
# urlpatterns = router_accounts.urls
