from django.urls import path
from .views import upload_csv, get_csv_data, get_user_files

urlpatterns = [
    path('upload/', upload_csv, name='upload-csv'),
    path('<int:file_id>/data/', get_csv_data, name='get-csv-data'),
    path('my/', get_user_files, name='get-user-files'),
]