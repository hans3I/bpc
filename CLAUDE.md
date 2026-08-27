# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software codebase** — it's the working directory for a team's submission to the
**Business Plan Competition (BPC) IFest 2026** (Informatics Festival, HIMATIF UNPAD). The deliverable
is a compiled **PDF business-plan proposal** (LaTeX source under `proposal/`) plus a Business Model
Canvas (BMC) in the appendix. Work here is research, writing, and document formatting, not
engineering. The only "build" is the XeLaTeX/biber compile described below.

Team (per `proposal/sections/lampiran-2-biodata.tex`): Hansel Stevan Boike (Universitas Padjadjaran),
Bryan Patrick Kurniawan (Universitas Bina Nusantara), Michael Hau (Universitas Tarumanegara).

## Current state (2026-08-27)

The proposal is **built and submitted-ready**: the business idea is **"Alurin"**, an asset-light
B2B/B2G IoT+AI SaaS platform for Jakarta waste logistics — ultrasonic fill-level sensors on TPS/
commercial containers, AI Dynamic Routing Engine, Predictive RDF Allocation System — targeting Bantar
Gebang TPA overload and RDF Plant Rorotan feedstock. Compiled `proposal/main.pdf` is 28 pages;
Bab 1→Kesimpulan = **14 pages** (within the hard 15-page cap). Remaining pre-submission TODOs
(deadline 30 Aug 2026): recompile `main.pdf` after recent edits, swap the placeholder cover logo for
the official IFest 2026 logo, fill Lampiran 2 biodata fields per member.

## Files

- **`GUIDEBOOK BPC IFEST 2026.pdf`** — the official rules. Source of truth for every constraint
  below. `pdftoppm` (page rendering) is not installed in this environment, so the Read tool cannot
  render pages directly — extract text instead with `pdftotext -layout "GUIDEBOOK BPC IFEST 2026.pdf" out.txt`
  (see `extract_guidebook.py` / `guidebook_text.txt` for the already-extracted text).
- **`proposal/`** — **the actual deliverable** (LaTeX source + compiled PDF):
  - `main.tex` — document root. `\ProductName` macro (one-line product-name swap) at line 87,
    `\ProposalTitle` at line 88. A4, 4/3/3/3 cm margins, Times New Roman (with TeX Gyre Termes
    fallback), 1.5 spacing, APA 7 via biblatex/biber, page numbers from Bab 1.
  - `sections/*.tex` — 13 files: `00-cover`, `01-kata-pengantar`, `02-daftar-isi`,
    `03-executive-summary`, `bab1`–`bab6`, `daftar-pustaka`, `lampiran-1-bmc`, `lampiran-2-biodata`.
  - `referensi.bib` — 33 fact-checked bibliography entries.
  - `main.pdf` — **the compiled deliverable** (tracked in git; build artifacts are gitignored).
- **`SUBTHEME-ANALYSIS.md`** — subtheme-selection research. Marked **SUPERSEDED**; the dated
  addendum (2026-08-26) documents the pivot from the earlier BurnAI idea to Alurin, the committed
  direction. Do **not** treat the BurnAI sections as current.
- **`BPC Testing.md` / `BPC Testing.txt`** — legacy pre-LaTeX draft skeleton (superseded by
  `proposal/`). `BPC Testing.txt` is what the fact-check round was run against.
- **`Contoh BMC.md`** — an example/reference Business Model Canvas showing the expected table format
  and the level of detail expected per cell (1-2 short bullet points per BMC element is acceptable).
- **`extract_guidebook.py`**, **`guidebook_text.txt`** — guidebook PDF text extraction (see above).
- **`aic-project-main.zip`** — unrelated archived research artifact; ignore.

## Competition constraints (hard requirements — treat as fixed, not preferences)

**Theme:** "Waves of Innovation: Structuring Tech for Real Impact." Every proposal must pick **at
least one** subtema and the business idea must genuinely implement technology (not cosmetic AI):

1. Smart Cities & Communities — public services, urban mobility, integrated security, community connectivity
2. Industry 5.0 Innovation — advanced tech integrated with human needs, human-centric value
3. Green & Sustainable Technology — renewable energy, smart grid, carbon management, circular economy, green computing
4. Digital Ecosystem & Super Apps — integrated multi-service platforms (Gojek/Grab/WeChat-style)

**Required proposal structure** (implemented in `proposal/sections/*.tex`):

```
Cover → Kata Pengantar → Daftar Isi → Executive Summary
Bab 1  Pendahuluan          (1.1 Latar Belakang Bisnis, 1.2 Tujuan Bisnis, 1.3 Manfaat Bisnis)
Bab 2  Analisis Produk/Jasa (2.1 Deskripsi, 2.2 Keunggulan, 2.3 Alur Produksi/Jasa, 2.4 Rencana Pengembangan)
Bab 3  Analisis Pasar       (3.1 SWOT, 3.2 Target & Segmen Pasar, 3.3 Strategi Pemasaran)
Bab 4  Rencana Operasional & Manajemen (4.1 Struktur Organisasi, 4.2 Kebutuhan SDM)
Bab 5  Analisis Keuangan    (5.1 Modal Awal, 5.2 Struktur Biaya, 5.3 Proyeksi Laba Rugi, 5.4 Kelayakan Usaha)
Bab 6  Penutup              (6.1 Kesimpulan)
Daftar Pustaka → Lampiran (Lampiran 1: BMC, Lampiran 2: Biodata)
```

**Formatting rules for the final PDF:**
- A4 paper; margins 4 cm left, 3 cm top/right/bottom
- Titles: Times New Roman 14pt, bold, centered, 1.5 spacing
- Body text: Times New Roman 12pt, 1.5 spacing, justified
- Page numbers: bottom-right, Arabic numerals, starting from Bab 1 through Lampiran
- Citations and bibliography: APA 7th edition
- Submission format: PDF only
- **Page limit: max 15 pages, counted from Bab 1 through Kesimpulan** (cover, kata pengantar, daftar isi, executive summary, daftar pustaka, and lampiran are outside this count)
- Cover and BMC must follow the official template/logo (linked from the guidebook — `bit.ly/LogodanTemplateBPCIFEST2026` — not stored in this repo; the cover currently has a placeholder logo box)

**Team/registration constraints:** teams of 2-3 active S1/D4/D3 students; one team per person; BMC
must be attached to the preliminary-round proposal; top 10 teams advance to the final (pitching) round.

**Key dates (2026):** proposal submission window 27 Jul – 30 Aug; finalist announcement 13 Sep;
technical meeting 15 Sep; mentoring 18 Sep; pitch deck submission 14–19 Sep; pitching day 20 Sep;
winners announced 3 Oct.

## Building the PDF

Run from `proposal/` (XeLaTeX + biber are required; `xelatex` is on PATH via MiKTeX):

```
xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex
```

or simply `latexmk -xelatex -interaction=nonstopmode main.tex`. **Must be XeLaTeX** (fontspec /
Times New Roman); bibliography backend **must be biber** (not bibtex). Recompile after any `.tex`/
`.bib` edit and commit `main.pdf` (the deliverable) together with the source. Known-cosmetic: 6
`hyperref Warning: Token not allowed in a PDF string` entries (stripping `\\` from `Bab N\\...`
headings in PDF bookmarks) — harmless.

LaTeX gotchas (from the build history, in `bpc-project-pivot` memory):
- Chapter headings must use `\section{...}` (not starred) or subsection auto-numbering breaks.
- `tabularx` cells holding sentences must be `X` columns; `\multicolumn` needs explicit `p{...}`.
- The landscape BMC uses `rotating`'s `sidewaystable` (plain `lscape`/floats don't combine under this
  XeLaTeX/MiKTeX install); size with `\textheight`-based widths.

## Working conventions

- Treat the guidebook PDF as authoritative over any summary (including this file) if they ever
  conflict — re-extract and re-check rather than trusting a stale paraphrase.
- Every claim/statistic used to justify the business idea (market size, problem cost, affected
  population, etc.) needs a real, checkable source (year, geography, publisher). Do not invent
  numbers; if evidence can't be found, say so explicitly and mark unavoidable estimates as
  **assumption**, not fact. The verified source base lives in the `bpc-factcheck-findings` memory and
  `referensi.bib` — reuse it instead of re-deriving figures.
- Keep Bab 1→Kesimpulan ≤ 15 pages (currently 14). Lampiran/daftar pustaka/front matter are outside
  the cap — move overflow depth into the appendix rather than growing the main chapters.
- The proposal prose was largely AI-drafted; running `humanizer` over Bab 1–6 would make it read more
  naturally before a judge sees it.
