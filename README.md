# blog

Cibersecurity and software development Open Source blog -> [blog.rotrixx.eu](https://blog.rotrixx.eu)

## :books: Tech Stack

- SSG: [Hugo](https://gohugo.io) + [Blowfish theme](https://blowfish.page)
- Hosting: [Vercel](https://vercel.com)

## Translation tool

I created a [tool](/translate_tool/translate.py) in python to translate posts to english. To setup the tool:

1. `python3 install -r requirements.txt`

2. `python3 translate_tool/translate.py`

This tool will iterate over `content/posts` directory and search for `index.es.md` files. Next, will obtain the post body, translate and formate it. Finally it will create `index.en.md` with the same front matter as the original and the body translated and formatted.

## :handshake: Contributions

You are free to contribute content and change the site if you think that your contribution is valuable!

<p>Thank you!</p>
