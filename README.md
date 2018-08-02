## Boilerplate Bottle Python

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

Instalación de dependencias:

    $ pip install -r requirements.txt

Migraciones con DBMATE:

    $ dbmate -d "db/migrations" -e "DATABASE_URL" new <<nombre_de_migracion>>
    $ dbmate -d "db/migrations" up

### Archivos a cambiar para el pase a producción

+ app.py
+ config/constants.py

### Fuentes:

+ https://bottlepy.org/docs/dev/
+ https://buxty.com/b/2013/12/jinja2-templates-and-bottle/
+ https://bottlepy.org/docs/dev/recipes.html
+ https://stackoverflow.com/questions/29450018/bottle-w-beaker-middleware

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
