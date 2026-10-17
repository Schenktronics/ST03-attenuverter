# PDFs

Printable versions of the docs:

- [User Manual (PDF)](ST-03_Attenuverter_User_Manual.pdf)
- [Assembly Guide (PDF)](ST-03_Attenuverter_Assembly_Guide.pdf)

These are built from [`../manual.md`](../manual.md) and [`../assembly-guide.md`](../assembly-guide.md). **Don't edit the PDFs by hand.** Edit the Markdown instead.

The build tool lives in [schenktronics-docs-tools](https://github.com/Schenktronics/schenktronics-docs-tools), so this repo only holds its settings, in [`config.json`](config.json): the product name, PCB version, and which documents to build.

## Automatic builds

The [Build PDFs workflow](../../.github/workflows/pdf.yml) rebuilds the PDFs whenever the docs, their images, or `config.json` change on `main`, and commits the new PDFs back. After you push a docs change, wait a minute and then `git pull` to get the rebuilt PDFs.

After an update to schenktronics-docs-tools, run the workflow by hand from the repo's **Actions** tab to rebuild with the new version.

## Previewing locally

See [Previewing locally](https://github.com/Schenktronics/schenktronics-docs-tools#previewing-locally) in the tools repo. In short:

```sh
node ~/Products/schenktronics-docs-tools/pdf/build.mjs docs/pdf/config.json
```

Don't commit the PDFs this produces. Let the workflow build the committed copies.
