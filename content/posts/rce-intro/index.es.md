---
title: "Introducción a los RCEs: Que son y como prevenirlos"
date: 2023-05-02T21:28:09Z
description: "Un RCE (Remote Code Execution) permite al atacante ejecutar codigo malicioso en un servidor remoto si por ejemplo tienes un sitio web con un parametro vulnerable en la url. Descubre más de RCEs y como prevenirlos en este artículo!"
summary: "Un RCE (Remote Code Execution) permite al atacante ejecutar codigo malicioso en un servidor remoto si por ejemplo tienes un sitio web con un parametro vulnerable en la url. Descubre más de RCEs y como prevenirlos en este artículo!"
categories: ["Hacking"]
tags: ["RCE"]
---

Los RCE (Remote Code Execution) son muy fáciles de escribir como desarrollador, y comúnmente fáciles de explotar como atacante. ¡Si quieres entender que son, como funcionan y como los podemos prevenir como desarrolladores, sigue leyendo este artículo, que seguro que aprendes!

## ¿Qué es un RCE?

Un RCE es una vulnerabilidad que permite a un atacante ejecutar código malicioso en un sistema remoto, normalmente en una web.

Esto significa que si tienes alojada una aplicación web en tu propio servidor, un atacante podría aprovecharse de algún parámetro en la URL para inyectar código. Esto le permite al atacante conseguir un posible acceso al servidor.

## ¿Cómo funciona un RCE?

Imagínate que estás alojando una tienda online PHP en tu servidor y tienes un parámetro para la funcionalidad de la paginación. Pues un atacante podría intentar una variedad de combinaciones para conseguir inyectar comandos.

Este tipo de vulnerabilidad está presente en muchas máquinas de [HTB](https://hackthebox.com) por lo que deberías dominarlo. ¿La mejor manera? La practica, cuanto más explotes esta vulnerabilidad, más fácil te será luego.

`http://www.example.com/index.php?page=;whoami`

En este caso, el atacante está utilizando la técnica de **command injection** para ejecutar el comando _whoami_ para ver con qué usuario se está ejecutando la app.

## ¿Cómo prevenir un RCE?

Para prevenir un RCE, es esencial seguir buenas prácticas. Aquí hay algunas medidas que se pueden tomar para prevenir el RCE:

### Actualizar el software

Mantener el software actualizado en todo momento es crucial para garantizar que se corrijan las vulnerabilidades conocidas. Esto incluye el sistema operativo, las aplicaciones web y cualquier servicio que se ejecute en el sistema.

### Validar y sanitizar la entrada

Es importante validar toda la entrada de usuario que se recibe a través de la aplicación web para garantizar que no se introduzcan datos maliciosos. Esto puede incluir la validación de la longitud de la entrada, la eliminación de caracteres especiales y la validación de los tipos de datos. Además, la sanitización de entrada se refiere a la eliminación de caracteres maliciosos o peligrosos de la entrada de usuario. Esto puede incluir la eliminación de caracteres especiales y la codificación de la entrada para evitar la inyección de código.

### Configurar el servidor de manera segura

Configurar el servidor de manera segura es esencial para evitar la RCE. Esto incluye la desactivación de servicios innecesarios, el uso de contraseñas seguras y la implementación de firewall y otros mecanismos de seguridad.

Y aunque se pueda conseguir una reverse shell, también es importante complicar la escalada de privilegios como medida de seguridad, para que si el atacante consigue acceso, que no pueda hacer mucha cosa.

### Realizar pruebas de seguridad

Realizar pruebas de seguridad regulares en la aplicación web y en el servidor es importante para detectar cualquier vulnerabilidad de seguridad. Esto puede incluir pruebas de penetración y análisis de vulnerabilidades, aunque como desarrollador también puedes intentar probar a inyectar código.

## Conclusión

El RCE es una amenaza grave para la seguridad que puede permitir a un atacante tomar el control completo de un sistema remoto. Para prevenirla, es esencial mantener el software actualizado, validar y sanitizar la entrada de usuario, configurar el servidor de manera segura y realizar pruebas de seguridad regulares. Al seguir estas mejores prácticas de seguridad, podemos reducir significativamente el riesgo de RCE y proteger nuestros sistemas y datos contra los ataques maliciosos.

¡Gracias por la lectura!

{{< alert >}}
Pronto escribiré writeups de HTB y artículos de desarrollo web!
{{< /alert >}}
