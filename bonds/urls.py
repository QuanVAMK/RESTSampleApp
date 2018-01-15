from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from bonds import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^bonds/$',
        views.BondList.as_view(),
        name='bond-list'),
    url(r'^bonds/(?P<pk>[0-9]+)/$',
        views.BondDetail.as_view(),
        name='bond-detail'),
    url(r'^companies/$',
        views.CompanyList.as_view(),
        name='company-list'),
    url(r'^companies/(?P<pk>[0-9]+)/$',
        views.CompanyDetail.as_view(),
        name='company-detail'),
]

urlpatterns += [
        url(r'^api-auth/',
        include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
