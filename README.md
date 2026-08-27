# belov.expert

Bilingual personal landing page built with Hugo. English is served at `/`, Russian at `/ru/`.

## Local run

Requirements:
- Hugo Extended
- Node.js (only for lint/format/asset tooling)

Install dependencies:
```bash
npm install
```

Run dev server:
```bash
npm run dev
```

or:
```bash
hugo server -D
```

Open `http://localhost:1313`.

## Build

```bash
npm run build
```

or:
```bash
hugo --minify
```

## What to edit

- `hugo.yaml`: site config, links, contact, analytics, menu, identity used in structured data.
- `data/en/publications.yaml`, `data/ru/publications.yaml`: publications list.
- `data/en/portfolio.yaml`, `data/ru/portfolio.yaml`: portfolio cards.
- `content/media.md`, `content/media.ru.md`: the `/media/` page (front matter only; the list is rendered from the publications data).
- `themes/cyberguard/i18n/en.yaml`, `themes/cyberguard/i18n/ru.yaml`: UI text.
- `themes/cyberguard/layouts/` and `themes/cyberguard/assets/`: templates, CSS, JS.
- `static/images/`: images and logos.

## Structure

```text
.
├── .github/workflows/hugo.yml
├── content/
├── data/
├── layouts/
├── static/
├── themes/cyberguard/
├── hugo.yaml
└── package.json
```

## Deploy

Deployment is via GitHub Actions (`.github/workflows/hugo.yml`) on push to `main`.
