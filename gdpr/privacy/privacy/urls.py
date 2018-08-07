"""privacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', views.preprocess),
    url(r'^register/$', views.register_user),
    url(r'^login/$', views.login_user),
    url(r'^add_attribute/$', views.add_attribute),
    url(r'^add_suppression_configuration/(\d+)/$',
        views.add_suppression_configuration),
    url(r'^add_deletion_configuration/(\d+)/$',
        views.add_deletion_configuration),
    url(r'^dashboard/$',
        views.show_dashboard),
    url(r'^add_alias/(\d+)/$',
        views.add_alias),
    url(r'^anonymize/$', views.anonymize),
    url(r'^logout/$', views.logout_user),
    url('^$', views.show_dashboard),
    url(r'^add_regex_pattern/(\d+)/$',
        views.add_regex_pattern),
    url(r'^add_generalization_configuration/(\d+)/$',
        views.add_generalization_configuration),
    url(r'^anonymize_text_api/$', views.anonymize_text_api),
    url(r'^api_token_management/$', views.api_token_management),
    url(r'^regenerate_api_token/$', views.regenerate_api_token),
    url(r'^token_level_api/$', views.token_level_api),
    url(r'^add_document_to_knowledgebase/$',
        views.add_document_to_knowledgebase),
    url(r'^tf_idf_anonymize/$', views.tf_idf_anonymize),
    url(r'^upload_file_to_knowledgebase/$',
        views.upload_file_to_knowledgebase),
    url(r'^upload_file_to_knowledgebase_api/$',
        views.upload_file_to_knowledgebase_api),
    url(r'^anonymize_uploaded_file_api/$',
        views.anonymize_uploaded_file_api),
    url(r'^anonymize_uploaded_file_gui/$',
        views.anonymize_uploaded_file_gui),
    url(r'^reset_setup_application/$',
        views.reset_setup_application),
    url(r'^delete_attribute/(\d+)/$',
        views.delete_attribute),
    url(r'^delete_alias/(\d+)/$',
        views.delete_alias),
    url(r'^delete_regex/(\d+)/$',
        views.delete_regex),

]
