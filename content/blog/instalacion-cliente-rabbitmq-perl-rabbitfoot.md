Title:  Instalación del cliente RabbitFoot de Perl en un servidor Linux
Slug: instalacion-cliente-rabbitmq-perl-rabbitfoot
Date: 2016-04-07 11:30
Tags: perl, rabbitmq, linux, rabbitfoot

<!-- PELICAN_BEGIN_SUMMARY -->
En este artículo explicaré cómo he instalado el cliente de RabbitMQ para Perl [Net::RabbitFoot](http://search.cpan.org/~ikuta/Net-RabbitFoot-1.03/lib/Net/RabbitFoot.pm).

![Logotipo de RabbitMQ]({filename}/images/rabbitmq_logo_strap.png){.right}

[RabbitMQ](http://www.rabbitmq.com/) es un servidor con licencia Open Source que permite la comunicación entre diferentes aplicaciones o servicios de forma distribuída mediante mensajes. La idea general de los servicios de mensajería es gestionar una o varias colas a las que van llegando las distintas "órdenes" o mensajes. Hay aplicaciones que se encargan de enviar mensajes, entendidos como conjuntos de datos al servicio, y otras aplicaciones (o procesos) van recibiendo los mensajes y actuando en consecuencia. [Aquí](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html) hay una excelente explicación de cómo funcionan este tipo de sistemas.

Un ejemplo típico podría ser un grupo de chat. Una aplicación (web o un cliente móvil en el caso de WhatsApp, por ejemplo) envía los mensajes del usuario y el resto de usuarios del grupo con sus respectivos dispositivos permanecen "escuchando" para procesar los mensajes que vayan llegando. Cada grupo sería una cola distinta.
<!-- PELICAN_END_SUMMARY -->

Usaremos [CPAN](http://www.cpan.org/) para instalar Net::RabbitFoot con todas sus dependencias de forma automática con los siguientes requisitos:
- Las librerías serán instaladas en un directorio personalizado, para no tocar el Perl del sistema
- En mi caso particular la instalación se ha hecho sobre un sistema SUSE Linux Enterprise 11

## Instalación de las librerías de desarrollo

Si no tenemos instalado el compilador gcc y los útiles de compilación deberemos hacerlo. En SuSE Linux con el comando _**zypper**_ lo podemos hacer indicando que queremos instalar todos los paquetes del "patrón" _"Basis-Devel"_:

    $ zypper install --type pattern Basis-Devel

## Configuración de CPAN para la instalación de módulos en nuetra carpeta de usuario

Para poder descargar de forma automatizada paquetes de Perl usaré ***cpanminus***, una herramienta superior a *cpan*, la incluída por defecto con Perl.

Para poder usar **un proxy HTTP con autentificación** estableceremos variables de entorno de la shell *http_proxy*, *ftp_proxy* y *https_proxy*

```bash
$ export http_proxy="http://miusuario:miclave@direcciondemiproxyhttp:puertodelproxyhttp"
$ export ftp_proxy="$http_proxy"
$ export https_proxy="$http_proxy"
```

Configuramos [CPAN](http://www.cpan.org/), en mi caso para utilizar **un proxy HTTP con autentificación** con el comando `perl -MCPAN -e shell`:

    $ perl -MCPAN -e shell
    Would you like to configure as much as possible automatically? [yes] no
    Do you want to halt on failure (yes/no)? [no] yes
    Your terminal expects ISO-8859-1 (yes/no)? [yes] no
    Would you like me to automatically choose some CPAN mirror sites for you? (This means connecting to the Internet) [yes] no

Este comando lo que hace es una serie de preguntas. Indico únicamente aquellas cuya respuesta es distinta a la ofrecida por defecto y que no son evidentes.

Hubo que indicarle que no intente obtener la lista de servidores de forma automática de Internet debido a que con la versión 5.16.3 de perl se producía el error ["Can't call method "http" on unblessed reference at ... FirstTime.pm"](http://stackoverflow.com/questions/9614347/error-running-cpan-the-first-time).

## Configuración del entorno de la shell

Una vez terminada la ronda de preguntas el script de configuración descargará algunos módulos de Internet y **añadirá automáticamente las siguientes varias variables de entorno a la configuración de la shell**, en el fichero _.bashrc_

```bash
PATH="$HOME/perl5/bin${PATH+:}${PATH}"; export PATH;
PERL5LIB="$HOME/perl5/lib/perl5${PERL5LIB+:}${PERL5LIB}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="$HOME/perl5${PERL_LOCAL_LIB_ROOT+:}${PERL_LOCAL_LIB_ROOT}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"$HOME/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=$HOME/perl5"; export PERL_MM_OPT;
```

Cerramos la sesión, volvemos a hacer login en el servidor y tendremos todo listo para instalar nuevos módulos debajo de la carpeta *"perl5"* en nuestra carpeta de usuario.

## Instalación de RabbitFoot

Una vez CPAN correctamente configurado instalamos cpanminus y luego usamos esta herramienta para instalar el módulo y sus dependencias

    $ cpan App::cpanminus
    $ cpanm Net::RabbitFoot

Durante la instalación dió un error a la hora de instalar *MooseX::App::Cmd* con lo que volvimos a reinstalar esta dependencia y solicitar de nuevo las instalación de *RabbitFoot*, esta vez con éxito.

    $ cpanm MooseX::App::Cmd
    $ cpanm Net::RabbitFoot

La documentación incluída en el módulo es casi inexistente, pero **hay unos bonitos tutoriales en el propio producto RabbitMQ que podemos consultar [aquí](https://github.com/rabbitmq/rabbitmq-tutorials/tree/master/perl)**.

## Envío de nuestro primer mensaje "¡Hola Mundo!"

Para poder enviar un mensaje al servidor RabbitMQ tendremos que conocer los siguientes datos:

- Dirección y puerto (5672 por defecto) del servidor RabbitMQ
- Host virtual en el que está configurada la cola
- Usuario y clave para poder enviar mensajes al servidor
- Nombre del _"exchange"_, el canal de entrada definido en RabbitMQ

¡Y allá vamos!

```Perl
#!/usr/bin/perl

use strict;
use warnings;

$|++;
use Net::RabbitFoot;

my $conn = Net::RabbitFoot->new()->load_xml_spec()->connect(
    host => 'elservidordondestainstaladorabbitmq.com',
    port => 5672,
    user => 'usuarioderabbitmq',
    pass => 'clavederabbitmq',
    vhost => 'reflex',
);


my $chan = $conn->open_channel();

$chan->publish(
    exchange => 'nombreexchange',
    routing_key => '',
    body => '¡Hola mundo!',
);

print " [x] Mensaje '¡Hola mundo!' enviado\n";

$conn->close();
```



