# rjplaton.com

Source for my personal homepage at [rjplaton.com](https://rjplaton.com).

Static one-page site, served directly by GitHub Pages from `/docs`.

## Editing

Edit `docs/index.html` (and `docs/style.css` if needed), commit, push. That's it — GitHub Pages picks it up within a minute or two.

```sh
git add docs/
git commit -m "your message"
git push
```

## Layout

```
docs/
  index.html    — the page
  style.css     — styles (system fonts, dark mode via prefers-color-scheme)
  404.html      — custom not-found
  portrait.jpg  — photo
  favicon.ico
  robots.txt
  sitemap.xml
  CNAME         — custom domain (rjplaton.com)
```

## Hosting & DNS

- **Host**: GitHub Pages, source = `master` branch / `/docs` folder
- **Registrar**: Porkbun
- **DNS**: Cloudflare (apex A → GitHub Pages IPs, www CNAME → rjplaton.github.io, AAAA, MX for Cloudflare Email Routing, DMARC, CAA)
- **Analytics**: Cloudflare Web Analytics (snippet in `index.html`, currently commented out — uncomment after pasting the token)
