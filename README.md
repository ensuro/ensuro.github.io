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

1. **Resize the image to 200x200 pixels and convert it to grayscale:**

```bash
convert /route/to/image.png -resize 200x200^ -gravity center -extent 200x200 -colorspace Gray resized_grayscale_image.png
```
2. **Create a mask with rounded corners:**

```bash
convert -size 200x200 xc:none -draw "roundrectangle 0,0 199,199 50,50" mask.png
```
3. **Apply the mask to the resized grayscale image:**

```bash
convert resized_grayscale_image.png mask.png -alpha set -compose DstIn -composite team_member.png
```

### To format partners & investors images from jpg/jpeg to png using ImageMagick, follow these steps:

```bash
convert /route/to/image.jpg -fuzz 20% -transparent white output.png
```

### To format partner images using ImageMagick, follow these steps:

1. **Resize the image to 90x90 pixels and convert it to grayscale:**

```bash
convert /route/to/image.png -resize 90x90^ -gravity center -extent 90x90 resized_image.png
```
2. **Create a mask with rounded corners:**

```bash
convert -size 90x90 xc:none -draw "roundrectangle 0,0 90,90 15,15" mask.png
```
3. **Apply the mask to the resized image:**

```bash
convert resized_image.png mask.png -alpha set -compose DstIn -composite image_rounded.png
```