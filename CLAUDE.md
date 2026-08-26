# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software codebase** — it's the working directory for a team's submission to the
**Business Plan Competition (BPC) IFest 2026** (Informatics Festival, HIMATIF UNPAD). There is no
build, lint, or test tooling; the deliverable is a PDF business-plan proposal plus a Business Model
Canvas (BMC). Work here is research, writing, and document formatting, not engineering.

Team (per `BPC Testing.md`): Hansel Stevan Boike (Universitas Padjadjaran), Bryan Patrick Kurniawan
(Universitas Bina Nusantara), Michael Hau (Universitas Tarumanegara).

## Files

- **`GUIDEBOOK BPC IFEST 2026.pdf`** — the official rules. Source of truth for every constraint
  below. `pdftoppm` (page rendering) is not installed in this environment, so the Read tool cannot
  render pages directly — extract text instead with `pdftotext -layout "GUIDEBOOK BPC IFEST 2026.pdf" out.txt`.
- **`BPC Testing.md`** — the working proposal draft. Currently an empty skeleton that mirrors the
  official chapter structure (headings only, no body content yet).
- **`Contoh BMC.md`** — an example/reference Business Model Canvas showing the expected table format
  and the level of detail expected per cell (1-2 short bullet points per BMC element is acceptable).
- **`SUBTHEME-ANALYSIS.md`** — deep research deciding which of the four subtemas to build the
  business plan around. Verdict: **Green & Sustainable Technology**, specifically **AI-Driven Industrial Combustion Optimization (BurnAI)**. Next stage is Customer/Problem Validation.

## Competition constraints (hard requirements — treat as fixed, not preferences)

**Theme:** "Waves of Innovation: Structuring Tech for Real Impact." Every proposal must pick **at
least one** subtema and the business idea must genuinely implement technology (not cosmetic AI):

1. Smart Cities & Communities — public services, urban mobility, integrated security, community connectivity
2. Industry 5.0 Innovation — advanced tech integrated with human needs, human-centric value
3. Green & Sustainable Technology — renewable energy, smart grid, carbon management, circular economy, green computing
4. Digital Ecosystem & Super Apps — integrated multi-service platforms (Gojek/Grab/WeChat-style)

**Required proposal structure** (this is the section order `BPC Testing.md` must follow):

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
- Cover and BMC must follow the official template/logo (linked from the guidebook, not stored in this repo)

**Team/registration constraints:** teams of 2-3 active S1/D4/D3 students; one team per person; BMC
must be attached to the preliminary-round proposal; top 10 teams advance to the final (pitching) round.

**Key dates (2026):** proposal submission window 27 Jul – 30 Aug; finalist announcement 13 Sep;
technical meeting 15 Sep; mentoring 18 Sep; pitch deck submission 14–19 Sep; pitching day 20 Sep;
winners announced 3 Oct.

## Working conventions

- Treat the guidebook PDF as authoritative over any summary (including this file) if they ever
  conflict — re-extract and re-check rather than trusting a stale paraphrase.
- Every claim/statistic used to justify the business idea (market size, problem cost, affected
  population, etc.) needs a real, checkable source (year, geography, publisher). Do not invent
  numbers; if evidence can't be found, say so explicitly and mark unavoidable estimates as
  **assumption**, not fact.
- When drafting `BPC Testing.md`, keep the 15-page limit (Bab 1–Kesimpulan) in mind — this caps how
  much depth each subsection can carry versus how much belongs in the appendix instead.
