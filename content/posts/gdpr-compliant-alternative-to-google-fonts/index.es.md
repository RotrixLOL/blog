---
title: "Alternativa a Google Fonts que cumple la GDPR"
date: 2023-07-22T11:08:23+02:00
description: "Como ya sabes, google fonts ha dejado de ser legal por el GDPR. Usa Bunny Fonts si no quieres tener una multa de hasta 1 millon de euros (en Europa)."
categories: ["web", "frontend", "services"]
tags: ["alternative"]
---

Como probablemente ya sepas, o en caso de que no, google fonts ya no es legal en Europa.
Esto se debe al GDPR, que es una regulación para las aplicaciones que sirven a Europa, para que las plataformas no recopilen información de los usuarios sin dejarlo claro.
Las multas pueden ser de hasta 1 millón de euros, así que es mejor pensar en alternativas.

He estado investigando y una alternativa muy buena es [**Bunny Fonts**](https://fonts.bunny.net).
La interfaz es muy similar a Google Fonts y también lo es la importación de fuentes.
Parece un clon de Google Fonts pero cumple con la GDPR.

## ¿Cómo importo una fuente desde bunny fonts?

Muy sencillo. Aquí hay una captura de pantalla de la página principal de Bunny Fonts:
página de inicio de bunny fonts (bunnyfonts.png)

Elija la fuente deseada. Haga clic en el botón _añadir variante_ para cada variante que desee importar.
![bunny fonts fuente elegida](fontpreview.png)

Esta ventana se abrirá, si no, haga clic en _Fonts +_.
![Importar fuente](importfont.png)

Y ahora sólo tienes que copiar y pegar esos estilos en tu archivo css, así:
```css
@import url(https://fonts.bunny.net/css?family=abeezee:400,400i);

body {
  font-family: 'ABeeZee', sans-serif;
}
```

## Outro

Ya has visto lo parecido que es bunny fonts a google fonts.
Así que recuerda usar esta página en lugar de google fonts, ¡a menos que quieras recibir una gran multa!

¡Gracias por leer este artículo!
