# Ensuro Website

This repository contains the source for the [Ensuro website](https://ensuro.co), deployed using **GitHub Pages** and built with **Pelican** and **Jinja2**.

---

## 📌 How it works

- **Content source:**
  - The input parameters for the Jinja2 templates are defined in the file [`content/data/input.yaml`](content/data/input.yaml).
  - Static assets (images, CSS, JS) live in [`content/`](content/).

- **Templates:**
  - Jinja2 templates are stored in the [`templates/`](templates/) folder as HTML file to ensure Pelican works correctly.
  - A custom script inside `pelicanconf.py` renders these templates to static HTML files before Pelican builds the final site.

- **Build output:**
  - The generated HTML files are placed in a temporary [`content/rendered/`](content/rendered/) folder (not committed).
  - Pelican copies these rendered pages and all static assets into [`output/`](output/).
  - The `output/` folder is **not versioned**; it is created on each build.

---

## 🚀 How to build locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```
### 2️⃣ Build the site
```bash
make html
```
### 3️⃣ Serve locally
```bash
make serve
```

This will start a local web server at http://localhost:8000 to preview the site.

## 🔄 How to deploy
### Deployement automatic on push & merge PR
- GitHub Actions build the site (make publish) and upload the contents of output/ to the gh-pages branch.
- GitHub Pages serves the latest version from gh-pages.

## ✏️ Formatting Team Images with ImageMagick

### Optional: Install ImageMagick

```bash
sudo apt-get install imagemagick
```

### To format team member images using ImageMagick, follow these steps:

1️⃣ **Resize the image to 200x200 pixels and convert it to grayscale:**

```bash
convert /route/to/image.png -resize 200x200^ -gravity center -extent 200x200 -colorspace Gray resized_grayscale_image.png
```
2️⃣ **Create a mask with rounded corners:**

```bash
convert -size 200x200 xc:none -draw "roundrectangle 0,0 199,199 50,50" mask.png
```
3️⃣ **Apply the mask to the resized grayscale image:**

```bash
convert resized_grayscale_image.png mask.png -alpha set -compose DstIn -composite team_member.png
```

### To format partners & investors images from jpg/jpeg to png using ImageMagick, follow these steps:

```bash
convert /route/to/image.jpg -fuzz 20% -transparent white output.png
```

### To format partner images using ImageMagick, follow these steps:

1️⃣ **Resize the image to 90x90 pixels and rounded borders:**

```bash
convert /route/to/image.png -resize 90x90^ -gravity center -extent 90x90 resized_image.png
```
2️⃣ **Create a mask with rounded corners:**

```bash
convert -size 90x90 xc:none -draw "roundrectangle 0,0 90,90 15,15" mask.png
```
3️⃣ **Apply the mask to the resized image:**

```bash
convert resized_image.png mask.png -alpha set -compose DstIn -composite image_rounded.png
```
