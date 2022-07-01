# Ensuro Website

This repository has the Ensuro website hosted in https://ensuro.co using GitHub pages.

The HTML files are generated from Jinja2 templates, so the changes need to be done on the .j2 files.

After changing the .j2 files, using the script `./generate.sh`, the HTML are refreshed.

To test locally, you can just run `$BROWSER $PWD/index.html`.

To deploy, just commit and push the HTML files.

The input parameters for the Jinja2 templates are defined in the file `input.yaml`.
