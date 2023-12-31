link utama: https://cargoship.adaptable.app

link main : https://cargoship.adaptable.app/main

# Tugas 2

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
        - Membuat sebuah routing pada "urls.py" aplikasi main untuk memetakan fungsi yang telah di buat pada "views.py"
            + Mengimport "path" dari "django.urls" dan show_main dari "main.views"
            + menambahkan *path* baru pada pada variable "urlpatterns" dengan cara menambahkan "path('', show_main, name='show_main')"
        - Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
            + Menghubungkan repositori lokal dengan repositori github dengan perintah "git remote add origin https://github.com/FarrellMuhammadHanau/cargoship.git"
            + Menyimpan repositori lokal / perubahan repositori lokal ke github dengan perintah "git add ." untuk menandai bahwa semua file siap untuk di commit, lalu "git commit -u <komentar>" untuk menyimpan perubahan lalu menyimpannya ke dalam github dengan perintah "git push -u origin main".
            + Setelah itu membuka web Adaptable.io lalu tekan tombol "new app" dan pilih "Connect an Existing Repository" Lalu pilih repo "cargoship"
            + Setelah itu pilih "Python App Template" sebagai template dan "PostgreSQL" sebagai basis data
            + Menyesuaikan versi python yang ada pada lokal ("Versi 3.10") lalu pada bagian "Start Command" tambahkan perintah "python manage.py migrate && gunicorn cargoship.wsgi"
            + Memasukan nama aplikasi dan mencentang "HTTP Listener on Port" lalu menekan tombol "Deploy App"

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara "urls.py", "views.py", "models.py" dan berkas html.

    ![Alt text](image.png)
    - URLS atau urls.py merupakan bagian yang menentukan pola url aplikasi. Pola url ini akan merujuk pada Views dari aplikasi tersebut.
    - Views atau views.py akan menampilkan laman sesuai dengan Template yang dipilih dengan data yang sesuai dengan Model.
    - Template menentukan tampilan dari website dan dapat menampilkan data yang didapat melewati Views
    - Model atau models.py menentukan bentuk atau struktur dari data-data yang ada pada database
    - Database merupakan tempat dimana data-data aplikasi disimpan

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    *Virtual environment* merupakan suatu ruang lingkup virtual yang memungkinkan kita untuk mengisolasi *dependencies* yang kita butuhkan dengan *dependencies* yang ada pada mesin lokal. Fitur ini sangat berguna karena aplikasi web yang kita buat terkadang membutuhkan versi *dependencies* yang berbeda dengan yang ada pada komputer kita. Namun meskipun begitu, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment* dengan syarat bahwa versi *dependencies* yang digunakan dalam membuat aplikasi web tersebut sama dengan versi *dependencies* yang ada pada mesin lokal. 

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    MVC (Model-View-Control), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) merupakan pola desain yang digunakan dalam mendesain suatu software. Elemen-elemen pada software dipisah sesuai dengan pola desain tersebut untuk memudahkan developer dalam mengelola dan mengembahkan software tersebut.
    - MVC membagi komponen-komponen aplikasi menjadi:
        + Model berfungsi dalam mengelola data
        + View berfungsi dalam mengatur *User Interface* atau *UI* dari suatu aplikasi 
        + Control berfungsi sebagai penghubung antara Model dengan View. Control dapat memanipulasi data menggunakan model dan me-*render* hasil akhir sesuai dengan view.
    - MVT membagi komponen-komponen aplikasi menjadi:
        + Model berfungsi dalam mengelola data
        + View berfungsi sebagai penghubung antara Model dan Template. View dapat mengambil data dari basis data melalui Model dan menampilkan data tersebut menggunakan Template
        + Template berfungsi dalam mengatur tampilan dan menampilkan data melalui View
    - MVVM membagi komponen-komponen aplikasi menjadi:
        + Model berfungsi dalam mengelola data
        + View berfungsi dalam mengatur User Interface dan terhubung dengan ViewModel melalui *Data Binding*
        + ViewModel berfungsi dalam menghubungkan Model dengan View
    Perbedaan ketiga pola desain tersebut terletak pada elemen penghubungnya dimana pada MVC, elemen penghubung terletak pada Control, pada MVT, elemen penghubungnya adalah View, sementara pada MVVM, elemen penghubungnya pada ViewModel. Selain itu, pada MVC, hubungan antara View dan Control satu arah sementara pada MVVM, hubungan antara View dan ViewModel dua arah karena adanya Data Binding

## Referensi:
Gallardo, Estefania Garcia. (2023). *What is MVVM Architecture?*. Retrieved from https://builtin.com/software-engineering-perspectives/mvvm-architecture

# Tugas 3

1. Apa perbedaan form POST dan form GET dalam django?

    Pada django, form POST digunakan untuk mengirimkan data pada server dengan tujuan mengubah atau menambahkan data pada server tersebut. Sementara itu, form GET digunakan untuk mengambil data pada server tanpa mengubah data pada server dimana form tersebut akan meminta input berupa *identifier* atau kata kunci untuk mencari data yang diinginkan.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    - XML menggunakan tag dan atribut untuk mendefinisikan suatu struktur data. Pada umumnya, XML lebih mudah untuk dibaca bagi manusia sehingga mudah untuk *debugging*. Selain itu, XML dapat merepresentasikan berbagai data yang kompleks.
    - JSON menggunakan *key-value pair* dalam menentukan menyimpan suatu data dimana key merupakan tipe data serta value adalah nilai dari data tersebut. Kelebihan JSON yang membuatnya sering dipakai dalam API web adalah kompabilitasnya dengan javascript dimana javascript dapat mengubah JSON menjadi objek javascript dengan mudah.
    - HTML merupakan *markup language* yang digunakan untuk membuat tampilan dari suatu website. Berbeda dengan XML dan JSON, HTML lebih cocok digunakan dalam presentasi suatu data dibandingkan untuk pengiriman data.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    Alasan mengapa JSON sering digunakan pada web modern yaitu karena Kompatibilitasnya dengan bahasa pemrograman JavaScript, dimana JavaScript dapat mengubah isi dari JSON menjadi objek javascript. Selain itu, JSON memiliki format data yang lebih ringan dan sederhana dibandingkan dengan XML. Selain itu, JSON mudah untuk di*parsing* dengan cepat sehingga memudahkan proses transfer data. JSON juga *compatible* dengan beberapa bahasa pemrograman selain javascript seperti python, java, C#, php, dll.

4. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

    - Membuat input form untuk menambahkan objek model pada app sebelumnya
        + Mengubah routing aplikasi main dari 'main/' menjadi '' pada file 'urls.py' di folder cargoship agar link url menjadi lebih simple
        + Membuat folder 'templates' pada root lalu membuat file 'base.html' didalamnya sebagai kerangka dari template-template yang akan digunakan dikedepannya.
        ```
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta
                    name="viewport"
                    content="width=device-width, initial-scale=1.0"
                />
                {% block meta %}
                {% endblock meta %}
            </head>

            <body>
                {% block content %}
                {% endblock content %}
            </body>
        </html>
        ```
        + Menambahkan "'DIRS': [DIRSBASE_DIR / 'templates']" pada baris 'TEMPLATES' yang ada pada 'settings.py' untuk memberi tahu dimana letak template tersebut
        ```
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR / 'templates'],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
        ```
        + Membuat file 'forms.py' di folder 'main' lalu mengimport beberapa module/class/fungsi yang dibutuhkan
        ```
        from django.forms import ModelForm, ChoiceField
        from main.models import Item, Container
        ``` 
        + membuat class ItemForm dan ContainerForm yang masing-masing menerima data Item dan Container baru (pada tugas ini, saya menambahkan model data baru yaitu Container dengan relasi one to many dengan Item).
        ```
        class ItemForm(ModelForm):
            class Meta:
                model = Item
                fields = ["name", "owner", "type", "amount", "weight", "container", "description"]

            type_choices = [
                ('Consumable', 'Consumable'),
                ('Tools', 'Tools'),
                ('Electronic', 'Electronic'),
                ('Fuel', 'Fuel'),
                ('Valuables', "Valuables")
            ]

            type = ChoiceField(choices=type_choices)

        class ContainerForm(ModelForm):
            class Meta:
                model = Container
                fields = ["name"]
        ```
        + Mengimport beberapa module/class/fungsi yang dibutuhkan pada file 'views.py'
        ```
        from main.forms import ItemForm, ContainerForm
        from django.http import HttpResponseRedirect, HttpResponse
        from django.urls import reverse
        ```
        + Membuat fungsi 'create_item' dan 'create_container' dimana didalam fungsi tersebut akan dicek apakah input form valid atau serta untuk container, nama tidak boleh duplikat.
        ```        
        def create_item(request):
            form = ItemForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return HttpResponseRedirect(reverse('main:show_main'))
            
            context = {'form': form}
            return render(request, "create_item.html", context)

        def create_container(request):
            form = ContainerForm(request.POST or None)
            if form.is_valid() and request.method == "POST":
                name = form.cleaned_data['name']
                if (name not in [container.name for container in Container.objects.all()]):
                    form.save()
                    return HttpResponseRedirect(reverse('main:show_main'))
            
            context = {'form': form}
            return render(request, "create_container.html", context)
        ```
        + Membuat template 'create_container.html' yang akan dirender oleh fungsi 'create_container' pada 'views.py'
        ```
        {% extends 'base.html' %} 

        {% block content %}
        <h1>Add New Container</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Add Container"/>
                    </td>
                </tr>
            </table>
        </form>

        {% endblock %}
        ```
        + Membuat template 'create_item.html' yang akan dirender oleh fungsi 'create_item' pada 'views.py'
        ```
        {% extends 'base.html' %} 

        {% block content %}
        <h1>Add New Item</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Add Item"/>
                    </td>
                </tr>
            </table>
        </form>

        {% endblock %}
        ```
        + Mengimport fungsi 'create_item' dan 'create_container' dari 'main.views'
        + Menambahkan path untuk fungsi views tersebut sebagai berikut:
        ```
        path('create-item/',create_item, name='create_item'),
        path('create-container/', create_container, name='create_container'),
        ```
        + Mengetes apakah form tersebut sudah dapat berjalan dengan menjalankan server local lalu mengakses 'http://localhost:8000/create-item/' dan 'http://localhost:8000/create-container/'
    
    - Menambahkan fungsi views untuk melihat objek dalam format HTML
        + Mengubah fungsi 'show_main' pada 'views.py' agar dapat menampilkan data yang ada pada basis data
        ```
        def show_main(request):
            containers = Container.objects.all()
            context = {
                'name': 'Farrell Muhammad Hanau',
                'class': 'PBP-C',
                'shipper': 'EfEmEitch Express',
                'containers': containers

            }
            
            return render (request, 'main.html', context)
        ```
        + Di dalam template 'main.html' akan dilakukan loop untuk setiap objek Container. Hal ini dilakukan untuk menampilkan setiap objek Item yang ada didalam Container tersebut
    
    - Membuat fungsi views untuk melihat objek dalam format XML dan JSON
        + Mengimport 'HttpResponse' dari 'django.http' serta 'serializers' dari 'django.core'
        + Membuat fungsi 'show_json' untuk format json dan 'show_xml' untuk format XML.
        ```
        def show_json(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        def show_xml(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
        + 'serializers.serialize("json", data)' dan 'serializers.serialize("xml", data)' digunakan untuk mengubah data menjadi format JSON atau XML.
    
    - Membuat fungsi views untuk melihat objek dalam format XML dan JSON
        + Membuat fungsi 'show_json_by_id' dan 'show_xml_by_id' pada 'views.py' yang keduanya memiliki 2 parameter yaitu request dan id, dimana parameter id tersebut digunakan untuk mem-*filter* objek sesuai dengan id dari objek tersebut
        ```
        def show_json_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        def show_xml_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        ```
    
    - Membuat routing URL untuk masing-masing views yang telah ditambahkan
        + Mengimport kelima fungsi views tersebut dari 'main.views.py' kedalam 'urls.py' pada main.
        ```
        from main.views import show_main, show_json, show_xml, show_xml_by_id, show_json_by_id

        ``` 
        + Pada 'urlpatterns', menampahkan path sebagai berikut
        ```
        urlpatterns = [
            ........
            path('', show_main, name='show_main'),
            path('json/', show_json, name='show_json'),
            path('xml/', show_xml, name='show_xml'),
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
            ........
        ]
        ```
        + Id pada akhir url 'json/<int:id>/' dan 'xml/<int:id>/' akan ditangkap oleh fungsi 'show_json_by_id' dan 'show_xml_by_id' yang digunakan untuk menyaring objek

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
    - format HTML
        ![Alt text](image-1.png)
    - format JSON
        ![Alt text](image-2.png)
    - format XML
        ![Alt text](image-3.png)
    - format JSON dengan ID (objek yang dipilih memiliki id = 6)
        ![Alt text](image-4.png)
    - format XML dengan ID (objek yang dipilih memiliki id = 6)
        ![Alt text](image-5.png)

# Tugas 4

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
    Django UserCreationForm adalah formulir bawaan Django yang digunakan untuk membuat user baru. Kelebihan dari form ini adalah kemudahan dalam menggunakannya dimana kita tidak perlu membuat class form baru untuk melakukan register dan disertai validasi bawaan. Namun, kelemahan dari form ini adalah kurangnya fitur seperti Email, alamat, maupun validasi kustom.

2. Apa perbedaan autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    Dalam Django, autentikasi adalah proses menverifikasi identitas user. Sementara itu, otorisasi adalah proses memverifikasi apakah user memiliki akses ke suatu fitur. Kedua proses tersebut penting karena dalam Django, autentikasi digunakan pada proses login, untuk mengecek apakah user ada atau tidak beserta passwordnya, sementara otorisasi penting menentukan hal apa yang user boleh lakukan misalkan apakah user boleh melakukan request DELETE atau PATCH, dll.

3. Apa itu Cookies dalam konteks aplikasi web, dan bagaimana django menggunakan cookies untuk mengelola data sesi pengguna?
    Cookies dalam konteks aplikasi web adalah kumpulan data kecil yang digunakan untuk menyimpan informasi di klien yang nantinya dapat diakses oleh web. Di Django, cookies digunakan untuk menyimpan iD sesi user yang nantinya id tersebut dapat digunakan untuk memverifikasi sesi user.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    Penggunaan cookies pada web pada dasarnya aman jika digunakan dengan baik, namun ada beberapa risiko yang dapat terjadi jika suatu web menggunakan cookies diantara lain yaitu pencurian data pribadi, melacak aktivitas pengguna, melakukan serangan SCRF, dll.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    - Mengimplementasikan fungsi registrasi, login, dan logout
        + Dalam 'views.py' di main, import UserCreationForm untuk membuat form register, messages untuk menampilkan message
        + Membuat fungsi register pada 'views.py' yang digunakan untuk membuat user yang menggunakan UserCreationForm dan menggunakan 'register.html' sebagai templatenya. Didalamnya akan dicek request apa yang digunakan sekarang.
        + Berikut fungsi register
        ```
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
                
            context = {'form':form}
            return render(request, 'register.html', context)
        ```
        + Berkut template 'register.html'
        ```
        {% extends 'base.html' %}

        {% block meta %}
            <title>Register</title>
        {% endblock meta %}

        {% block content %}  

        <div class = "login">
            
            <h1>Register</h1>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>

            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}

        </div>  

        {% endblock content %}
        ```
        + Menghubungkan fungsi register tersebut dengan menambahkan url baru di urls.py sebagai berikut
        ```
        path('register/', register, name='register'),
        ```
        + Mengimport authenticate, login, logout, dan login_required
        + Membuat fungsi login yang akan mengecek user dengan fungsi authenticate yang sudah di import. Jika user ada maka akan kembali ke main, jika user belum benar maka akan merender template 'login.html'.
        + Berikut fungsi login
        ```
        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse("main:show_main"))
                else:
                    messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            context = {}
            return render(request, 'login.html', context)
        ```
        + Berikut template 'login.html'
        ```
        {% extends 'base.html' %}

        {% block meta %}
            <title>Login</title>
        {% endblock meta %}

        {% block content %}

        <div class = "login">

            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                            
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>

                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
                
            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

        </div>

        {% endblock content %}
        ```
        + Menambahkan decorator 'login_required' pada show_main agar fungsi main tersebut tidak dapat diakses sebelum user login.
        + Membuat fungsi logout_user pada 'views.py' sebagai berikut
        ```
        def logout_user(request):
            logout(request)
            return HttpResponseRedirect(reverse('main:login'))
        ```

    - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal
        + Membuka link http://127.0.0.1:8000 lalu akan diminta untuk login
        + Menekan hyperlink "register now" dan membuat 2 akun
        + Lalu login akun yang telah dibuat tersebut dan menekan tombol create container secukupnya
        + Setelah membuat container, membuat 3 item (dummy data) dan memasukkannya ke dalam kontainer yang diinginkan

    - Menghubungkan model item item dengan user
        + Pada models.py import User dari django.contrib.auth.models
        + Pada class Container dan Item, tambahkan field baru bernama user yang merupakan relasi one to many dimana user adalah one dan Item/Container adalah many.
        ```
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ```
        + Membuat migrasi tersebut dengan menjalankan "python manage.py makemigrations"
        + Memasukan nilai 1 sebagai nilai default dari user
        + Lakukan migrasi dengan menjalankan "python manage.py migrate"
    
    - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
        + Pada fungsi login pada views.py, tambahkan cookies 'last_login' sebagai berikut
        ```
        -----------------
        if user is not None:
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main"))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
        -----------------
        ```
        + Pada show_main, filter Container sesuai dengan user yang sedang login sebagai berikut
        ```
        containers = Container.objects.filter(user=request.user)
        ```
        + Pada context, tambahkan key 'shipper' dengan value user yang sedang login dengan menggunakan 'request.user.username' dan tambahkan key 'last_login' dengan value cookies 'last_login' yang didapat dengan menggunakan 'request.COOKIES['last_login']'
        ```
        context = {
            'name': 'Farrell Muhammad Hanau',
            'class': 'PBP-C',
            'shipper': request.user.username,
            'containers': containers,
            'last_login': request.COOKIES['last_login'],
            'total_item': total_item
        }
        ```
        + Pada logout, akan didelete cookies 'last_login' yang telah dibuat
        ```
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
        ```

# Tugas 5

1. Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya.
    Dalam html dan css, terdapat 3 selector yaitu element selector, id selector, dan class selector. Element selctor digunakan untuk mengubah property seluruh element dengan tag yang sama. ID selector digunakan untuk mengubah elemen yang memiliki atribut ID tertentu. Class selector digunakan untuk memodifikasi dan mengelompokan elemen-elemen dengan karakteristik yang sama.

2. Jelaskan HTML5 tag yang kamu ketahui
    - tag "html" menandakan awal dan akhir dari dokumen html
    - tag "head" berisi informasi tentang dokumen html, seperti judul
    - tag "meta" berisi metadata dokumen html
    - tag "title" digunakan untuk menentukan judul
    - tag "style" digunakan untuk memberikan *style* css pada elemen
    - tag "script" merupakan tag berisi *script* javascript pada dokumen html
    - tag "hx" merupakan tag heading dimana 1 memiliki hirarki tertinggi dan 5 hirarki terendah
    - tag "p" merupakan tag yang berisi teks paragraf
    - tag "div" merupakan tag yang digunakan untuk mengelompokan dan membagi beberapa elemen ke bagian-bagian
    - tag "form" digunakan untuk membuat form html
    - tag "ul", "ol" dan "li". "ul" dan "ol" merupakan tag yang digunakan untuk menampung beberapa item "li"
    - tag "a" digunakan untuk membuat hyperlink
    - tag "body" merupakan bagian utama dari web
    -  tag "link" digunakan untuk menghubungkan file html dengan file external

3. Jelaskan perbedaan antara margin dan padding
    Pada css, terdapat beberapa properti yang digunakan untuk memberikan jarak pada suatu elemen 2 diantaranya yaitu margin dan padding. Margin digunakan untuk memberikan jarak luar yaitu jarak antara elemen satu dengan elemen lainnya. Sementara itu, padding digunakan untuk memberikan jarak dalam, yaitu jarak antara content dari elemen dengan border atau batas dari elemen.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    - Framework bootstrap adalah framework yang menyediakan komponen dan gaya yang siap digunakan. Framework ini dapat  digunakan untuk mendesain web dengan cepat karena sangat mudah digunakan dan tidak perlu menuliskan kode css.
    - Framework Tailwind adalah framework menyediakan kelas-kelas utilitas yang telah didefinisikan. Framework ini memungkinkan pengembang untuk memegang kontrol lebih dibandingkan bootstrap.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    - Menambahkan bootstrap dan js pada proyek
        + Pada "base.html" di folder "templates" pada root folder, tambahkan beberapa link dan script sebagai berikut
        ```
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
        ```
    - Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin
        + Pada base.html di folder templates yang ada di root. Tambahkan block baru yaitu block navigation sebagai berikut
        ```
        <body>
            {% block navigation %}
            {% endblock navigation %}

            {% block content %}
            {% endblock content %}
        </body>
        ```
        + Pada folder templates di root, tambahkan file "navigation.html"
        + Pada file tersebut buat navbar yang sudah disediakan oleh bootstrap. Berikut adalah isi dari file tersebut
        ```
        {% extends 'base.html' %}
        {% load static %}

        {% block navigation %}
        <nav class="navbar navbar-expand-lg bg-dark-subtle pb-2 pt-2 mb-3">
            <div class="container-fluid">
                <span class="navbard-brand h2">CargoShip</span>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-3" >
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'main:show_main' %}">Home</a>
                        </li>
                        <li>
                            <a class="nav-link" href="{% url 'main:create_item' %}">Create Item</a>
                        </li>
                        <li>
                            <a class="nav-link" href="{% url 'main:create_container' %}">Create Container</a>
                        </li>

                    </ul>
                    <span class="navbar-text ms-auto">{{shipper}}</span>
                    <ul class="navbar-nav ms-3">
                        <li>
                            <button type="button" class="btn btn-danger btn-sm">
                                <a class="nav-link" href="{% url 'main:logout' %}">Logout</a>
                            </button>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        {% endblock navigation %}
        ```
        + Pada setiap file html di "templates/main" kecuali register.html dan login.html, ubah extends file tersebut dari "base.html" menjadi "navigation.html" untuk menambahkan fitur navigasi.
        + pada login.html atau register.html, masukan form login/register kedalam tag div dan tambahkan beberapa atribut container pada tag div tersebut dan tambahkan beberapa style agar form tersebut berada di tengah layar.
        + Berikut login.html
        ```        
        <div class="container">
            <div class="col-md-6 offset-md-3" style="display: flex; justify-content: center; align-items: center; min-height: 100vh;">
                <div class="login">
                    <div class="text-center">
                        <h1>Login</h1>
                    </div>
                    <form method="POST" action="">
                        {% csrf_token %}
                        <div class="form-group">
                            <label for="username">Username:</label>
                            <input type="text" name="username" id="username" class="form-control" placeholder="Username">
                        </div>
                        <div class="form-group">
                            <label for="password">Password:</label>
                            <input type="password" name="password" id="password" class="form-control" placeholder="Password">
                        </div>
                        <button class="btn btn-primary" type="submit">Login</button>
                    </form>
                    {% if messages %}
                        <ul>
                            {% for message in messages %}
                                <li>{{ message }}</li>
                            {% endfor %}
                        </ul>
                    {% endif %}
                    <p>Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a></p>
                </div>
            </div>
        </div>
        ```
        + Berikut register.html
        ```
        <div class="container">
            <div class="col-md-6 offset-md-3" style="display: flex; justify-content: center; align-items: center; min-height: 100vh;">
                <div class = "login">
                    
                    <div class="text-center">
                        <h1>Register</h1>  
                    </div>

                        <form method="POST" >  
                            {% csrf_token %}  
                            <table>  
                                {{ form.as_table }}  
                                <tr>  
                                    <td></td>
                                    <td><input type="submit" name="submit" value="Daftar" class="btn btn-primary"/></td>  
                                </tr>  
                            </table>  
                        </form>

                    {% if messages %}  
                        <ul>   
                            {% for message in messages %}  
                                <li>{{ message }}</li>  
                                {% endfor %}  
                        </ul>   
                    {% endif %}
                </div>  
            </div>
        </div>
        ```
        + Pada create_container.html dan create_item.html tambahkan atribut 'class' dengan value 'btn btn-primary' yang digunakan untuk memberikan style button pada button submit
        + Buat fungsi edit_item sebagai berikut
        ```
        def edit_item(request, id):
        item = Item.objects.get(pk = id)

        form = ItemForm(request, instance=item)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form,  'shipper':request.user.username}
        return render(request, "edit_item.html", context)
        ```
        + Pada forms.py tambahkan beberapa kode pada constructor dari ItemForm untuk menghandle ketika form digunakan untuk membuat atau mengedit item
        ```
        def __init__ (self, request, instance=None):
            if (instance is None):
                super().__init__(request.POST or None)
            else:
                super().__init__(request.POST or None, instance=instance)

            self.fields['container'].queryset = Container.objects.filter(user=request.user)
        ```
        + import fungsi view pada urls.py dan tambahkan path baru
        ```
        from main.views import edit_item
        .
        .
        .
        .
        path('edit-item/<int:id>', edit_item, name='edit_item'),
        ```
        + Buat templates edit_item.html sebagai berikut
        ```
        {% extends 'navigation.html' %}

        {% load static %}

        {% block content %}

        <h1>Edit Product</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Edit Product" class="btn btn-primary"/>
                    </td>
                </tr>
            </table>
        </form>

        {% endblock %}
        ```

    - Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan approach lain seperti menggunakan Card
        + Pada show_main, tambahkan atribut class pada table dan isi valuenya dengan 'table table-bordered'
        + Bagi row pada table menjadi 2 yaitu header row dan body row dengan menggunakan atribut 'thead' dan 'tbody'
        + Pada button-button yang ada, tambahkan class 'btn btn-primary' untuk memberikan *style* pada button
        + Buatlah tag style dibawah table yang berisi selector elemen td yang digunakan untuk memodifikasi setiap cell pada table agar konten dari cell berada di tengah-tengah cell tersebut dan dengan lebar yang diinginkan. 


# Tugas 6

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
    Pada synchronous programming, program dieksekusi satu per satu secara berurutan dimana perintah setelahnya akan menunggu hingga perintah sebelumnya selesai dieksekusi. Sementara itu, pada asynchronous programming, perintah dapat dieksekusi tanpa menghambat eksekusi program, dimana program dapat mengeksekusi perintah lain selagi menunggu perintah asynchronous selesai.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    Dalam AJAX / JavaScript, event-driven programming adalah pemrograman berbasis event (peristiwa) dimana program dapat memberi response terhadap event tersebut secara asynchronous. Dalam tugas ini, saya menggunakan paradigma ini untuk membuat button increment, decrement, remove, dan search.

3. Jelaskan penerapan asynchronous programming pada AJAX
    Pada AJAX, kita dapat mengambil data atau mengirim data dari/ke server secara asynchronous. Dengan demikian, kita dapat mengupdate halaman web tanpa harus melakukan refrehs/reload halaman.

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
    Fetch Api dapat digunakan tanpa harus mengimport library tambahan, ringan, berbasis promise sehingga mudah untuk dibaca. Sementara itu, jQuery kompatible untuk berbagai browser dengan abstraksi yang konsisten, serta memiliki banyak fitur. Disini, Fetch API lebih baik digunakan untuk aplikasi-aplikasi dengan browser modern sementara itu jQuerey dapat digunakan untuk aplikasi yang membutuhkan browser lama.

5. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
    
    - Ubahlah kode cards data item agar dapat mendukung AJAX GET.
        + Pada main.html buat tag script baru lalu buat fungsi refreshTable yang akan digunakan untuk merefresh halaman secara asynchronous
        + Didalamnya akan di ubah isi dari table yg diinginkan
        ```
        async function refreshTable(){
            document.getElementById("ContentTable").innerHTML = ""
            const data = await search()
            let content = ''
            data.forEach(container => {
                content += `
                <div class="container">
                    <div class="class="row col-md-8 offset-md-2"">
                        <div class="card bg-secondary-subtle" style="margin-bottom: 70px">
                            <div class="card-body">
                                <div class="text-center" style="margin-bottom: 40px;">
                                    <h4 class="card-title">${container.name}</h4>
                                </div>
                                <div class="container" id="container-card">

                `
                const items = JSON.parse(container.item)
                items.forEach(item => {
                    content += `
                    <div class="card bg-dark mx-auto" style="width: 18rem; margin-bottom: 20px; color: white;">
                        <div class="card-body ms-3 mt-3">
                            <h4 class="card-title">${item.fields.name}</h4>
                            <p class="card-text">Owner      : ${item.fields.owner}</p>
                            <p class="card-text">Type       : ${item.fields.type}</p>
                            <p class="card-text">Amount    : ${item.fields.amount}</p>
                            <p class="card-text">Weight     : ${item.fields.weight}</p>
                            <p class="card-text">Description: ${item.fields.description}</p>
                        </div>
                        <div class="card-footer" style="margin-bottom: 30px">
                            <div class="container text-center">
                                <div class="row">
                                    <div class="col">
                                        <button type="button" class="btn btn-success" style="width: 100%;" onClick="incrementItem(${item.pk})">Add</button>
                                    </div>
                                    <div class="col">
                                        <button type="button" class="btn btn-warning" style="width: 100%;" onClick="decrementItem(${item.pk})">Min</button>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col">
                                        <button type="button" class="btn btn-danger" style="width: 100%;" onClick="deleteItem(${item.pk})">Remove</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    `
                })
                        
                content += `
                                </div>
                                <div class="text-center" style="margin-top: 20px;">
                                    <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#CreateItemModal" onclick="initModal('${container.name}', ${container.id})">Add Product</button>
                                </div>
                                <style>
                                    #container-card {
                                        display: grid;
                                        grid-template-columns: repeat(3, 1fr);
                                        gap: 20px;
                                        justify-content: center;
                                    }
                                </style>
                            </div>
                        </div>
                    </div>
                </div>
                `
            })
            document.getElementById("ContentTable").innerHTML = content
        }
        ```

    - Lakukan pengambilan task menggunakan AJAX GET
        + Pada tag script, buat fungsi baru search
        + Disana akan mengambil input dari SearchForm lalu disimpan dengan membuat objek FormData
        + Isi dari FormData tersebut akan dimasukan kedalam query parameter
        ```
        async function search(){
            const data = new FormData(document.querySelector("#SearchForm"))
            name = data.get("SearchField")
            type = data.get("FilterType")
            owner = data.get("FilterOwner")

            let url = "{% url 'main:get_data' %}"
            url += `?Name=${name}&Type=${type}&Owner=${owner}`

            return fetch(url, {
                method: "GET",
            }).then(response => response.json())
        }
        ```
        + Buat fungsi view pada views.py sebagai berikut
        ```
        def get_data(request):
            if request.method == "GET" and "Name" in request.GET and "Type" in request.GET and "Owner" in request.GET:
                name = request.GET.get("Name")
                type = request.GET.get("Type")
                owner = request.GET.get("Owner")
                containers = Container.objects.prefetch_related('item_set').filter(user=request.user)

                # Filter nama
                if name != "":
                    temp = containers
                    for container in temp:
                        isContain = False
                        for item in container.item_set.all():
                            if item.name == name:
                                isContain = True

                        if not isContain:
                            containers = containers.exclude(id=container.id)

                # Filter type
                if type != "Type":
                    temp = containers
                    for container in temp:
                        isContain = False
                        for item in container.item_set.all():
                            if item.type == type:
                                isContain = True

                        if not isContain:
                            containers = containers.exclude(id=container.id)

                # Filter owner
                if owner != "Owner":
                    temp = containers
                    for container in temp:
                        isContain = False
                        for item in container.item_set.all():
                            if item.owner == owner:
                                isContain = True

                        if not isContain:
                            containers = containers.exclude(id=container.id)

                
                data = []
                for container in containers:
                    sub_data = {
                        "name": container.name,
                        "id": container.id,
                        "item": serializers.serialize('json', container.item_set.all())
                    }
                    data.append(sub_data)

                return HttpResponse(json.dumps(data))
            
            return HttpResponseBadRequest("Data tidak valid")
        ```
        + Import fungsi tersebut lalu tambahkan pathnya
        ```
        path('get-data/', get_data, name='get_data'),
        ```

    - Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item
        + Pada main, buat modal untuk menambahkan item sebagai berikut
        ```
        <div class="modal fade" id="CreateItemModal" tabindex="-1" data-bs-backdrop="static">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="ModalTitle"></h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <form id="CreateItemForm">
                            {% csrf_token %}
                            <div class="mb-2">
                                <label for="name" class="col-form-label">Name:</label>
                                <input type="text" class="form-control" id="name" name="name"></input>
                            </div>
                            <div class="mb-2">
                                <label for="owner" class="col-form-label">Owner:</label>
                                <input type="text" class="form-control" id="owner" name="owner"></input>
                            </div>
                            <div class="mb-2">
                                <label for="type" class="col-form-label">Type:</label>
                                <select id="type" name="type" class="form-control">
                                    <option value="Consumable">Consumable</option>
                                    <option value="Tools">Tools</option>
                                    <option value="Electronic">Electronic</option>
                                    <option value="Fuel">Fuel</option>
                                    <option value="Valuables">Valuables</option>
                                </select>
                            </div>
                            <div class="mb-2">
                                <label for="amount" class="col-form-label">Amount:</label>
                                <input type="number" min="1" class="form-control" id="amount" name="amount"></input>
                            </div>
                            <div class="mb-2">
                                <label for="weight" class="col-form-label">Weight:</label>
                                <input type="number" min="0.01" class="form-control" id="weight" name="weight"></input>
                            </div>
                            <div class="mb-2">
                                <label for="description" class="col-form-label">Description:</label>
                                <textarea class="form-control" id="description" name="description"></textarea>
                            </div>
                            <input type="hidden" class="form-control" id="containerID" name="containerID"></input>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" onclick="addItem()">Add Product</button>
                    </div>
                </div>
            </div>
        </div>
        ```
        + Buat fungsi initModal yang akan digunakan untuk set modal tersebut sesuai container yang ingin ditambahkan itemnya pada saat button diclick
        ```
        function initModal(containerName, containerID){
            document.getElementById("ModalTitle").textContent = `Add Item To ${containerName}`
            document.getElementById("containerID").value = containerID
        }
        ```
        + Buat button yang akan menampilkan modal tersebut
        ```
        // Didalam fungsi refreshTable
        <div class="text-center" style="margin-top: 20px;">
            <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#CreateItemModal" onclick="initModal('${container.name}', ${container.id})">Add Item</button>
        </div>
        ```
    - Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data
        + Pada views.py, tambahkan fungsi view berikut
        ```
        def create_item_ajax(request):
            if request.method == "POST":
                user = request.user
                name = request.POST.get('name')
                owner = request.POST.get('owner')
                type = request.POST.get('type')
                amount = request.POST.get('amount')
                weight = request.POST.get('weight')
                description = request.POST.get('description')
                containerID = request.POST.get('containerID')
                container = Container.objects.get(id=containerID)

                item = Item(user=user, name=name, owner=owner, type=type, amount=amount, weight=weight, description=description, container=container)
                item.save()

                return HttpResponse(b"CREATED", status=201)
            
            return HttpResponseNotFound()
        ```
    - Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat
        + Pada urls.py, import create_item_ajax dari views.py lalu tambahkan path berikut
        ```
        path('create-ajax', create_item_ajax, name='create_ajax')
        ```
    - Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/
        + Buat fungsi add item yang akan menyimpan dan mereset isi dari form modal tersebut
        ```
        async function addItem(){
            fetch("{% url 'main:create_ajax' %}", {
                method: "POST",
                headers: {
                    'X-CSRFToken': csrf,
                },
                body: new FormData(document.querySelector("#CreateItemForm"))
            }).then(refreshTable)

            document.getElementById("CreateItemForm").reset()
        }
        ```
    - Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan
        + Ketika menekan tombol search / add item / add / min / remove, maka tabel akan terupdate secara asinkronus tanpa harus reload halaman 