# AGENTS.md

## Project overview

This repository contains the source for `belov.expert`, a bilingual personal landing page built with Hugo Extended. English is served at `/`; Russian is served at `/ru/`.

The site uses plain Hugo templates, CSS, and browser JavaScript. There is no frontend framework or application bundler. The `cyberguard` theme is committed directly under `themes/cyberguard/`; it is not an external dependency or submodule.

## Source map

- `hugo.yaml`: site configuration, languages, menus, contact details, social links, certifications, analytics, SEO flags, and output formats.
- `themes/cyberguard/layouts/_default/home.html`: homepage sections and the data-to-markup mapping.
- `themes/cyberguard/layouts/_default/baseof.html`: document shell, Hugo asset pipeline, language redirect, and analytics scripts.
- `themes/cyberguard/layouts/partials/`: shared header, footer, and additional `<head>` markup.
- `themes/cyberguard/assets/css/main.css`: all site styles, responsive rules, and light/dark theme variants.
- `themes/cyberguard/assets/js/main.js`: theme switching, mobile navigation, smooth scrolling, animations, publication expansion, language preference, and portfolio scrolling.
- `themes/cyberguard/i18n/{en,ru}.yaml`: translated interface strings used through Hugo's `i18n` function.
- `data/{en,ru}/portfolio.yaml`: localized portfolio cards.
- `data/{en,ru}/publications.yaml`: localized publication lists.
- `static/`: files copied to the site root unchanged. Reference `static/images/foo.webp` as `images/foo.webp`, never with a `static/` prefix.
- `layouts/_default/sitemap.xml`: project-level sitemap override. It takes precedence over `themes/cyberguard/layouts/_default/sitemap.xml` in Hugo's lookup order.
- `.github/workflows/hugo.yml`: production build and GitHub Pages deployment. CI currently pins Hugo Extended `0.165.0`.

Generated directories such as `public/` and `resources/`, plus `node_modules/`, are not source files and must not be edited or committed.

## Working principles

- Make the smallest change that fully solves the requested task.
- Assume maintainers are HTML, CSS, and JavaScript experts. Do not add comments that explain obvious code.
- Prefer self-explanatory names; short names are appropriate when their meaning is clear from the local context.
- Preserve existing comments, empty lines, indentation, and formatting unless the requested change requires touching them.
- Do not reformat whole files or run broad automatic fixes for a localized change.
- Match the style of the surrounding file rather than introducing a new abstraction or convention.
- Do not fix unrelated defects, deprecations, content, or formatting while completing another task. Report relevant findings instead.
- Inspect the current working tree before editing and preserve changes that are not yours.
- Do not commit, push, deploy, or modify GitHub settings unless explicitly asked.

## Hugo and template conventions

- Edit source templates and assets in `themes/cyberguard/`; do not patch generated HTML in `public/`.
- Root `layouts/` files override same-path theme templates. Check both locations before changing or adding a layout.
- Keep asset-managed CSS and JS under `themes/cyberguard/assets/`. `baseof.html` loads them with `resources.Get`, minification, and fingerprinting.
- Keep directly served files under `static/`. Use `relURL` for static asset paths in templates unless an absolute URL is specifically required.
- Use language-aware Hugo URLs such as `.Site.Home.RelPermalink`, `relLangURL`, and translated page permalinks. Do not hard-code `/ru/` routing in markup.
- Keep menu identifiers in `hugo.yaml`, section IDs in `home.html`, and matching i18n keys aligned.
- Preserve the early inline theme initialization in `<head>`; moving it can cause a light/dark flash before paint.
- When adding an external resource, update the Content Security Policy in `partials/head-custom.html` for the exact required origin and directive. Do not broaden the policy unnecessarily.
- External links opened with `target="_blank"` must include at least `rel="noopener"`; use `noreferrer` as well where the surrounding code does.

## Localization and structured data

- User-facing template text belongs in both `themes/cyberguard/i18n/en.yaml` and `themes/cyberguard/i18n/ru.yaml`, with identical key sets, unless the task explicitly targets one locale.
- Portfolio entries use `title`, `logo`, `url`, and `description`.
- Publication entries use `title`, `media_name`, `media_logo`, `url`, and optional `date`.
- Keep localized portfolio and publication files structurally aligned when content exists in both languages.
- Publications are displayed in file order. Keep them newest first and preserve the existing `MM-DD-YYYY` date representation.
- Quote YAML values when punctuation, colons, leading symbols, or implicit YAML types could change parsing.
- A new image referenced by YAML or configuration belongs under `static/images/`; verify that its case-sensitive path exists.
- A new certification needs its configuration in `hugo.yaml`, its badge asset, and its `titleKey` translation in both locale files.

## Frontend conventions

- Keep JavaScript dependency-free and compatible with the browser APIs already used in `main.js`.
- Reuse existing CSS custom properties, components, breakpoints, and state classes before adding new ones.
- Any visible UI change must work in light and dark themes and at the existing responsive breakpoints: 1200px, 992px, 768px, and 576px.
- Preserve semantic HTML, keyboard access, visible focus behavior, useful alternative text, and explicit image dimensions when known.
- Keep Hugo-provided translated text in template attributes when JavaScript needs it; do not duplicate localized strings in JavaScript.
- Treat analytics IDs, contact details, profile links, and publication URLs as content. Do not alter or fabricate them without an explicit request.

## Commands

Requirements:

- Hugo Extended. Match CI's pinned version when compatibility matters.
- Node.js and npm only for the optional formatting, linting, and image tooling declared in `package.json`.

Install optional Node dependencies:

```bash
npm install
```

Run the local server:

```bash
npm run dev
```

Build the production site:

```bash
npm run build
```

The repository has no automated test suite. The production Hugo build is the minimum required validation for every source change.

Do not use `npm run format` for a focused task because it rewrites many file types. `npm run lint` also runs Stylelint with `--fix`; inspect its effects before using it and never include unrelated rewrites. Do not run `npm run deploy`: it contains a placeholder destination and destructive `rsync --delete` behavior.

## Validation checklist

1. Run `npm run build` and distinguish new errors from the known baseline deprecation warnings for `languageCode`, `languageName`, and `.Site.Data` on Hugo 0.165.0.
2. For template, content, or localization changes, inspect both the English `/` output and Russian `/ru/` output.
3. For UI changes, check desktop and mobile layouts, light and dark themes, keyboard interaction, and the browser console.
4. For data or asset changes, verify referenced files and links and confirm ordering in the rendered section.
5. Review the final diff and confirm that only files required by the task changed; never include generated `public/` or `resources/` output.
