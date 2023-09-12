1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat sebuah projek Django baru
        + Membuat direktori baru dengan nama cargoship
        + Menginisialisasi direktori tersebut menjadi repositori git dengan perintah "git init"
        + Membuat virtual environment pada repo tersebut dengan perintah "python -m venv env"
        + Membuat file teks baru dengan nama "requirements.txt" lalu mengisinya dengan beberapa dependencies sesuai dengan keperluan
        + Menjalankan virtual environment dengan menjalankan script "env\Scripts\activate.bat"
        + Meng-install dependencies tersebut dengan perintah "pip install -r requirements.txt" 
        + Menambah file .gitignore yaitu file yang berisi daftar-daftar file atau direktori yang akan diabaikan
        + Membuat projek django dengan perintah "django-admin startproject cargoship ."
        + Menambahkan "*" pada ALLOWED_HOST di settings.py yang berada di direktori cargoship
        + Menjalankan server django dengan perintah "python manage.py runserver" lalu buka link http://127.0.0.1:8000 untuk mengecek apakah server sudah dapat berjalan dengan baik atau belum.
        + Menekan tombol "CTRL-C" untuk mematikan server
    - Membuat aplikasi dengan nama main pada proyek tersebut
        + Membuat aplikasi baru bernama main dengan perintah "python manage.py startapp main"
        + Memasukan main ke dalam daftar aplikasi proyek dengan menambahkan "main" pada variable INSTALLED_APPS yang ada di settings.py yang berada pada directori cargoship
    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main
        + Mengimport "include" dari "django.urls"
        + Menambahkan "path('main/', include(main.urls)) di dalam variable list "urlpatterns" dimana 'main/' sendiri merupakan path url dari applikasi main 
        + Mengecek apakah applikasi main sudah dapat dijalankan dengan membuka link http://127.0.0.1:8000/main
    - Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sesuai dengan yang ada pada soal
        + Pada main\models.py, mengimport "models" dari "django.db"
        + Membuat class baru bernama "Item" yang meng-inherit dari class "models.Model"
        + Menambahkan beberapa attribut pada kelas Item sebagai berikut:
            ```
            class Item(models.Model):
                name = models.CharField(max_length=255)
                owner = models.CharField(max_length=255)
                type = models.CharField(max_length=255)
                amount = models.IntegerField()
                weight = models.FloatField()
                description = models.TextField()
            
            ```
