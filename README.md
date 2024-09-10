# Ensuro Website

This repository has the Ensuro website hosted in https://ensuro.co using GitHub pages.

The HTML files are generated from Jinja2 templates, so the changes need to be done on the .j2 files.

After changing the .j2 files, using the script `./generate.sh`, the HTML are refreshed.

To test locally, you can just run `<browser> index.html`.

To deploy, just commit and push the HTML files.

The input parameters for the Jinja2 templates are defined in the file `input.yaml`.

## Formatting Team Images with ImageMagick

### Optional: Install ImageMagick

```bash
sudo apt-get install imagemagick
```

### To format team member images using ImageMagick, follow these steps:

1. **Resize the image to 500x500 pixels and convert it to grayscale:**

```bash
convert ./static/assets/team_lucas.png -resize 500x500^ -gravity center -extent 500x500 -colorspace Gray team_lucas_resized_grayscale.png
```
2. **Create a mask with rounded corners:**

```bash
convert -size 500x500 xc:none -draw "roundrectangle 0,0 499,499 50,50" mask.png
```
2. **Apply the mask to the resized grayscale image:**

```bash
convert team_lucas_resized_grayscale.png mask.png -alpha set -compose DstIn -composite team_lucas_final_fixed.png
```