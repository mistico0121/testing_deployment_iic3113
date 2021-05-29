# iic2173-e0-mistico0121

Está hecho en Django, Gunicorn, Postgres con motor web nginx como el proxy inverso

### Local

Usar `sudo docker-compose -f docker-compose-dev.yml up --build -d` para levantar la app en un daemon thread en local. Ejecutar `sudo docker-compose exec web python manage.py migrate --noinput` para migrar la base de datos.

Si ocurre un error, hacer `sudo docker-compose -f docker-compose-dev.yml down -v` para bajar la app y los volumenes, e intentar nuevamente

Luego metan todo lo que necesiten a los templates de la app. Esta ya está arriba y funcionando, solo debiera bastar hacer git pull y migrar cuando agreguen sus views


### Docker-compose

Pueden verse los detalles de los 3 requisitos en el archivo docker-compose. La aplicación se encuentra en un daemon thread y pueden bajarla del server, y luego volverla a subir con "sudo docker-compose up". Si quisieran bajar los volúmenes, para volver a subirlos se debe hacer `sudo docker-compose -d --build`, `sudo docker-compose exec web python manage.py migrate --noinput`, `sudo ./init-letsencrypt.sh` (script para obtener permisos SSL actualizados, si no se puede ejecutar se debe correr `chmod +x init-letsencrypt.sh`) y luego `screen` y adentro `sudo docker-compose up`. Así lo dejé corriendo en el servidor EC2. 

Los detalles del proxy inverso se pueden ver tanto en docker-compose.yml como en nginx/conf.d con sus puertos correspondientes.
