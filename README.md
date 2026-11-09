# Revisions of recognition criteria for overwork-related disease and workers' compensation in Japan, 2009–2025

Data and code for the manuscript "Revising recognition criteria for overwork-related disease changed who was compensated, not how many: an interrupted time series and within-category analysis of national workers' compensation data in Japan, 2009–2025" by Hironori Uematsu (Uematsu Occupational Physician's Office / Mestate LLC, Kyoto, Japan). Correspondence: office@mestate.jp.

Repository: https://github.com/mestate-academic/recognition-criteria-revisions-japan

Journal: submitted to the *American Journal of Industrial Medicine*.

## What is here

| Folder | Contents |
|---|---|
| `data/` | Transcribed public statistics (CSV, UTF-8). See `data/DATA_DICTIONARY.md` for every file, column and source. This dictionary is also Supplementary Table S4 of the paper. |
| `code/` | Python scripts that build the datasets, run the analyses and draw the figures. |
| `output/` | Results as text files (`results_*.txt`), intermediate CSVs and Figures 1–3 (PNG). These are produced by the code. |
| `manuscript/` | Manuscript text (Markdown). |

All data are aggregate statistics published by the Japanese government; no individual-level data are included.

## Reproducing the results

Requirements: Python ≥3.11 with the packages in `requirements.txt`. The code was tested with Python 3.13, pandas, numpy, statsmodels, scipy and matplotlib. Figures use the Noto Sans CJK font if it is installed, and otherwise the matplotlib default.

Run everything from the repository root:

```bash
pip install -r requirements.txt
bash run_all.sh
```

| Step | Script | Produces |
|---|---|---|
| 1 Build data | `code/build_data.py` | The analysis CSVs in `data/`. The committed CSVs are identical to the script's output. The script contains every transcribed value, with the source document, table number and cross-checks (sums against totals, overlapping editions) written next to the numbers. |
| 2 First pass | `code/analyze1.py` | `output/results_v1.txt`: decomposition, first-pass interrupted time series, overtime-category tables, the share of approvals below the thresholds by evaluation period (FY2017–2025). Also `output/A_decomposition.csv`, `C_cvd_bands.csv`, `D_mental_bands.csv`. |
| 3 Robustness | `code/analyze2.py` | `output/results_v2.txt`: interrupted time series sensitivity analyses (window, transition-year coding, slope change, Newey–West, placebo years) and the industry analysis of the 2023 revision (wild cluster score bootstrap with Webb weights, seed 20261109; permutation of industry labels). |
| 4 Main estimates | `code/analyze4_unified.py` | `output/results_v3_unified.txt`: all main estimates for the common window FY2009–2025. This covers Table 1, Table 2 (including the permutation test, in-time placebo and specificity contrasts) and the ratio models in Table 3. |
| 5 Figures | `code/make_figures_en.py` | `output/AJIM_Figure1.png` to `AJIM_Figure3.png` |

### Where each number in the paper comes from

| Paper | Source |
|---|---|
| Table 1, decomposition and level changes | `results_v3_unified.txt` sections A and B (CCVD and the three mental disorder steps); mental disorder period means in `output/A_decomposition.csv` |
| Table 2 | `results_v3_unified.txt` section C |
| Table 3 | `data/mental_overtime_bands.csv`, `data/mental_processing_time.csv`; ratio changes in `results_v3_unified.txt` section D |
| Share below either threshold, FY2017–2025 | `results_v1.txt` section C |
| Table S2 (sensitivity of interrupted time series) | `results_v3_unified.txt` section B (CCVD main and no-trend models); `results_v2.txt` sections I and I2 (other windows and the mental disorder sensitivity analyses) |
| Table S3 (industries) | `results_v2.txt` section J |

## Analysis in brief

- **Revisions evaluated:**
  - cerebro-cardiovascular disease (CCVD) criteria, 14 September 2021 (Notification Kihatsu 0914 No. 1);
  - mental disorder criteria, 26 December 2011 (Kihatsu 1226 No. 1);
  - partial revision of the mental disorder criteria, 29 May 2020 (Kihatsu 0529 No. 1);
  - revised mental disorder criteria, 1 September 2023 (Kihatsu 0901 No. 2).
- **Interrupted time series:** quasi-Poisson models for annual claims, decisions and approvals, and a quasi-binomial model for the approval rate (approvals divided by decisions, weighted by decisions). Each model has a linear trend and a post-revision step. Transition years (FY2021 for CCVD, FY2023 for mental disorders) are excluded.
- **Within-category analysis (CCVD):** quasi-Poisson model of approvals by overtime category with year fixed effects, using an interaction between the targeted category and the post-revision period.
  - Main contrast: <80 versus ≥80 overtime hours per month, FY2022–2025 versus FY2009–2020.
  - Robustness: exact permutation test over all 1,820 assignments of 4 post-revision years among 16 non-transition years, and in-time placebo windows.
  - Specificity contrast: 80–100 versus ≥100 hours.
- **Mental disorders:** composition of approvals by overtime category, including approvals made without examining working hours (FY2017–2025), and mean processing time.

Fiscal years (FY) run from April to March; FY2025 = April 2025–March 2026. Claims are counted by fiscal year of filing, and decisions and approvals by fiscal year of decision.

## Sources of the data

All sources are Japanese government publications. Details per file are in `data/DATA_DICTIONARY.md`.

- Ministry of Health, Labour and Welfare (MHLW), 過労死等の労災補償状況 (Status of workers' compensation for karoshi and related disorders), annual editions with annex tables 1 (cerebro-cardiovascular disease) and 2 (mental disorders).
- MHLW, materials of the Expert Committee on Recognition Criteria for Cerebrovascular and Cardiovascular Diseases (2020), and of the Expert Committee on Recognition Criteria for Mental Disorders (2021).
- MHLW, policy evaluation pre-analysis sheets for policy objective III-3-1 (FY2024 and FY2025 editions), for processing time.
- Osaka Labour Bureau, press release of 27 June 2013 (national column of table 1-1), for CCVD decisions in FY2008–2012.
- White Paper on Measures to Prevent Karoshi (2024 edition), for CCVD approvals by disease type in FY2021.
- Statistics Bureau of Japan, Labour Force Survey, basic tabulation, table 2-5-1 (employed persons by industry), used for the supplementary industry analysis.

## Licence

- Code: MIT License (see `LICENSE`).
- Transcribed data (`data/`) and outputs: CC BY 4.0.
- The underlying statistics are published by the Government of Japan under its Standard Terms of Use, which are compatible with CC BY 4.0. Please credit them to the issuing ministry.

## Citation

See `CITATION.cff`. Please cite the paper once it is published; until then, cite this repository.
