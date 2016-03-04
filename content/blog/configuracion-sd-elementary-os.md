Title: Configuración de la tarjeta wifi y el lector de tarjetas SD en Elementary OS (Ubuntu) Linux (Intel Wireless N7260, chipset RTL 5287)
Slug: configuracion-lector-sd-linux-n7260
Date: 2016-02-23 16:28
Tags: wifi, drivers, sd, ubuntu, linux, elementaryos, mountain

<!-- PELICAN_BEGIN_SUMMARY -->
Hace algún tiempo, en Mayo del 2014, compré un portatil a la empresa [Mountain](ihttp://www.mountain.es/), en concreto el **Mountain Nickel 10**, un portátil de 14" con procesador Core i5 4310M Mobile a 2.7 GHz, equipo del que estoy muy contento. Mountain es una empresa española conocida por montar sus equipos en España y por fabricar productos de gran calidad.

![Imagen de un portátil Mountain]({filename}/images/portatil_mountain.jpg){.right}

Tengo instalado un sistema operativo **Linux**, en concreto una [Elementary OS](https://elementary.io/es/), distribución basada en [Ubuntu](http://www.ubuntu.com/) y me encontré con que parte del hardware es demasiado *moderno* para la versión del kernel incluída por defecto.

No me funcionan los siguientes dispositivos:

- La tarjeta de red Wifi, una *Intel Wireless N7260*
- El lector de tarjetas SD, con chipset *Realtek 5287*
<!-- PELICAN_END_SUMMARY -->

Los pasos para solucionarlo han sido:

1. Actualizar el *kernel de Linux* desde este [PPA de Ubuntu](http://kernel.ubuntu.com/~kernel-ppa/)
2. Actualizar el *firmware* utilizado por los drivers de la tarjeta wifi

## Actualización al kernel a la versión 3.19.8

Para actualizarlo cogí la **última version disponible de la serie 3 del kernel, la *3.19.8*, descargando los tres paquetes .deb, dos para las cabeceras y uno para el kernel, directamente desde [la web del PPA del kernel de Ubuntu](http://kernel.ubuntu.com/~kernel-ppa/mainline/v3.19.8-vivid/)** e instalándolos manualmente con *dpkg*

    dpkg -i linux-headers-3.19.8-031908_3.19.8-031908.201505110938_all.deb
    dpkg -i linux-headers-3.19.8-031908-generic_3.19.8-031908.2015s5110938_amd64.deb
    dpkg -i linux-image-3.19.8-031908-lowlatency_3.19.8-031908.201505110938_amd64.deb

## Actualización del firmware para los drivers de la tarjeta WiFi

Una vez actualizado el kernel a esta versión el lector de tarjetas SD funciona correctamente. El problema es que ¡no tenemos red!

Al arrancar podemos ver el siguiente mensaje de error en el log del sistema */var/log/syslog*

    iwlwifi 0000:02:00.0: Direct firmware load for iwlwifi-7260-12.ucode failed with error -2

Lo que está pasando es que los ficheros de firmware instalados (paquete *linux-firmware*) son antiguos, ya que nos está pidiendo el archivo *iwlwifi-7260-12.ucode* *(versión 12)* y el que tenemos en el sistema instalado en */lib/firmware* es una versión anterior.

Una rápida búsqueda nos lleva a que se encuentra en [este repositorio de actualizaciones de seguridad de Ubuntu](http://packages.ubuntu.com/en/vivid/linux-firmware).  Siguiendo la recomendación de su web, he **añadido el repositorio de actualizaciones de seguridad** a la lista de fuentes del sistema creando un archivo debajo de */etc/apt/sources.list.d* con el siguiente contenido:

    deb http://security.ubuntu.com/ubuntu vivid-security main

Para posteriormente instalarlo de la manera habitual:

    apt-get update
    apt-get install linux-firmware

Resuelto :-)

> Be Free! Be Wild! Be Linux!
