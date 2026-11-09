# Manuscript for American Journal of Industrial Medicine — v3 (anonymised main document)

---

## Title

Changes in the composition of workers' compensation approvals after revisions of the recognition criteria for overwork-related disease in Japan, 2009–2025: interrupted time series and within-category analyses

**Running title:** Recognition criteria revisions and compensated overwork-related disease

---

## Abstract (245 words, including headings)

**Background:** Recognition criteria determine which workers are compensated for overwork-related disease, yet revisions are rarely evaluated. In 2021, Japan revised its cerebro-cardiovascular disease (CCVD) criteria to allow recognition when overtime approached the "karoshi line" and other workload factors were present. Mental disorder criteria were revised in 2011, 2020 and 2023.

**Methods:** Using national statistics (fiscal years [FY] 2009–2025), we fitted interrupted time series models to claims, approvals and approval rates. For CCVD, we compared approvals with <80 versus ≥80 overtime hours per month using year-fixed-effects Poisson models, overall and by evaluation period. For mental disorders, we examined the composition of approvals.

**Results:** No significant level change in CCVD approvals was detected after 2021 (rate ratio [RR] 1.11, 95% CI 0.93–1.33), but the ratio of approvals with <80 to ≥80 overtime hours per month increased 4.27-fold (3.28–5.57). In the 2–6-month evaluation period, annual approvals with 80–100 hours fell from 82 to 48 and those with <80 hours rose from 17 to 43; the period total remained similar. For mental disorders, approval rates rose after 2011 (odds ratio 1.63, 1.34–1.99) and approvals after 2023 (RR 1.54, 1.37–1.74). Approvals made without examining hours rose from 139 (FY2017–2019) to 657 per year (FY2024–2025); mean processing time rose from 216 (FY2017) to 277 days (FY2024).

**Conclusions:** After Japan's 2021 revision, compensated CCVD cases shifted below the karoshi line without a detectable change in total approvals. Aggregate data cannot distinguish newly eligible workers from lower recorded hours among previously eligible workers.

**Keywords:** workers' compensation; occupational disease; karoshi; long working hours; mental disorders; harassment; interrupted time series; Japan

---

## 1 | INTRODUCTION

Workers' compensation systems translate evidence on work-related disease into eligibility rules. Where those rules are narrow, many workers whose disease or disability was caused by work receive no compensation,¹ and each step from illness to an accepted claim filters out cases.² For diseases with multifactorial causes, such as cerebro-cardiovascular disease (CCVD) and mental disorders, recognition criteria are the decisive filter: they specify which exposures, and at what level, establish work-relatedness. Long working hours are an established cause of coronary heart disease and stroke,³,⁴ and Japan, the Republic of Korea and Taiwan have each adopted explicit criteria for compensating overwork-related CCVD.⁵

Japan introduced the first such criteria, in 1961. Since 2001, CCVD has been regarded as strongly work-related when overtime reached about 100 hours in the month before onset or averaged about 80 hours per month over 2–6 months, thresholds widely known as the "karoshi line".⁶,⁷ In September 2021, after a review by an expert committee, the Ministry of Health, Labour and Welfare (MHLW) revised these criteria for the first time in 20 years.⁸,⁹ The revision kept the hour thresholds but stated explicitly that overtime approaching them, combined with other workload factors, could establish work-relatedness. It also added new workload factors, such as short rest intervals between shifts and physically demanding work, clarified the criteria for short-term overload and extraordinary events, and added severe heart failure as a compensable disease.⁹ Criteria for mental disorders were codified in 2011, replacing earlier guidelines,¹⁰ and revised in 2020 to add power harassment¹¹ and in 2023 to add customer harassment and other events.¹² Each revision was intended to make compensation easier to claim and faster to decide.

Whether such revisions work as intended is rarely examined. Lin and colleagues compared rates of compensated overwork-related CCVD in the 5 years before and after new criteria were introduced in Japan (2001) and Taiwan (2010), reporting increases in both countries (2.81-fold in Japan and 2.53-fold in Taiwan; 2.58-fold in a pooled model).¹³ In Korea, approval rates for occupational CCVD fell from 44.7% in 2006 to 12.9% in 2011 and rose to 41.3% by 2018 after successive changes to standards and procedures, but these changes were described rather than modelled.¹⁴ Outside East Asia, interrupted time series studies have evaluated reforms of Australian compensation systems,¹⁵,¹⁶ premium incentives in Finland¹⁷ and, most recently in this journal, presumptive coverage for post-traumatic stress disorder (PTSD) in Canada. There, presumptions were associated with a higher proportion of PTSD claims among lost-time claims, and presumptions restricted to PTSD were not associated with claims for other mental health conditions.¹⁸ In Japan, the 2021 revision has been explained by the administration,¹⁹ and approved cases have been analysed descriptively, including their working patterns,⁶,²⁰ but we found no quantitative evaluation of the 2020, 2021 or 2023 revisions.

Previous evaluations have examined total outcomes as well as selected subgroups, such as PTSD versus other mental health conditions,¹⁸ claim types¹⁵ or claim severity.¹⁷ For criteria revisions, the relevant subgroups are defined by the criteria themselves. Revisions usually target a defined category of cases, here workers with overtime below the karoshi line, while other forces act on the rest of the caseload. Between 2019 and 2024, for example, Japan introduced statutory caps on overtime,²¹ which might be expected to reduce the number of workers with very long hours. Totals could then remain unchanged while the composition of compensated cases changes. Conversely, an increase in totals could reflect claiming behaviour rather than any change in adjudication. The consequences of Japan's 2021 revision for approvals across the overtime categories that it addressed have not been quantified using national longitudinal data.

We therefore described changes in compensation for CCVD and mental disorders around the revisions using national data for fiscal years 2009–2025 and three complementary approaches: (1) a decomposition of approvals into claims, decisions and approval rates, analysed with interrupted time series; (2) a within-category comparison contrasting the overtime category addressed by the 2021 revision with other categories decided in the same year, overall and separately for each evaluation period; and (3) for mental disorders, an analysis of the composition of approvals and of processing time. Because the analyses use aggregate data and no concurrent control population, we report associations with the timing of the revisions rather than causal effects.

## 2 | METHODS

### 2.1 | Setting

Japan's Industrial Accident Compensation Insurance covers employees of almost all private employers. Claims for overwork-related disease are filed with local Labour Standards Inspection Offices, which investigate working hours and workplace events and decide whether the disease is work-related. They apply recognition criteria issued as notifications by the MHLW. Approved claimants receive medical care and wage-replacement benefits; survivors receive benefits after death.

The 2021 CCVD revision (notification of 14 September 2021, applied from 15 September 2021) had four elements.⁹,¹⁹ First, cases with overtime approaching but not reaching the karoshi line could be recognised when other workload factors were present. Second, the list of other workload factors was revised; rest intervals of less than about 11 hours between shifts and physically demanding work were added. Third, the conditions under which short-term overload and extraordinary events establish work-relatedness were clarified. Fourth, severe heart failure was added to the compensable diseases. The mental disorder criteria are summarised in Supplementary Table S1:
- **2011:** introduced a structured table for rating psychological load and limited review by a panel of specialists to difficult cases.¹⁰
- **2020:** added power harassment as an event category, following legislation requiring employers to prevent harassment.¹¹
- **2023:** added customer harassment and other events, broadened the recognition of aggravated pre-existing disorders, and further limited the cases that require a panel of specialists, so that more decisions could rest on the opinion of a single specialist.¹²

Under the mental disorder criteria, the psychological load of each workplace event is rated weak, moderate or strong. When a single event, such as severe harassment, violence or a serious accident, is rated strong on its own, work-relatedness can be established without reconstructing monthly overtime. This is a formal pathway in the criteria, not an omission of investigation.¹⁰,¹²

### 2.2 | Data

We used the MHLW's annual reports on compensation for overwork-related disorders (*karoshi-tō no rōsai hoshō jōkyō*). Each report is published in June for the preceding fiscal year (April to March).²² The reports give national numbers of claims, decisions and approvals for CCVD and mental disorders, including deaths and suicides. They also cross-tabulate approvals by the overtime recorded in the investigation, by disease type and by industry. Cases recognised from September 2020 as multiple-job work-related disease, in which loads at two or more employers are combined, are reported separately and were not included; they numbered 2–5 CCVD approvals per year in FY2021–2023.²²

- **CCVD decisions:** decisions for FY2009–2012 were taken from a regional labour bureau's republication of the national tables.
- **Overtime categories for CCVD approvals:** approvals for long-term overload are classified by average monthly overtime (<45, 45–60, 60–80, 80–100, 100–120, 120–140, 140–160 and ≥160 hours). Overtime is measured over the evaluation period under which the case was assessed: the month before onset (threshold about 100 hours) or 2–6 months before onset (threshold about 80 hours per month). A separate category covers short-term overload and extraordinary events.
  - FY2009–2019: tables combining the two evaluation periods, published by the expert committee.²³
  - FY2017 onwards: separate tables for each evaluation period in the annual reports. For FY2020 onwards we summed them to extend the combined series; in the overlapping years FY2017–2019 the sums equalled the committee's combined tables.
- **Mental disorders:** approvals are classified by monthly overtime in the same bands, plus an official category for cases judged work-related "without the need to examine working hours" (*rōdō jikan wo chōsa suru made mo naku*), that is, through the event-alone pathway described above. These tables are available for FY2017–2025.
- **Processing time:** mean time from claim to decision for mental disorders.
  - FY2009–2020: reported in months by an expert committee;²⁴ we converted to days by multiplying by 30, as in the source.
  - FY2021–2024: reported in days in the MHLW's policy evaluation documents.²⁵

All values were transcribed by hand from the source documents into a script that records the source document and table for every value. They were checked in three ways: across overlapping editions, by confirming that category tables summed to annual totals, and against the narrative text of the reports. Within the periods analysed, no values were missing, except mean processing time for FY2025, which had not been published. Claims are counted by fiscal year of filing, and decisions and approvals by fiscal year of decision; none of the series is counted by year of onset. The data dictionary (Supplementary Table S4) lists the source of every series.

### 2.3 | Outcomes

The outcomes were annual numbers of claims, decisions and approvals, and the approval rate. Because decisions in a year include claims filed in earlier years, we used decisions rather than claims as the denominator of the approval rate. Approvals per claim then equal the product of the decision ratio (decisions per claim) and the approval rate, so a change in approvals can be attributed to claiming, throughput or adjudication. Approvals by overtime category are published only for approved cases, so approval rates by overtime category cannot be calculated.

### 2.4 | Statistical analysis

**Interrupted time series.** We modelled annual counts with log-linear quasi-Poisson regression and the approval rate with logistic quasi-binomial regression weighted by decisions.²⁶⁻²⁸ Each model included a linear secular trend and a step indicator for the post-revision period. Dispersion was estimated from the Pearson χ² statistic.

- **CCVD:** the post-revision period was FY2022–2025. FY2021, during which the revision took effect, was excluded as a transition year.
- **Mental disorders:** all three revisions were modelled jointly over FY2009–2025, with steps from FY2012, FY2020 and FY2024. FY2023 was excluded as a transition year. FY2011, in which the criteria were issued in December, was treated as pre-revision.

Sensitivity analyses varied the analytic window and omitted the trend. For the 2023 revision, they also coded FY2023 as half-exposed or post-revision, added a change in slope from FY2020, refitted the models as ordinary least squares with Newey–West standard errors,²⁹ and placed placebo steps in FY2014–2019.

**Within-category analysis (CCVD).** We modelled approvals in category *g* and year *t* as log E[*Y*ₜ_g] = α_t + γ_g + δ·(target_g × post_t), with quasi-Poisson errors. The year fixed effects α_t absorb any influence common to all categories in a year, such as the total number of claims, administrative capacity, the COVID-19 pandemic or general shifts in claiming. They do not absorb influences that act on one category more than another. The exponentiated δ estimates the change in the ratio of targeted to reference approvals, comparing FY2022–2025 with FY2009–2020.

- **Main contrast:** <80 hours versus ≥80 hours per month, combining the two evaluation periods.
- **Robustness checks:**
  - Group-specific linear trends.
  - Alternative inference: standard errors clustered by year; and ordinary least squares of the annual log ratio with a linear trend and Newey–West standard errors.
  - Exclusion of single years (FY2013, an outlier; FY2020, the first pandemic year; FY2022, the first post-revision year), restriction of the pre-revision period to FY2015–2020, and redefinition of the target as <100 hours.
  - In-time placebo tests: pseudo-revisions defining 4-year windows wholly within the pre-revision period.
  - Ranking of the actual timing: we compared the observed change in the mean log ratio with all 1,820 ways of choosing 4 "post-revision" years from the 16 non-transition years. Because fiscal years are not exchangeable under a null hypothesis (overtime caps, the pandemic and claiming trends differ between years), we interpret this as a descriptive ranking, not as an exact test of a causal effect.
- **Evaluation-period analysis (FY2017–2025):** because the threshold is 100 hours for the 1-month period but 80 hours for the 2–6-month period, the combined <80-hour category does not coincide exactly with the cases the revision addressed, and the combined 80–100-hour category includes 1-month cases below the 1-month threshold. Using the period-specific tables, we therefore compared approvals below either threshold (<100 hours in the 1-month table or <80 hours in the 2–6-month table) with approvals above it, and examined each period separately, including 80–100 versus ≥100 hours within the 2–6-month period. We refer to these as categories operationally defined by the hour thresholds, because the revision addressed near-threshold hours combined with other workload factors, not every case below a threshold. The pre-revision period for these analyses was FY2017–2020. Because only 4 years are available on each side, we also report the main evaluation-period contrast with year-clustered standard errors, group-specific trends and Newey–West standard errors (Supplementary Table S5).
- **Elements addressed by the other parts of the revision:**
  - short-term overload and extraordinary events versus ≥80 hours;
  - ischaemic heart disease and other cardiac conditions versus cerebrovascular disease (severe heart failure was added).

The evaluation-period analyses and the alternative inference were added after internal review of an earlier draft and should be regarded as post hoc.

**Composition of mental disorder approvals.** For FY2017–2025, we used the same fixed-effects model to estimate changes in the ratio of approvals made without examining working hours to approvals with ≥80 hours, with steps at FY2020 and FY2024 (FY2023 excluded). Processing time was analysed descriptively.

**Supplementary analysis (exploratory).** The 2023 revision added customer harassment. We therefore compared approvals and claims in four customer-facing industries (wholesale and retail; accommodation and food services; medical, health care and welfare; education) with three other industries (manufacturing; information and communications; finance and insurance). The model was a difference-in-differences Poisson model with employment from the Labour Force Survey as an offset. With only 7 clusters, inference used a wild cluster score bootstrap with Webb weights³⁰,³¹ and permutation of industry labels (35 assignments).

Analyses used Python 3 (pandas, statsmodels). Reporting follows the STROBE and RECORD statements;³²,³³ the checklist is provided as Supporting Information. The availability of data and code is described in the Data Availability Statement.

### 2.5 | Ethics

The study used only publicly available aggregate statistics containing no information on identifiable individuals and therefore did not require ethical review.

## 3 | RESULTS

### 3.1 | Cerebro-cardiovascular disease: totals

From FY2009–2020 to FY2022–2025:
- mean annual claims rose from 826 to 1,028;
- decisions were stable (686 to 693);
- approvals fell from 268 to 217 (Table I).

The crude approval rate fell from 39.1% to 31.3%, continuing a decline that began in FY2013 (Table I). After accounting for the secular trends, no statistically significant change in the level of claims (RR 1.13, 95% CI 0.93–1.36), approvals (RR 1.11, 0.93–1.33) or the approval rate (OR 1.17, 0.90–1.51) was detected. The crude decline in approvals is consistent with the pre-existing downward trend. The approval rate estimate depended on the analytic window (Supplementary Table S2). Shorter pre-revision windows produced increases (OR 1.59–1.96) and a simple before–after comparison produced a decrease (OR 0.71). We therefore regard the change in the overall approval rate as indeterminate.

### 3.2 | Cerebro-cardiovascular disease: composition

The composition of approvals changed markedly (Figure 1; Table II).

| Approvals per year | FY2009–2020 | FY2022–2025 |
|---|---:|---:|
| <80 overtime hours/month | 18.6 | 48.5 |
| ≥80 overtime hours/month | 230.9 | 141.0 |
| Short-term overload and extraordinary events | 18.9 | 27.5 |

- The share of approvals with <80 hours averaged 7.0% before the revision and 22.5% afterwards.
- The ratio of <80-hour to ≥80-hour approvals increased 4.27-fold (95% CI 3.28–5.57) relative to the pre-revision period.
- The ratio increased 3.81-fold (2.22–6.53) when group-specific trends were allowed.

### 3.3 | Robustness

- **Alternative inference:** with standard errors clustered by year, the ratio change was 4.27 (2.95–6.20), and 3.81 (1.73–8.37) with group-specific trends. Ordinary least squares of the annual log ratio with Newey–West standard errors gave 3.88 (2.33–6.48).
- **Excluding single years or restricting the pre-revision period:** estimates ranged from 4.01 to 4.54 (Table II).
- **In-time placebo tests:** placebo windows in the pre-revision period produced ratio changes of 0.71–1.12.
- **Ranking of the actual timing:** the observed change (4.39-fold on the unweighted log-ratio scale) was the largest of all 1,820 possible assignments of post-revision years (Figure 3A).
- **Short-term overload and extraordinary events:** approvals increased relative to ≥80-hour approvals (2.38, 1.46–3.89).
- **Disease type:** the ratio of cardiac to cerebrovascular approvals did not change (0.98, 0.86–1.11), consistent with the small number of approvals for severe heart failure (4 in FY2021 and 2 in FY2022).

### 3.4 | Cerebro-cardiovascular disease: evaluation periods

Table III and Figure 3B show approvals separately for the two evaluation periods in FY2017–2025.

- **Below either threshold:** approvals below the threshold of their evaluation period were 7.1%–12.0% of approvals in FY2017–2020, 20.9% in FY2021 and 22.7%–33.5% in FY2022–2025. Relative to approvals above the thresholds, they increased 4.26-fold (2.84–6.37; 2.40–7.55 with year-clustered standard errors). The estimate was less precise when group-specific trends were allowed (3.60, 1.25–10.35), and its confidence interval included 1 when standard errors were also clustered by year (0.50–25.87); ordinary least squares with Newey–West standard errors gave 2.88 (1.31–6.32; Supplementary Table S5).
- **1-month period:** approvals with ≥100 hours fell from 75.8 to 44.3 per year, and those with <100 hours rose from 3.8 to 17.3 (ratio change 7.87, 3.32–18.65).
- **2–6-month period:** approvals with 80–100 hours fell from 82.3 to 48.3 per year, those with <80 hours rose from 17.0 to 42.5, and those with ≥100 hours changed little (33.8 to 37.3). The period total remained similar (133.0 and 128.0). Approvals with <80 hours increased relative to those with ≥100 hours (2.27, 1.32–3.89), whereas approvals with 80–100 hours decreased relative to those with ≥100 hours (0.53, 0.40–0.71).
- **Combined table:** the contrast of 80–100 versus ≥100 hours did not change (0.96, 0.81–1.13), because 1-month cases below the 1-month threshold entered the 80–100-hour band after the revision (3%–5% of the band in FY2017–2020; 10%–31% in FY2022–2025) and offset the decline in 2–6-month cases. This contrast therefore cannot serve as a negative control.

Thus, approvals above the threshold declined in the 1-month period, and approvals in the adjacent 80–100-hour category declined in the 2–6-month period, while approvals below the thresholds increased; the number of approvals based on long-term overload did not increase. With only 4 years before and after the revision, the evaluation-period analysis is descriptive evidence that is consistent with the main contrast but cannot confirm it independently.

### 3.5 | Mental disorders: totals

Claims rose from 1,136 in FY2009 to 4,958 in FY2025, and approvals from 234 to 1,082 (Figure 2A). The three revisions were associated with different components (Table I).

- **2011:**
  - The approval rate increased (OR 1.63, 1.34–1.99) and approvals increased (RR 1.50, 1.28–1.77).
  - Claims did not change (RR 0.88, 0.74–1.06).
- **2020:**
  - Approvals increased (RR 1.22, 1.06–1.40).
  - Claims (RR 0.99, 0.85–1.16) and the approval rate (OR 1.12, 0.94–1.33) did not change clearly.
- **2023:**
  - Claims (RR 1.43, 1.26–1.63) and approvals (RR 1.54, 1.37–1.74) increased.
  - The approval rate was unchanged (OR 0.94, 0.81–1.08).
  - Placebo steps in FY2014–2019 ranged from 0.94 to 1.07 for claims and from 0.90 to 1.04 for approvals (Supplementary Table S2).
  - The increase in claims after 2023 was not distinguishable from a steepening of the trend that began in FY2020: when a change in slope from FY2020 was added, the step in claims became 1.00 (0.85–1.18), whereas the step in approvals remained (1.32, 1.02–1.71).

Approvals for suicide, including attempts, ranged from 63 to 99 per year throughout and did not share the increase.

### 3.6 | Mental disorders: composition and processing time

Approvals with ≥80 and <80 overtime hours each remained between about 150 and 230 per year from FY2017 to FY2025 (Figure 2C; Table IV). Approvals made without examining working hours rose from 139 per year in FY2017–2019 to 315 in FY2020–2022 and 657 in FY2024–2025. Their share of all approvals therefore rose from 24%–31% to 46%–51% and then to 58%–65%. Relative to ≥80-hour approvals:
- they increased 2.70-fold (1.90–3.82) after 2020 and a further 1.60-fold (1.15–2.21) after 2023;
- the ratio of <80-hour to ≥80-hour approvals changed little (1.25 and 0.90).

Mean processing time had fallen from 255 days in FY2011 to 216 days in FY2015–2017, after the 2011 criteria. It then rose to 255 days in FY2020, 261 days in FY2022 and 277–278 days in FY2023–2024 (Figure 2D), exceeding both the 8-month standard processing period (about 240 days) and the administrative target of 215 days.²⁵ Over the same period, annual decisions increased from 1,355 (FY2016) to 3,496 (FY2024).

In the exploratory industry analysis, the estimates for customer-facing relative to other industries after 2023 were imprecise and depended on the inference method: RR 1.24 for claims (wild bootstrap p = 0.033; permutation p = 0.086) and RR 1.33 for approvals (p = 0.18 and 0.20; Supplementary Table S3).

## 4 | DISCUSSION

### 4.1 | Principal findings

After Japan's 2021 revision of the criteria for overwork-related CCVD, no change in the level of total approvals was detected. The composition of approvals, however, shifted towards overtime below the karoshi line. Approvals with <80 hours per month rose 2.6-fold, and their ratio to long-hours approvals rose about 4-fold. In the 16-year series, this shift was robust to group-specific trends, alternative inference and exclusion of single years, and no comparable shift occurred at placebo dates. It was also seen when categories were defined by the threshold of each evaluation period, although that comparison rests on 4 years before and after the revision and was imprecise when category-specific trends were allowed. Short-term overload and extraordinary events, which the revision also clarified, increased as well. However, the rise in approvals below the thresholds was accompanied by a fall in approvals above the threshold in the 1-month period and in the adjacent 80–100-hour category in the 2–6-month period, and the number of approvals based on long-term overload did not increase. The shift is therefore better described as a change in the recorded overtime of compensated cases than as an addition of cases.

For mental disorders, the three revisions were associated with different components. The 2011 criteria were followed by a higher approval rate. The 2020 and 2023 revisions coincided with rising approvals, concentrated almost entirely in cases decided without examining working hours, and with rising claims and longer processing times. Because these changes coincided with other developments, we cannot attribute them to the criteria.

### 4.2 | Comparison with previous studies

Lin and colleagues found that the introduction of new CCVD criteria in Japan in 2001 and in Taiwan in 2010 was each followed by a more than 2.5-fold increase in compensated cases.¹³ Their outcome was the total. Japan's 2021 revision, by contrast, was not followed by a detectable change in the total, and our results show that totals can conceal a substantial change in the composition of compensated cases: in Japan, approvals with ≥80 hours fell by about 40% across the study period while below-threshold approvals rose. The Korean experience, in which approval rates more than tripled after changes to standards and procedures,¹⁴ similarly shows that recognition rules strongly shape compensated incidence, but it cannot separate the contributions of individual changes.

Durand-Moreau and colleagues found in this journal that presumptive coverage was associated with a higher proportion of PTSD claims, and that presumptions restricted to PTSD, unlike broader presumptions, were not associated with claims for other mental health conditions.¹⁸ In both settings, the change was concentrated in the category the rule addressed. Our evaluation-period analysis adds a caution: a category-specific increase can partly reflect movement between adjacent categories rather than additional compensated cases. In Australia, a reform that restricted eligibility in one state reduced claims by 15% relative to other jurisdictions, more so for time-loss claims than for medical-only claims.¹⁵ Lane and colleagues found that a system overhaul halted a previous decline in insurer decision time.¹⁶ We observed processing time for mental disorders lengthening as caseloads rose, even though the revisions were intended to speed decisions. Japanese studies of approved CCVD cases have documented long and irregular working patterns, such as consecutive work days and night work, that the 2021 revision listed as workload factors,²⁰ but they did not examine changes over time.

### 4.3 | Interpretation

Three explanations, not mutually exclusive, are consistent with the shift in CCVD approvals.

- **Wider eligibility.** Workers with overtime below the thresholds and other workload factors, who would previously have been rejected, were approved under the revised criteria. This is the intended effect.
- **Lower hours among workers who would previously have qualified.** Overtime caps introduced in April 2019 for large and April 2020 for small and medium-sized employers limit overtime, including statutory holiday work, to less than 100 hours in a single month and to an average of no more than 80 hours over 2–6 months, broadly corresponding to the thresholds of the criteria.²¹ From April 2019, employers were also required to record working hours by objective methods.³⁴ If the hours of workers who develop CCVD were compressed to just below the thresholds, some would have been rejected under the former criteria but approved under the revised ones. The revision would then have maintained, rather than extended, coverage. Because counts are by year of decision and decisions follow onset by about a year, effects of the caps would appear in approvals around FY2020–2022, coinciding with the revision. However, the caps applied to construction and vehicle driving only from April 2024, and drivers are subject to an annual limit of 960 hours rather than the monthly limits,³⁵ while road freight transport accounts for the largest share of CCVD approvals.²²
- **Changes in how hours were established.** Before the revision, investigators had an incentive to establish hours at or above a threshold to approve a case; afterwards, near-threshold cases could be approved on other grounds. Such a change would move cases from just above to just below a threshold without changing who was compensated.

Several observations bear on these explanations. The absolute number of approvals below 80 hours more than doubled, which a declining reference category cannot produce mechanically; allowing group-specific trends changed the estimate little (3.81); and in FY2009–2020 the share below 80 hours fluctuated between 4.8% and 10.6% without a sustained trend. In the 2–6-month period, however, the decline was concentrated in the adjacent 80–100-hour category, approvals with ≥100 hours were stable, and the period total remained similar. This pattern fits the second and third explanations at least as well as the first. Other contemporaneous changes, including the COVID-19 pandemic, which coincided with low numbers of decisions in FY2021–2022, may also have affected overtime categories differentially through changes in occupational composition, working patterns and the underlying incidence of disease. The aggregate data cannot establish which mechanism contributed most to the observed redistribution. Distinguishing the explanations requires approval rates by hour category, which would need the number of rejected claims by recorded overtime, or individual-level data.

The increase was not entirely abrupt. The below-threshold share was already 10.6% in FY2019 and reached 16.9% in the transition year FY2021. This may reflect the expert committee's deliberations from 2020, decisions on pending claims under the new criteria during FY2021, the overtime caps, or chance. Because counts are by year of decision, some approvals in FY2022 concern claims filed before the revision.

For mental disorders, the concentration of growth in approvals made without examining working hours is consistent with the revisions' focus on harassment, because a harassment event rated strong establishes work-relatedness on its own. The same pattern could arise if growing awareness after the 2020 harassment-prevention legislation increased claims for harassment independently of the criteria, if investigators increasingly used this pathway to manage rising caseloads, or if recordings and electronic messages made harassment easier to substantiate. Our data cannot separate these mechanisms. The increase in claims also began before the 2023 revision, so the step in claims attributed to 2023 is fragile, whereas the step in approvals is more robust. The stability of suicide approvals suggests that the growth occurred mainly among surviving workers.

The lengthening of processing time while the event-alone pathway expanded may seem paradoxical. Establishing the facts of interpersonal events requires interviews with the claimant, the alleged perpetrator, co-workers and the employer, which can take longer than reconstructing working hours from records. In addition, the pathway shortens only approvals: to reject a claim, which applies to about 70% of decisions, investigators must presumably confirm that neither workplace events nor working hours meet the criteria. Rising numbers of decisions would then lengthen processing time even if approvals became simpler.

### 4.4 | Implications

Japan's 2021 revision addresses a general issue with hour benchmarks: workers just below them may face other hazards, such as short rest intervals. The revision retained the established overtime benchmarks while explicitly clarifying that near-threshold overtime, together with other workload factors, could support recognition of work-relatedness. Jurisdictions that compensate multifactorial disease through occupation-specific presumptions, as in North America and Australia, or through hour thresholds, as in Korea and Taiwan, may face similar design choices.

Although aggregate statistics cannot isolate whether the shift reflects newly eligible workers, changes in recorded hours or changes in adjudication, the findings carry a general lesson. A clarification of recognition criteria that left the hour benchmarks unchanged coincided with a substantial movement of compensated cases across those benchmarks, while total approvals did not change detectably. Without category-specific indicators, such a change would have gone unnoticed.

For policymakers, our findings suggest that a criteria revision should be evaluated by its effect on the categories it addresses, and that these categories should be examined together with adjacent categories, not only total approvals or approval rates. These indicators should be monitored routinely:
- the distribution of approvals by overtime within each evaluation period;
- the share of approvals decided without examining hours;
- processing time.

Publishing the number of rejected claims by recorded overtime would allow approval rates by category to be calculated and would distinguish wider eligibility from changes in recorded hours. The rising processing times indicate that revisions that broaden eligibility require matching investigative capacity. For researchers, the within-category design can be applied wherever compensation statistics are cross-tabulated by the criterion under which cases were accepted. For occupational health practitioners, the revised criteria allow workers with substantial but sub-threshold overtime and other workload factors to be compensated, which underlines the importance of recording these factors, such as rest intervals, in workplace health records.

### 4.5 | Strengths and limitations

The strengths of this study are its use of complete national statistics over 17 years and its separation of claiming, throughput and adjudication. It also combines interrupted time series with within-category comparisons that are robust to alternative inference, and it examines each evaluation period separately. All data and code are publicly available.

It has several limitations.
- **Aggregate data:** we used published aggregate data and could not follow individual claims. Counts are by year of decision, so the approval rate is not a cohort measure, and some decisions in each year concern claims filed earlier.
- **Approved cases only by category:** hours are tabulated only for approved cases. Without rejected claims by recorded overtime, we cannot estimate approval rates by category, which limits the separation of wider eligibility from changes in recorded hours.
- **Recorded overtime:** the overtime categories record hours established in the investigation, which may be underestimated and may themselves be affected by a revision.
- **Concurrent events:** overtime caps, the mandate to record working hours, the COVID-19 pandemic and harassment-prevention legislation coincided with the revisions and may have affected categories differentially. We therefore report associations, not causal effects.
- **Analytic choices:** the evaluation-period analyses and alternative inference were added after internal review, and the analyses were not pre-registered. The evaluation-period analyses rest on 4 years before and after the revision and were imprecise when category-specific trends were allowed. Fiscal years are not exchangeable, so the ranking of the actual timing is descriptive.
- **Changes in data sources and short series:** the combined CCVD category tables came from different sources before and after FY2020, although sums matched in the overlapping years. Period-specific tables and mental disorder category tables begin only in FY2017, and follow-up after the 2021 and 2023 revisions was 4 and 2 years.
- **Few clusters:** the industry analysis rests on 7 industries, and its results depended on the inference method.
- **Compensated cases, not disease:** we studied compensated cases, not the incidence of disease.

### 4.6 | Conclusions

After Japan's 2021 revision of the recognition criteria for overwork-related CCVD, compensated cases shifted towards overtime below the karoshi line, while no change in total approvals was detected. Approvals above the thresholds, particularly in the adjacent 80–100-hour category of the 2–6-month period, declined as those below them rose, so aggregate statistics cannot show whether the revision extended compensation to newly eligible workers or maintained it for workers whose recorded hours fell. Recent revisions of the mental disorder criteria coincided with growth in approvals based on workplace events rather than hours, and with longer processing times. Evaluations of recognition criteria should examine the categories that the criteria address together with adjacent categories, and compensation statistics should report rejected claims by the same categories.

---

## DATA AVAILABILITY STATEMENT

All data analysed are publicly available government statistics. The transcribed aggregate data, analysis code and outputs are publicly available in an online repository; the link is withheld for anonymised review and is given on the Title Page. An anonymised copy is provided as Supporting Information.

---

## REFERENCES

1. Spieler EA, Burton JF Jr. The lack of correspondence between work-related disability and receipt of workers' compensation benefits. *Am J Ind Med.* 2012;55(6):487-505.
2. Azaroff LS, Levenstein C, Wegman DH. Occupational injury and illness surveillance: conceptual filters explain underreporting. *Am J Public Health.* 2002;92(9):1421-1429.
3. Kivimäki M, Jokela M, Nyberg ST, et al. Long working hours and risk of coronary heart disease and stroke: a systematic review and meta-analysis of published and unpublished data for 603,838 individuals. *Lancet.* 2015;386(10005):1739-1746.
4. Pega F, Náfrádi B, Momen NC, et al. Global, regional, and national burdens of ischemic heart disease and stroke attributable to exposure to long working hours for 194 countries, 2000–2016: a systematic analysis from the WHO/ILO Joint Estimates of the Work-related Burden of Disease and Injury. *Environ Int.* 2021;154:106595.
5. Park J, Kim Y, Cheng Y, Horie S. A comparison of the recognition of overwork-related cardiovascular disease in Japan, Korea, and Taiwan. *Ind Health.* 2012;50(1):17-23.
6. Yamauchi T, Yoshikawa T, Takamoto M, et al. Overwork-related disorders in Japan: recent trends and development of a national policy to promote preventive measures. *Ind Health.* 2017;55(3):293-302.
7. Takahashi M. Sociomedical problems of overwork-related deaths and disorders in Japan. *J Occup Health.* 2019;61(4):269-277.
8. Ministry of Health, Labour and Welfare. Report of the Expert Committee on Recognition Criteria for Cerebrovascular and Cardiovascular Diseases [in Japanese]. Tokyo: MHLW; 16 July 2021.
9. Ministry of Health, Labour and Welfare. Recognition criteria for cerebrovascular diseases and ischaemic heart diseases, etc. caused by work that markedly aggravates vascular lesions, etc. Notification Kihatsu 0914 No. 1, 14 September 2021 [in Japanese].
10. Ministry of Health, Labour and Welfare. Recognition criteria for mental disorders caused by psychological load. Notification Kihatsu 1226 No. 1, 26 December 2011 [in Japanese].
11. Ministry of Health, Labour and Welfare. Partial revision of the recognition criteria for mental disorders caused by psychological load. Notification Kihatsu 0529 No. 1, 29 May 2020 [in Japanese].
12. Ministry of Health, Labour and Welfare. Recognition criteria for mental disorders caused by psychological load. Notification Kihatsu 0901 No. 2, 1 September 2023 [in Japanese].
13. Lin RT, Lin CK, Christiani DC, et al. The impact of the introduction of new recognition criteria for overwork-related cardiovascular and cerebrovascular diseases: a cross-country comparison. *Sci Rep.* 2017;7:167. (Author correction: *Sci Rep.* 2018;8:4654.)
14. Kim UJ, Choi WJ, Kang SK, et al. Standards for recognition and approval rate of occupational cerebro-cardiovascular diseases in Korea. *Ann Occup Environ Med.* 2022;34:e30.
15. Collie A, Beck D, Gray SE, Lane TJ. Impact of legislative reform on benefit access and disability duration in workers' compensation: an interrupted time series study. *Occup Environ Med.* 2020;77(1):32-39.
16. Lane TJ, Di Donato MF, Collie A. Injured worker outcomes after compensation system overhaul: an interrupted time series study. *J Epidemiol Community Health.* 2023;77(8):515-520.
17. Rautiainen RH, Ledolter J, Sprince NL, et al. Effects of premium discount on workers' compensation claims in agriculture in Finland. *Am J Ind Med.* 2005;48(2):100-109.
18. Durand-Moreau Q, Descatha A, Adisesh A, Smith PM. Presumptive coverage policies and workers' compensation of post-traumatic stress disorder and other mental health conditions: a retrospective time-series study in Canada 2001–2019. *Am J Ind Med.* 2026. doi:10.1002/ajim.70132
19. Koyano F. Trends and commentary on revision of certification criteria for brain/heart disease and mental disorders [in Japanese]. *J Occup Health Law.* 2022;1(2):105-116. doi:10.57523/jaohl.1.2_105
20. Takami T. Analysis of consecutive work, night work and irregular work in approved workers' compensation cases of cerebrovascular and cardiovascular disease [in Japanese]. JILPT Research Material Series No. 297. Tokyo: Japan Institute for Labour Policy and Training; 2026.
21. Labour Standards Act (Act No. 49 of 1947), Article 36, as amended by Act No. 71 of 2018, in force 1 April 2019 (1 April 2020 for small and medium-sized enterprises) [in Japanese].
22. Ministry of Health, Labour and Welfare. Status of workers' compensation for karoshi and other overwork-related disorders, FY2009–FY2025 editions [in Japanese]. Tokyo: MHLW; 2010–2026.
23. Ministry of Health, Labour and Welfare. Materials of the 2nd meeting of the Expert Committee on Recognition Criteria for Cerebrovascular and Cardiovascular Diseases [in Japanese]. Tokyo: MHLW; 2020.
24. Ministry of Health, Labour and Welfare. Materials of the 1st meeting of the Expert Committee on Recognition Criteria for Mental Disorders [in Japanese]. Tokyo: MHLW; December 2021.
25. Ministry of Health, Labour and Welfare. Policy evaluation: pre-analysis sheets for policy objective III-3-1, FY2024 and FY2025 [in Japanese]. Tokyo: MHLW; 2024–2025.
26. Wagner AK, Soumerai SB, Zhang F, Ross-Degnan D. Segmented regression analysis of interrupted time series studies in medication use research. *J Clin Pharm Ther.* 2002;27(4):299-309.
27. Lopez Bernal J, Cummins S, Gasparrini A. Interrupted time series regression for the evaluation of public health interventions: a tutorial. *Int J Epidemiol.* 2017;46(1):348-355.
28. Lopez Bernal J, Cummins S, Gasparrini A. The use of controls in interrupted time series studies of public health interventions. *Int J Epidemiol.* 2018;47(6):2082-2093.
29. Newey WK, West KD. A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica.* 1987;55(3):703-708.
30. Kline P, Santos A. A score based approach to wild bootstrap inference. *J Econom Methods.* 2012;1(1):23-41.
31. Webb MD. Reworking wild bootstrap-based inference for clustered errors. *Can J Econ.* 2023;56(3):839-858.
32. von Elm E, Altman DG, Egger M, et al. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. *Lancet.* 2007;370(9596):1453-1457.
33. Benchimol EI, Smeeth L, Guttmann A, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. *PLoS Med.* 2015;12(10):e1001885.
34. Industrial Safety and Health Act (Act No. 57 of 1972), Article 66-8-3, as amended by Act No. 71 of 2018, in force 1 April 2019 [in Japanese].
35. Ministry of Health, Labour and Welfare. Hatarakikata Susume: work-style reform for construction, drivers and physicians [website, in Japanese]. https://hatarakikatasusume.mhlw.go.jp/ (accessed 9 November 2026).

---

## TABLES (each to be uploaded as a separate editable Word file)

### Table I. Claims, decisions and approvals before and after each revision, and level changes estimated by interrupted time series

| Disease / revision | Period | Claims | Decisions | Approvals | Approval rate, % | Claims RR (95% CI) | Approvals RR (95% CI) | Approval rate OR (95% CI) |
|---|---|---:|---:|---:|---:|---|---|---|
| **CCVD, Sep 2021** | Pre FY2009–2020 | 826.1 | 686.4 | 268.4 | 39.1 | | | |
| | Post FY2022–2025 | 1,027.5 | 692.8 | 217.0 | 31.3 | 1.13 (0.93–1.36) | 1.11 (0.93–1.33) | 1.17 (0.90–1.51) |
| **Mental, Dec 2011** | Pre FY2009–2011 | 1,196.3 | 995.7 | 289.0 | 29.0 | | | |
| | Post FY2012–2014 | 1,374.0 | 1,239.0 | 469.3 | 37.9 | 0.88 (0.74–1.06) | 1.50 (1.28–1.77) | 1.63 (1.34–1.99) |
| **Mental, May 2020** | Pre FY2017–2019 | 1,870.7 | 1,530.7 | 493.3 | 32.2 | | | |
| | Post FY2020–2022 | 2,360.0 | 1,948.3 | 649.0 | 33.3 | 0.99 (0.85–1.16) | 1.22 (1.06–1.40) | 1.12 (0.94–1.33) |
| **Mental, Sep 2023** | Pre FY2020–2022 | 2,360.0 | 1,948.3 | 649.0 | 33.3 | | | |
| | Post FY2024–2025 | 4,369.0 | 3,667.5 | 1,069.0 | 29.1 | 1.43 (1.26–1.63) | 1.54 (1.37–1.74) | 0.94 (0.81–1.08) |

*Notes:*
- Values are annual means; the approval rate is approvals divided by decisions.
- The level changes are post-revision step estimates from segmented regression with a linear trend: quasi-Poisson models for counts and quasi-binomial models weighted by decisions for the approval rate.
- CCVD: FY2009–2025, with FY2021 excluded as a transition year.
- Mental disorders: three revisions modelled jointly over FY2009–2025, with FY2023 excluded. The 2023 step in claims was 1.00 (0.85–1.18) when a change in slope from FY2020 was added (Supplementary Table S2).
- Abbreviations: CCVD, cerebro-cardiovascular disease; CI, confidence interval; FY, fiscal year (April–March); OR, odds ratio; RR, rate ratio.

### Table II. Within-category analysis of approvals for cerebro-cardiovascular disease, combined evaluation periods

| Analysis | Ratio change, FY2022–2025 vs pre-revision | 95% CI |
|---|---:|---|
| **Main: <80 h vs ≥80 h (year fixed effects; pre FY2009–2020)** | **4.27** | 3.28–5.57 |
| Group-specific linear trends | 3.81 | 2.22–6.53 |
| Standard errors clustered by year | 4.27 | 2.95–6.20 |
| Group-specific trends, standard errors clustered by year | 3.81 | 1.73–8.37 |
| Annual log ratio, OLS with trend, Newey–West (lag 1) | 3.88 | 2.33–6.48 |
| Pre-revision period FY2015–2020 | 4.54 | 3.11–6.63 |
| Excluding FY2013 | 4.51 | 3.51–5.79 |
| Excluding FY2020 | 4.36 | 3.32–5.73 |
| Excluding FY2022 | 4.01 | 3.01–5.34 |
| Target redefined as <100 h vs ≥100 h | 1.47 | 1.29–1.67 |
| In-time placebo windows, FY2012–2020 | 0.71–1.12 | — |
| Ranking of the actual timing among 1,820 assignments | largest | — |
| Short-term overload/extraordinary events vs ≥80 h | 2.38 | 1.46–3.89 |
| 80–100 h vs ≥100 h | 0.96 | 0.81–1.13 |
| Cardiac vs cerebrovascular disease | 0.98 | 0.86–1.11 |

| Approvals per year | FY2009–2020 | FY2022–2025 |
|---|---:|---:|
| ≥80 h/month | 230.9 | 141.0 |
| <80 h/month | 18.6 | 48.5 |
| Short-term overload/extraordinary events | 18.9 | 27.5 |

*Notes:*
- Overtime is the average monthly overtime in the evaluation period, combining the 1-month and 2–6-month tables. FY2021 was excluded.
- Ratio changes are exponentiated interaction coefficients from quasi-Poisson models with year fixed effects, unless stated otherwise.
- The ranking statistic is the difference in mean log ratio; the observed value corresponds to a 4.39-fold change. Fiscal years are not exchangeable, so the ranking is descriptive.
- The 80–100 h versus ≥100 h contrast is not a valid negative control because 1-month cases below the 1-month threshold fall in the 80–100 h band (Table III).

### Table III. Approvals for cerebro-cardiovascular disease by evaluation period and overtime, FY2017–2025

| FY | 1 month: ≥100 h | 1 month: <100 h | 2–6 months: ≥100 h | 2–6 months: 80–100 h | 2–6 months: <80 h | Short-term overload/ extraordinary events | Below either threshold, % |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2017 | 86 | 5 | 49 | 96 | 13 | 4 | 7.1 |
| 2018 | 97 | 3 | 23 | 85 | 15 | 15 | 7.6 |
| 2019 | 66 | 3 | 35 | 73 | 23 | 16 | 12.0 |
| 2020 | 54 | 4 | 28 | 75 | 17 | 16 | 10.8 |
| 2021 | 35 | 11 | 29 | 56 | 25 | 16 | 20.9 |
| 2022 | 41 | 19 | 28 | 34 | 46 | 26 | 33.5 |
| 2023 | 48 | 10 | 39 | 54 | 39 | 26 | 22.7 |
| 2024 | 40 | 28 | 47 | 63 | 36 | 27 | 26.6 |
| 2025 | 48 | 12 | 35 | 42 | 49 | 31 | 28.1 |
| Mean FY2017–2020 | 75.8 | 3.8 | 33.8 | 82.3 | 17.0 | 12.8 | |
| Mean FY2022–2025 | 44.3 | 17.3 | 37.3 | 48.3 | 42.5 | 27.5 | |

| Ratio change, FY2022–2025 vs FY2017–2020 (year fixed effects; FY2021 excluded) | Estimate (95% CI) |
|---|---|
| Below either threshold vs above | 4.26 (2.84–6.37) |
| 1 month: <100 h vs ≥100 h | 7.87 (3.32–18.65) |
| 2–6 months: <80 h vs ≥80 h | 3.39 (1.98–5.81) |
| 2–6 months: <80 h vs ≥100 h | 2.27 (1.32–3.89) |
| 2–6 months: 80–100 h vs ≥100 h | 0.53 (0.40–0.71) |
| Combined periods, same years: <80 h vs ≥80 h | 3.96 (2.60–6.02) |
| Combined periods, same years: 80–100 h vs ≥100 h | 0.93 (0.75–1.15) |

*Notes:*
- The thresholds are about 100 hours for the month before onset and an average of about 80 hours per month over 2–6 months. "Below either threshold" is 1 month <100 h plus 2–6 months <80 h, as a percentage of all approvals.
- Period-specific tables are published from FY2017. These analyses were added after internal review (post hoc). Sensitivity to category-specific trends and alternative inference is shown in Supplementary Table S5.

### Table IV. Approvals for mental disorders by monthly overtime category and processing time

| FY | Approvals | ≥80 h | <80 h | Without examining hours, n (%) | Mean days, claim to decision |
|---|---:|---:|---:|---:|---:|
| 2017 | 506 | 184 | 178 | 144 (28.5) | 216 |
| 2018 | 465 | 177 | 176 | 112 (24.1) | 219 |
| 2019 | 509 | 182 | 167 | 160 (31.4) | 240 |
| 2020 | 608 | 150 | 179 | 279 (45.9) | 255 |
| 2021 | 629 | 158 | 166 | 305 (48.5) | 251 |
| 2022 | 710 | 149 | 201 | 360 (50.7) | 261 |
| 2023 | 883 | 174 | 181 | 528 (59.8) | 278 |
| 2024 | 1,056 | 227 | 214 | 615 (58.2) | 277 |
| 2025 | 1,082 | 171 | 212 | 699 (64.6) | — |

| Ratio change (year fixed effects; FY2023 excluded) | After 2020 revision | Additional change after 2023 revision |
|---|---|---|
| Without examining hours vs ≥80 h | 2.70 (1.90–3.82) | 1.60 (1.15–2.21) |
| <80 h vs ≥80 h | 1.25 (1.02–1.52) | 0.90 (0.72–1.11) |

*Notes:*
- "Without examining hours" denotes cases judged work-related because the psychological load of a workplace event was rated strong on its own, without the need to investigate working hours (the event-alone pathway of the criteria).
- Processing time for FY2017–2020 is converted from months (×30); FY2021–2024 is reported in days.

---

## FIGURE LEGENDS

**Figure 1.** Approved claims for cerebro-cardiovascular disease by overtime category, Japan, FY2009–2025.
- (A) Approvals by average monthly overtime in the evaluation period, combining the 1-month and 2–6-month periods: ≥80 hours, <80 hours, and short-term overload or extraordinary events.
- (B) Share of approvals with <80 hours. Dotted lines show the means for FY2009–2020 and FY2022–2025.
- The dashed line marks the revision of September 2021. FY2021 was treated as a transition year.

**Figure 2.** Workers' compensation for mental disorders, Japan.
- (A) Claims, decisions and approvals, FY2009–2025.
- (B) Approval rate for all approvals and for suicides, including attempts.
- (C) Approvals by monthly overtime category, FY2017–2025. Labels give the percentage approved without examining working hours.
- (D) Mean days from claim to decision, FY2009–2024. The dotted line marks the 8-month standard processing period (about 240 days).
- Dashed lines mark the revisions of December 2011, May 2020 and September 2023.

**Figure 3.** Robustness of the change in the composition of approvals for cerebro-cardiovascular disease, and approvals by evaluation period.
- (A) Distribution of the change in the ratio of <80-hour to ≥80-hour approvals under all 1,820 assignments of 4 post-revision years among 16 non-transition years. The vertical line marks the actual timing. Because fiscal years are not exchangeable, the distribution is a descriptive ranking.
- (B) Approvals by evaluation period and overtime, FY2017–2025: solid lines, 2–6-month period (threshold about 80 hours per month); dashed lines, 1-month period (threshold about 100 hours).
- (C) Ratio changes after the revision from quasi-Poisson models with year fixed effects. Orange: categories addressed by the revision; blue: other contrasts. Contrasts marked * compare FY2022–2025 with FY2017–2020 using the period-specific tables; the others compare FY2022–2025 with FY2009–2020.

---

## SUPPLEMENTARY MATERIAL (Supporting Information for Review)

### Table S1. Content of the revisions

| Revision | Main content |
|---|---|
| CCVD, 14 Sep 2021 (applied from 15 Sep) | Hour thresholds kept (about 100 h in the month before onset, or about 80 h/month averaged over 2–6 months). Overtime approaching the thresholds plus other workload factors stated to establish work-relatedness. New workload factors: rest interval <~11 h, working without days off, physically demanding work, travel other than business trips; psychological load factors aligned with the mental disorder criteria. Short-term overload and extraordinary events clarified. Severe heart failure added. |
| Mental, 26 Dec 2011 | Criteria replaced the 1999 guidelines (revised 2009). Structured psychological load rating table with concrete examples; long hours (e.g., ≥160 h in the month before onset) rated strong on their own; review by a panel of specialists limited to difficult cases to shorten processing. |
| Mental, 29 May 2020 | "Power harassment" added as an event category and a specific event, following legislation requiring employers to prevent harassment (from June 2020 for large employers). |
| Mental, 1 Sep 2023 | Customer harassment added as an event; examples of harassment expanded; recognition of aggravation of pre-existing disorders broadened; medical opinion procedures simplified (cases requiring a panel of specialists further limited, so that more decisions can rest on the opinion of a single specialist). |

### Table S2. Sensitivity analyses of interrupted time series estimates

| Revision / model | Claims RR | Approvals RR | Approval rate OR |
|---|---|---|---|
| CCVD: main (FY2009–2025) | 1.13 (0.93–1.36) | 1.11 (0.93–1.33) | 1.17 (0.90–1.51) |
| CCVD: window FY2014–2025 | 0.97 (0.74–1.27) | 1.15 (0.92–1.44) | 1.59 (1.28–1.97) |
| CCVD: window FY2017–2025 | 0.86 (0.57–1.30) | 1.08 (0.75–1.56) | 1.96 (1.71–2.25) |
| CCVD: no trend (FY2009–2025) | 1.24 (1.11–1.39) | 0.81 (0.68–0.96) | 0.71 (0.55–0.91) |
| Mental 2023: main | 1.43 (1.26–1.63) | 1.54 (1.37–1.74) | 0.94 (0.81–1.08) |
| Mental 2023: FY2023 coded 0.5 | 1.42 (1.24–1.63) | 1.54 (1.37–1.73) | 0.93 (0.79–1.09) |
| Mental 2023: FY2023 coded post | 1.38 (1.22–1.55) | 1.44 (1.26–1.64) | 1.00 (0.86–1.17) |
| Mental 2023: window FY2016–2025 | 1.32 (1.09–1.60) | 1.35 (1.15–1.59) | 0.85 (0.68–1.06) |
| Mental 2023: slope change from FY2020 | 1.00 (0.85–1.18) | 1.32 (1.02–1.71) | 0.74 (0.55–1.00) |
| Mental 2023: OLS with Newey–West SE | 1.45 (1.26–1.67) | 1.54 (1.42–1.66) | 0.94 (0.83–1.06) |
| Mental: placebo steps FY2014–2019 | 0.94–1.07 | 0.90–1.04 | 0.84–1.07 |

### Table S3. Customer-facing vs other industries after the 2023 revision (exploratory)

| Outcome | RR | Cluster-robust CI (t₆) | Wild cluster score bootstrap p (95% CI) | Permutation, one-sided p (35 assignments) |
|---|---|---|---|---|
| Approvals | 1.33 | 0.83–2.11 | 0.178 (0.83–2.28) | 0.200 |
| Claims | 1.24 | 0.98–1.57 | 0.033 (1.04–1.56) | 0.086 |

*Notes:* FY2016–2022 vs FY2024–2025 (FY2023 excluded). Customer-facing industries: wholesale and retail; accommodation and food services; medical, health care and welfare; education. Comparison industries: manufacturing; information and communications; finance and insurance. Offset: employed persons (Labour Force Survey). With 7 clusters, the two inference methods disagree for claims; neither result should be regarded as evidence of an industry difference.

### Table S5. Sensitivity of the evaluation-period contrast (below either threshold vs above), FY2022–2025 vs FY2017–2020

| Model | Ratio change | 95% CI |
|---|---:|---|
| Quasi-Poisson, year fixed effects (Table III) | 4.26 | 2.84–6.37 |
| Standard errors clustered by year | 4.26 | 2.40–7.55 |
| Group-specific linear trends | 3.60 | 1.25–10.35 |
| Group-specific trends, standard errors clustered by year | 3.60 | 0.50–25.87 |
| Annual log ratio, OLS with linear trend, Newey–West (lag 1) | 2.88 | 1.31–6.32 |

*Notes:* 8 fiscal years (FY2021 excluded). With 8 clusters, the clustered intervals rely on a normal approximation and are themselves imprecise. Post hoc analyses.

### Table S4. Data sources by series and fiscal year
Provided as a separate Supporting Information file (the data dictionary of the public repository): source document, table number and fiscal years for every series.

### STROBE/RECORD checklist
Provided as a separate Supporting Information file.
