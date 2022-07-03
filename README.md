# MusicPro
Super admin users:
=
- Username: MusicPro
Pass:MusicPro

- Username: admin
Pass:1234

URLS: 
=
- Api:'api/'
- Index:' '
- contacto:'contactanos'
- Blog:'blog'
- Productos:'productos'
- About:'sobrenuestrosproductos'

LOGINS:
=
- cliente: cliente@gmail.com pass: Pelicanoprueba1 (hasta el momento no se si esta agregado el gmail)
- Administrador:  admin@gmail.com pass: 123 
- Contador: contador@gmail.com pass: Pelicanoprueba1
- Bodeguero:bodeguero@gmail.com pass: Pelicanoprueba1
- Vendedor: vendedor@gmail.com pass: Pelicanoprueba1
- Falta crearlos y limpiar la base de datos de usuarios prueba 

POSIBLES PROBLEMAS:
=
- en caso de problemas con la base de datos ejecutar: python manage.py migrate --run-syncdb

CAMBIOS:
=
- Ahora la api recibe el gmail como credencial al igual que el inicio de sesion ahora solicita el email