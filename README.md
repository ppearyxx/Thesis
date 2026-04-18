# Thesis

KMUTT CPE undergraduate thesis — LaTeX source.

## Layout

```
Thesis/
├── Report/                 LaTeX source for the thesis
│   ├── main.tex            entry point — compile this
│   ├── latexmkrc           build config
│   ├── chapters/           one file per chapter/section
│   ├── figures/            images
│   ├── bibliography/       .bib and .bst files
│   ├── template/           original KMUTT sample (reference only)
│   └── *.cls               required class files — do not move
└── Docs/                   separate, unrelated work
```

## Requirements

Install MacTeX (once):

```sh
brew install --cask mactex-no-gui
```

This provides `xelatex`, `bibtex`, and `latexmk`. Restart your terminal afterward so the new binaries are on `PATH`.

The Thai fonts in the template expect **TH Sarabun New** — install from [f0nt.com](https://www.f0nt.com/release/th-sarabun-new/) if missing.

## Build

```sh
cd Report
latexmk                 # produces main.pdf
latexmk -pvc            # watch mode — rebuilds on save
latexmk -c              # clean intermediates, keep PDF
latexmk -C              # clean everything
```

## Write

1. Edit the **project metadata** block in [Report/main.tex](Report/main.tex) (title, author, advisors, year).
2. Write chapters in [Report/chapters/](Report/chapters/) — one file per chapter. Add new chapters by creating a file and `\input{chapters/xx-name}` in `main.tex`.
3. Drop images in [Report/figures/](Report/figures/) and reference by basename:
   ```latex
   \includegraphics[width=10cm]{myplot.png}
   ```
4. Add citations to [Report/bibliography/cpe.bib](Report/bibliography/cpe.bib) and cite with `\cite{key}`.

## Recommended VS Code setup

Install the **LaTeX Workshop** extension. It auto-detects `latexmkrc`, provides:
- on-save compile
- side-by-side PDF preview
- SyncTeX: ⌘+click in the PDF jumps to the source line
- `.bib` intellisense for citations

## Reference

The original KMUTT sample (English + Thai) is kept intact in [Report/template/sample/](Report/template/sample/) for when you need to see how a feature is used.
