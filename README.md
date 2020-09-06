# iic2173-e0-mistico0121

Me dijieron que hiciera un 4chan, así que hice un sitio parecido a propósito. Está hecho en Django, Gunicorn, Postgres con motor web nginx como el proxy inverso

La app se encuentra containerizada. Se encuentra en el sitio testimageboard.tk, el cual está asegurado con ssl.

Cada "thread" corresponde a la funcionalidad de una sala de chat. Acá quedan guardados todos los mensajes que postean los usuarios, los cuales son anónimos a menos que ellos introduzcan un nombre en el form. También dejé implementada una funcionalidad para subir imágenes a la db de la app(/testupload), pero no la alcancé a unir a la funcionalidad de imageboard de la página, por ende, por ahora solo se parece a un viejo sitio BBS, queda como tarea personal a futuro con motivos educativos. 

No implementé los comandos de chat, solo los puntos 1 y 2 opcionales.
El frontend está hecho con templates de Django, boostrap, y copié parte del CSS de 4chan para darle un toque.

### Requerimientos obligatorios

#### RF1

Otros usuarios logran ver los mensajes cuando recargan la página, mientras que se recarga automáticamente para el usuario que hace post. Si se sale de la página y se vuelve a entrar se puede ver todo.

#### RF2

En la página de inicio, cualquier usuario puede crear un thread, el cual sería el equivalente de la sala de chat en esta app.

#### RF3

Cada usuario puede ingresar su username al momento de hacer un post o thread.

#### RNF1

La configuración del proxy inverso la pueden ver con los archivos docker-compose.yml y nginx/conf.d

#### RNF2

testimageboard.tk

#### RNF3

En el formulario canvas mandé el .pem con las credenciales y esta info.


#### RNF4

La configuración de la base de datos depende de un container de postgres. Pueden ver la configuración en docker-compose.yml.

#### RNF5

Dentro de la maquina EC2, se encuentra corriendo un screen en el cual hice sudo docker-compose up luego de haber hecho build y migrate con los contenedores.  


### Docker-compose

Pueden verse los detalles de los 3 requisitos en el archivo docker-compose. La aplicación se encuentra en un screen y pueden bajarla del server, y luego volverla a subir con "sudo docker-compose up". Si quisieran bajar los volúmenes, para volver a subirlos se debe hacer `sudo docker-compose -d --build`, `sudo docker-compose exec web python manage.py migrate --noinput`, `sudo ./init-letsencrypt.sh` (script para obtener permisos SSL actualizados, si no se puede ejecutar se debe correr `chmod +x init-letsencrypt.sh`) y luego `screen` y adentro `sudo docker-compose up`. Así lo dejé corriendo en el servidor EC2. 

Los detalles del proxy inverso se pueden ver tanto en docker-compose.yml como en nginx/conf.d con sus puertos correspondientes.

### SSL

#### RNF1

El servidor se encuentra asegurado con SSL. En nginx/conf.d se puede observar como está hecha la redirección de http(puerto 80) a https(puerto 443). 

#### RNF2

La base de datos se puede observar en docker-compose.yml. Cuando no se especifica una network, docker-compose hace una network automáticamente con todos los contenedores, y no requería mas que eso en esta entrega. Gracias a la db que se encuentra en el contenedor `db` es que se pueden almacenar y mostrar los posts.

#### RNF3
En el archivo docker-compose.yml pueden ver que nginx revisa por nuevos permisos SSL cada 6 horas, mientras que certbot obtiene un permiso nuevo cada 12 horas.

 
