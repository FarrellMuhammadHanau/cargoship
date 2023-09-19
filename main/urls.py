from django.urls import path
from main.views import show_main, create_item, create_container, show_json, show_xml, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item/',create_item, name='create_item'),
    path('create-container/', create_container, name='create_container'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),

]