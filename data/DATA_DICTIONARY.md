# Data dictionary (Supplementary Table S4: data sources by series)

All files are UTF-8 CSV.

- `fy` is the Japanese fiscal year (April to March).
- Claims are counted by fiscal year of filing; decisions and approvals by fiscal year of decision.
- Counts are for work-related cases. Cases under the "multiple-employment factor" category introduced in 2020 are excluded.
- Every value is transcribed in `code/build_data.py`, with the source and cross-checks noted next to it.
- Unless stated otherwise, the source is:
  - "Annual report": MHLW, 過労死等の労災補償状況 (Status of workers' compensation for karoshi and related disorders), annexes 1 (CCVD) and 2 (mental disorders).
  - Editions are cited by Japanese era year (令和5年度版 = FY2023 edition).
  - Each edition reports the current and preceding fiscal years. Values for overlapping years were checked against each other.

## `cvd_national.csv` — cerebro-cardiovascular disease (CCVD), national totals

| column | meaning |
|---|---|
| `fy` | fiscal year, 2001–2025 |
| `claims`, `claims_death` | 請求件数 (claims filed); of which deaths |
| `decisions`, `decisions_death` | 決定件数 (claims decided); of which deaths |
| `approvals`, `approvals_death` | 支給決定件数 (claims approved as work-related); of which deaths |

| Fiscal years | Variables | Source |
|---|---|---|
| FY2001–2019 | claims and approvals | MHLW, Expert Committee on Recognition Criteria for CCVD, 2nd meeting, material 1 (2020; mhlw.go.jp/content/11201000/000650614.pdf), table 1 |
| FY2008–2012 | decisions | Osaka Labour Bureau, press release of 27 June 2013, table 1-1 (national column) |
| FY2013 | decisions | Annual report, 平成29年度版, table 1-1 |
| FY2014–2018 | decisions | Annual report, 平成30年度版, table 1-1 |
| FY2019–2025 | all variables | Annual report, 令和5年度版 and 令和7年度版, table 1-1; FY2020–2024 also checked against 令和6年度版 |

## `cvd_overtime_bands.csv` — CCVD approvals by overtime category

| column | meaning |
|---|---|
| `fy` | fiscal year, 2007–2025 |
| `period` | `combined` (the 1-month and 2–6-month evaluation periods together); `m1` (1-month table); `m26` (2–6-month table); `m1+m26` (category `other`, reported once) |
| `band` | average monthly overtime in the evaluation period: `lt45`, `45_60`, `60_80`, `80_100`, `100_120`, `120_140`, `140_160`, `ge160` (hours); `other` = short-term overload or extraordinary events |
| `n` | approvals |
| `source` | source label |

| Fiscal years | Rows | Source |
|---|---|---|
| FY2007–2019 | `combined` | Expert committee material 1 (2020), table 5 |
| FY2017–2025 | `m1` and `m26` | Annual reports, table 1-6, in the following editions: 平成30年度版 (FY2017–2018), 令和2年度版 (FY2019–2020), 令和4年度版 (FY2021), 令和5年度版 (FY2022–2023), 令和7年度版 (FY2024–2025) |
| FY2020–2025 | `combined` | Sum of the `m1` and `m26` rows |

The order of the rows was checked against the narrative text of each report, which states the most frequent category. For every year, the `combined` rows sum to the approvals in `cvd_national.csv`.

## `cvd_by_type.csv` — CCVD by disease type

| column | meaning |
|---|---|
| `fy` | fiscal year |
| `type` | 脳血管疾患 (cerebrovascular disease); 虚血性心疾患等 (ischaemic heart disease and other cardiac conditions, including severe heart failure from September 2021) |
| `approvals` | approvals |
| `claims`, `decisions`, deaths | available only for FY2020 and FY2022–2025 |

| Fiscal years | Variables | Source |
|---|---|---|
| FY2001–2019 | approvals | Expert committee material 1 (2020), table 6 |
| FY2020, FY2022–2025 | all variables | Annual reports, table 1-5 (total row) |
| FY2021 | approvals | White Paper on Measures to Prevent Karoshi, 2024 edition (令和6年版過労死等防止対策白書), figure 4-1-1-4 |

## `mental_national.csv` — mental disorders, national totals

| column | meaning |
|---|---|
| `fy` | fiscal year, 1999–2025 (decisions from FY2009) |
| `claims`, `decisions`, `approvals` | national totals |
| `claims_suicide`, `decisions_suicide`, `approvals_suicide` | suicides, including attempts, FY2009–2025 |

Sources:
- FY1999–2020: MHLW, Expert Committee on Recognition Criteria for Mental Disorders, 1st meeting (December 2021; mhlw.go.jp/content/11201000/000862995.pdf).
- FY2019–2025: Annual reports, annex 2, table 2-1 (令和5年度版 and 令和7年度版).
- Built from `rosai_mental_national.csv`.

## `mental_overtime_bands.csv` — mental disorder approvals by monthly overtime category

| column | meaning |
|---|---|
| `fy` | fiscal year, 2017–2025 |
| `band` | overtime in the month before onset: `lt20`, `20_40`, `40_60`, `60_80`, `80_100`, `100_120`, `120_140`, `140_160`, `ge160` (hours); `other` = judged work-related without the need to examine working hours (その他) |
| `n` | approvals |

Sources (annual reports, table 2-6, unless noted):

| Fiscal years | Edition |
|---|---|
| FY2017–2018 | 平成30年度版 |
| FY2019 | 令和元年度版 |
| FY2020 | Expert committee material (2021) |
| FY2021 | 令和4年度版 |
| FY2022–2023 | 令和5年度版 |
| FY2024–2025 | 令和7年度版 |

FY2020–2024 were also checked against 令和6年度版, tables 2-1 and 2-6. The rows for each year sum to the approvals in `mental_national.csv`.

## `mental_processing_time.csv` — mental disorders, mean time from claim to decision

| column | meaning |
|---|---|
| `fy` | fiscal year, 2007–2024 |
| `mean_months`, `median_months` | months (median for FY2007–2020 only) |
| `days` | days |

| Fiscal years | Source and conversion |
|---|---|
| FY2007–2020 | Months, from expert committee material (2021), section 8. Converted to days as months × 30, the conversion used in the source. |
| FY2021–2024 | Days, from MHLW policy evaluation pre-analysis sheets, policy objective III-3-1 (FY2024 and FY2025 editions), performance indicator on processing time |

FY2020 (255 days) matches in both sources.

## Files shared with a related repository

These files are transcribed in the same way as in https://github.com/mestate-academic/overtime-caps-mental-disorders-japan.

| File | Content | Source |
|---|---|---|
| `rosai_mental_national.csv` | mental disorders, national claims, decisions and approvals | Annual reports, table 2-1 |
| `rosai_mental_by_industry.csv` | mental disorders by industry: `fy`, `industry` (Japanese Standard Industrial Classification divisions), `approvals`, `claims` | Annual reports, table 2-2 |
| `rosai_cvd_by_industry.csv` | CCVD by industry: `fy`, `industry`, `cvd_claims`, `cvd_approvals` | Annual reports, table 1-2 |
| `employment_by_industry.csv` | employed persons by industry, in 10,000 persons; `year` (calendar year), used as the denominator for the fiscal year beginning in that year | Statistics Bureau of Japan, Labour Force Survey, basic tabulation, table 2-5-1, annual averages |
