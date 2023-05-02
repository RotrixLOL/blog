---
title: "Subdomain Takeover: como un atacante puede tomar el control de tu sitio web"
date: 2023-05-01T13:46:15Z
description: "Toma medidas preventivas para proteger tu sitio web del subdomain takeover. Aprende cómo monitorear tus subdominios, configurar correctamente los registros DNS y utilizar herramientas de detección para evitar ataques malintencionados. Descubre cómo proteger tu sitio web contra el subdomain takeover en este artículo."
categories: ["Hacking"]
tags: ["Vuln"]
---


Los ataques informáticos son cada vez más sofisticados y, en muchos casos, pueden pasar desapercibidos durante mucho tiempo. Uno de estos tipos de ataques es el subdomain takeover, en el que un atacante puede tomar el control de un subdominio de un sitio web y utilizarlo para sus propios fines malintencionados. En este artículo, exploraremos qué es el subdomain takeover, cómo funciona y cómo puedes proteger tu sitio web contra él.

## ¿Qué es el subdomain takeover?

Los registros vulnerables son los **_CNAME_**, que son los que apuntan a otro dominio.

Pongamos un ejemplo. Imagina que estás alojando tu proyecto en Github Pages o en algún otro servicio similar. Decides que quieres un dominio personalizado, por ejemplo: `project.example.com` que apunta a `user.github.io/project`. Hasta ahí todo bien.

Pero un día decides borrar tu cuenta, y si alguien intenta acceder a tu proyecto, no podrá hacerlo. Ahora un atacante puede crearse una cuenta de Github con el nombre que tenías tú y usar tu subdominio personalizado para alojar su propio sitio web malicioso. Si un usuario intenta acceder a tu proyecto, será redirigido al sitio web del atacante sin siquiera darse cuenta. Esto podria llevar al phishing, si la pagina que estabas alojando era un login y el atacante clona esa pagina redireccionando las credenciales a su base de datos, por ejemplo.

## Cómo funciona el subdomain takeover

Este tipo de ataque se conoce como subdomain takeover y puede tener graves consecuencias para tu sitio web y tus usuarios. El atacante puede utilizar tu subdominio para alojar phishing, malware, o cualquier otro contenido malicioso, lo que puede dañar tu reputación y poner en riesgo la seguridad de tus usuarios.

Es importante tener en cuenta que el ejemplo que mencionamos es solo uno de los escenarios en los que se puede producir un subdomain takeover. Hay muchas otras formas en las que un atacante puede aprovecharse de un subdominio vulnerable, como cuando un servicio de terceros deja de estar disponible y el subdominio ya no está en uso.

Por lo tanto, es fundamental que los propietarios de sitios web tomen medidas para protegerse contra este tipo de ataque. A continuación hay algunas medidas preventivas que se pueden tomar para evitar un subdomain takeover:

## Cómo proteger tu sitio web contra el subdomain takeover

1. **Monitorear los subdominios**: Es importante tener una lista de todos los subdominios que se utilizan en el sitio web y monitorear regularmente su estado y actividad para detectar cualquier cambio sospechoso. También es recomendable realizar un seguimiento de los subdominios inactivos o que ya no se utilizan y desactivarlos o eliminarlos si es necesario.

2. **Configurar correctamente los registros DNS**: Los registros DNS son una parte fundamental de la configuración de un sitio web y deben configurarse correctamente para evitar posibles vulnerabilidades.

3. **Utilizar herramientas de detección**: Hay varias herramientas disponibles en línea que pueden ayudar a detectar posibles subdomain takeovers, como por ejemplo, [takeover](https://github.com/m4ll0k/takeover). Esta herramienta te puede escanear tu dominio para ver si hay subdominios libres.

## Conclusiones

En conclusión, el subdomain takeover es un riesgo real para cualquier sitio web, y los atacantes pueden aprovecharse de él de diversas maneras. Sin embargo, hay medidas que puedes tomar para detectar y prevenir este tipo de ataques. Es importante ser consciente de la amenaza y tomar medidas para proteger tu sitio web y a tus usuarios. Monitorear regularmente los subdominios, configurar correctamente los registros DNS y utilizar herramientas de detección son algunas de las mejores prácticas para proteger tu sitio web contra el subdomain takeover.

Gracias por tu lectura!
