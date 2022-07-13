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
- cliente: cliente@gmail.com pass: pelicanoprueba (hasta el momento no se si esta agregado el gmail)
- Administrador:  admin@gmail.com pass: 123 
- Contador: contador@gmail.com pass: pelicanoprueba
- Bodeguero:bodeguero@gmail.com pass: pelicanoprueba --CREADO
- Vendedor: vendedor@gmail.com pass: pelicanoprueba
- Falta crearlos y limpiar la base de datos de usuarios prueba 

Paypal:
=
- Ingresar a www.sandbox.paypal.com
- correo: ClienteJhonDoe@personal.example.com
- contraseña: pelicanoprueba123

POSIBLES PROBLEMAS:
=
- en caso de problemas con la base de datos ejecutar: python manage.py migrate --run-syncdb

CAMBIOS:
=
- Ahora la api recibe el gmail como credencial al igual que el inicio de sesion ahora solicita el email
- Ahora no se puede acceder a las urls desde cualquier vista

INSTRUCCIONES PARA EL TESTING (Python):
=
- Entrar a la carpeta Test desde el CMD
- Ejecutar comando: pip install selenium
- Ejecutar comando: pip install pytest
- Tener el archivo chromedriver.exe (verifique que la versión que ya está en la carpeta es la que corresponde a su navegador. La que está es la versión Chrome 103.0.5060.66 )
- Ejecutar comando: pytest

INSTRUCCIONES PARA EL TESTING (Selenium IDE):
=
- Descargar Selenium IDE para su navegador
- Abrir Selenium IDE desde su navegador
- Abrir proyecto "Test_MusicPro" que está en la carpeta Test
- Levantar servidor desde CMD
- Ejecutar las pruebas