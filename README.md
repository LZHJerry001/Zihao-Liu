# Zihao Liu · Academic Website

This repository contains Zihao Liu's academic website, a responsive static site inspired by the visual style of Hugoplate. The site uses a small Python generator; it does not require Hugo, Node, or additional Python packages.

## Edit the website

- Update papers, talks, conferences, courses, and photo captions in `content.py`.
- Replace or add photographs in `assets/`.
- The page layouts are in `build.py`; colors and layout are in `style.css`.
- Run `python3 build.py` to regenerate the `dist/` directory.

## Publish with GitHub Pages

1. Upload the repository contents, including the `.github` folder, to the default `main` branch of a GitHub repository.
2. In the repository, open **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**.
3. In **Actions**, run the **Deploy website to GitHub Pages** workflow if it has not already deployed. Future pushes to `main` deploy automatically.
4. The website address is shown under **Settings → Pages** and in the completed workflow.

The generated links support both a personal site at `USERNAME.github.io` and a project site at `USERNAME.github.io/REPOSITORY/`. A GitHub Pages website is public. GitHub Free requires a public repository for Pages.

The `dist/` folder also contains a ready-to-serve copy for other static hosting providers.
