link utama: https://cargoship.adaptable.app
link main : https://cargoship.adaptable.app/main

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat sebuah projek Django baru
        + Membuat direktori baru dengan nama cargoship
        + Menginisialisasi direktori tersebut menjadi repositori git dengan perintah "git init"
        + Membuat repositori github baru dengan nama "cargoship" dan visibility public
        + Membuat virtual environment pada repo tersebut dengan perintah "python -m venv env"
        + Membuat file teks baru dengan nama "requirements.txt" lalu mengisinya dengan beberapa dependencies sesuai dengan keperluan
            ```
            django
            gunicorn
            whitenoise
            psycopg2-binary
            requests
            urllib3 
            ```
        + Menjalankan virtual environment dengan menjalankan script "env\Scripts\activate.bat"
        + Meng-install dependencies tersebut dengan perintah "pip install -r requirements.txt" 
        + Menambah file .gitignore yaitu file yang berisi daftar-daftar file atau direktori yang akan diabaikan oleh git
            ```
            # Django
            *.log
            *.pot
            *.pyc
            __pycache__
            db.sqlite3
            media

            # Backup files
            *.bak 

            # If you are using PyCharm
            # User-specific stuff
            .idea/**/workspace.xml
            .idea/**/tasks.xml
            .idea/**/usage.statistics.xml
            .idea/**/dictionaries
            .idea/**/shelf

            # AWS User-specific
            .idea/**/aws.xml

            # Generated files
            .idea/**/contentModel.xml

            # Sensitive or high-churn files
            .idea/**/dataSources/
            .idea/**/dataSources.ids
            .idea/**/dataSources.local.xml
            .idea/**/sqlDataSources.xml
            .idea/**/dynamic.xml
            .idea/**/uiDesigner.xml
            .idea/**/dbnavigator.xml

            # Gradle
            .idea/**/gradle.xml
            .idea/**/libraries

            # File-based project format
            *.iws

            # IntelliJ
            out/

            # JIRA plugin
            atlassian-ide-plugin.xml

            # Python
            *.py[cod] 
            *$py.class 

            # Distribution / packaging 
            .Python build/ 
            develop-eggs/ 
            dist/ 
            downloads/ 
            eggs/ 
            .eggs/ 
            lib/ 
            lib64/ 
            parts/ 
            sdist/ 
            var/ 
            wheels/ 
            *.egg-info/ 
            .installed.cfg 
            *.egg 
            *.manifest 
            *.spec 

            # Installer logs 
            pip-log.txt 
            pip-delete-this-directory.txt 

            # Unit test / coverage reports 
            htmlcov/ 
            .tox/ 
            .coverage 
            .coverage.* 
            .cache 
            .pytest_cache/ 
            nosetests.xml 
            coverage.xml 
            *.cover 
            .hypothesis/ 

            # Jupyter Notebook 
            .ipynb_checkpoints 

            # pyenv 
            .python-version 

            # celery 
            celerybeat-schedule.* 

            # SageMath parsed files 
            *.sage.py 

            # Environments 
            .env 
            .venv 
            env/ 
            venv/ 
            ENV/ 
            env.bak/ 
            venv.bak/ 

            # mkdocs documentation 
            /site 

            # mypy 
            .mypy_cache/ 

            # Sublime Text
            *.tmlanguage.cache 
            *.tmPreferences.cache 
            *.stTheme.cache 
            *.sublime-workspace 
            *.sublime-project 

            # sftp configuration file 
            sftp-config.json 

            # Package control specific files Package 
            Control.last-run 
            Control.ca-list 
            Control.ca-bundle 
            Control.system-ca-bundle 
            GitHub.sublime-settings 

            # Visual Studio Code
            .vscode/* 
            !.vscode/settings.json 
            !.vscode/tasks.json 
            !.vscode/launch.json 
            !.vscode/extensions.json 
            .history
            ```
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
        + Melakukan migrasi model dengan perintah "python manage.py makemigrations" lalu melakukan migrasi ke basis data lokal dengan perintah "python manage.py migrate"
    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
        + Membuat file "views.py" pada folder main
        + Di dalam file tersebut, mengimport "render" dari "django.shortcuts"
        + Membuat fungsi show_main dengan parameter "request" yang berguna untuk menampilkan app main sesuai dengan template
        + Membuat variable dictionary bernama context dengan isi sebagai berikut:
            ```
            context = {
                'Cargo1':
                {
                    'Item1': 
                    {
                        'name': 'Tomato',
                        'owner': 'Farrell',
                        'type': 'Consumable',  
                        'ammount': '10',
                        'weight': '1.3'
                    },
                    'Item2':
                    {
                        'name': 'Spoon',
                        'owner': 'Farrell',
                        'type': 'Tools',  
                        'ammount': '8',
                        'weight': '0.8'
                    },
                    'Item3':
                    {
                        'name': 'Phone',
                        'owner': 'Hanau',
                        'type': 'Electronic',
                        'ammount': '5',
                        'weight': '1'
                    }
                },
                'Cargo2':
                {
                    'Item1':
                    {
                        'name': 'Gasoline',
                        'owner': 'Unknown',
                        'type': 'Flammable',
                        'ammount': '2',
                        'weight': '5.7'
                    },
                    'Item2':
                        {
                            'name': 'Diesel',
                            'owner': 'Unknown',
                            'type': 'Flammable',
                            'ammount': '3',
                            'weight': '9.6'
                        }
                }
            }
            ```
            + Mereturn "render (request, 'main.html', context)" dimana 'main.html' merupakan template yang akan digunakan
            + Membuat folder "templates" pada direktori "main" dan di dalamnya, membuat file "main.html"
            + Mengisi main.html dengan nama, kelas, dan Item yang ada dalam context. Karena dalam context terdapat beberapa Item, maka dapat menggunakan for-each loop untuk mengambil setiap Item dari dalam masing-masing "cargo"
            + Mengecek apakah tampilan sudah sesuai dengan keinginan dengan menjalankan server dan mengunjungi http://127.0.0.1:8000/main
        - Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
            + Menghubungkan repositori lokal dengan repositori github dengan perintah "git remote add origin https://github.com/FarrellMuhammadHanau/cargoship.git"
            + Menyimpan repositori lokal / perubahan repositori lokal ke github dengan perintah "git add ." untuk menandai bahwa semua file siap untuk di commit, lalu "git commit -u <komentar>" untuk menyimpan perubahan lalu menyimpannya ke dalam github dengan perintah "git push -u origin main".
            + Setelah itu membuka web Adaptable.io lalu tekan tombol "new app" dan pilih "Connect an Existing Repository" Lalu pilih repo "cargoship"
            + Setelah itu pilih "Python App Template" sebagai template dan "PostgreSQL" sebagai basis data
            + Menyesuaikan versi python yang ada pada lokal ("Versi 3.10") lalu pada bagian "Start Command" tambahkan perintah "python manage.py migrate && gunicorn cargoship.wsgi"
            + Memasukan nama aplikasi dan mencentang "HTTP Listener on Port" lalu menekan tombol "Deploy App"

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara "urls.py", "views.py", "models.py" dan berkas html.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual environment merupakan suatu ruang lingkup virtual yang memungkinkan kita untuk mengisolasi dependencies yang kita butuhkan dengan dependencies yang ada pada mesin lokal. Fitur ini sangat berguna karena aplikasi web yang kita buat terkadang membutuhkan versi dependencies yang berbeda dengan yang ada pada komputer kita. Namun meskipun begitu, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment dengan syarat bahwa versi dependencies yang digunakan dalam membuat aplikasi web tersebut sama dengan versi dependencies yang ada pada mesin lokal. 

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    MVC (Model-View-Control), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) merupakan pola desain yang digunakan dalam mendesain suatu software. Elemen-elemen pada software dipisah sesuai dengan pola desain tersebut untuk memudahkan developer dalam mengelola dan mengembahkan software tersebut.
    - MVC membagi komponen-komponen aplikasi menjadi:
        + Model berfungsi dalam mengelola data
        + View berfungsi dalam mengatur User Interface atau UI dari suatu aplikasi 
        + Control berfungsi sebagai penghubung antara Model dengan View. Control dapat memanipulasi data menggunakan model dan me-render hasil akhir sesuai dengan view.
    - MVT membagi komponen-komponen aplikasi menjadi:
        + Model berfungsi dalam mengelola data
        + View berfungsi sebagai penghubung antara Model dan Template. View dapat mengambil data dari basis data melalui Model dan menampilkan data tersebut menggunakan Template
        + Template berfungsi dalam mengatur tampilan dan menampilkan data melalui View
    - MVVM membagi komponen-komponen aplikasi menjadi:
        + Model berfungsi dalam mengelola data
        + View berfungsi dalam mengatur User Interface dan terhubung dengan ViewModel melalui Data Binding
        + ViewModel berfungsi dalam menghubungkan Model dengan View
    Perbedaan ketiga pola desain tersebut terletak pada elemen penghubungnya dimana pada MVC, elemen penghubung terletak pada Control, pada MVT, elemen penghubungnya adalah View, sementara pada MVVM, elemen penghubungnya pada ViewModel. Selain itu, pada MVC, hubungan antara View dan Control satu arah sementara pada MVVM, hubungan antara View dan ViewModel dua arah karena adanya Data Binding

## Referensi:
Gallardo, Estefania Garcia. (2023). *What is MVVM Architecture?*. Retrieved from https://builtin.com/software-engineering-perspectives/mvvm-architecture