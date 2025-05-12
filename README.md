# Sergey Belov - Cybersecurity Expert Website

A professional static website for Sergey Belov, a cybersecurity expert providing services for enterprise companies.

This website is built with [Hugo](https://gohugo.io/), a fast static site generator, and is designed to be highly optimized for performance, SEO, and accessibility.

## Features

- 🌐 Multilingual support (English, Russian, Chinese)
- 🎯 High conversion focused design
- 📱 Fully responsive (mobile, tablet, desktop)
- 🚀 Optimized for Google PageSpeed (Performance, SEO, Accessibility, Best Practices)
- 🔒 Security best practices implemented
- 🔍 SEO-optimized with metadata, structured data, and sitemap
- 📄 Dynamic publication management via data files

## Getting Started

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.100.0 or newer)
- Node.js for development tools (optional)

### Installation

1. Clone the repository
```
git clone https://github.com/sergeypbelov/website.git
cd website
```

2. Run Hugo's development server
```
hugo server -D
```

3. Open your browser and visit http://localhost:1313

## Project Structure

```
├── archetypes/         # Content templates
├── assets/             # Theme assets (CSS, JS)
├── content/            # Site content in Markdown
│   ├── en/             # English content
│   ├── ru/             # Russian content
│   └── cn/             # Chinese content
├── data/               # Data files for publications
│   ├── en/
│   ├── ru/
│   └── cn/
├── i18n/               # Translation files
├── layouts/            # HTML templates
├── static/             # Static files
│   ├── images/         # Images
│   └── fonts/          # Fonts
└── hugo.yaml           # Hugo configuration
```

## Customization

### Publications

Publications are managed through YAML data files in the `data/[language]/publications.yaml` directory. Each publication has the following structure:

```yaml
- title: "Article Title"
  media: "Media Source"
  logo: "logo-file.webp"  # Path relative to static/images/media-logos/
  url: "https://example.com/article"
  date: "2023-05-18"
  featured: true  # Set to true to display in the featured section
```

### Adding Images

Place all images in the `static/images/` directory. For media logos, use the `static/images/media-logos/` directory.

### Modifying Content

Edit the Markdown files in the `content/` directory to change the site content. The site uses front matter for page metadata.

## Deployment

The site is configured for deployment to Cloudflare Pages with automatic build and deploy.

### Manual Deployment

1. Build the site
```
hugo --minify
```

2. The `public` directory contains the built site, ready for deployment

## Performance Optimization

The site is optimized for maximum performance with:

- Minified CSS and JS
- WebP images with proper sizing and optimization
- Critical CSS for fast rendering
- Proper use of async and defer for scripts
- Font preloading and optimization
- HTTP/2 support

## SEO Features

- Structured data with Schema.org
- Optimized meta tags and Open Graph
- XML sitemap with hreflang
- Canonical URLs
- Proper heading structure

## Browser Support

The site is designed to support all modern browsers including:

- Chrome, Firefox, Safari, Edge (latest versions)
- IE11 with fallbacks

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Hugo](https://gohugo.io/)
- Icons from [Heroicons](https://heroicons.com/)
- Font by [Inter](https://rsms.me/inter/) 