# Manuscript for American Journal of Industrial Medicine — v1 (anonymised main document)

> Article type: Research Article. Main document anonymised for peer review; author information is in the separate Title Page. Tables are to be uploaded as separate editable files; figures as separate files.

---

## Title

Revising recognition criteria for overwork-related disease changed who was compensated, not how many: an interrupted time series and within-category analysis of national workers' compensation data in Japan, 2009–2025

**Running title:** Recognition criteria revisions and compensated overwork-related disease

---

## Abstract (248 words)

**Background:** Recognition criteria determine which workers are compensated for overwork-related disease, yet revisions are rarely evaluated. In 2021, Japan revised its criteria for cerebro-cardiovascular disease (CCVD) to allow recognition when overtime approached, but did not reach, the "karoshi line" and other workload factors were present. Mental disorder criteria were revised in 2011, 2020 and 2023.

**Methods:** Using national compensation statistics (fiscal years 2009–2025), we decomposed approvals into claims, decisions and approval rates and fitted interrupted time series models. For CCVD, we compared approvals with <80 versus ≥80 overtime hours per month (target versus reference) in year-fixed-effects Poisson models, with permutation tests, placebo years and a non-targeted contrast (80–100 versus ≥100 hours). For mental disorders, we examined approvals made without examining working hours.

**Results:** The level of CCVD approvals did not change after 2021 (rate ratio [RR] 1.11, 95% CI 0.93–1.33). Approvals with <80 hours rose from 18.6 to 48.5 per year, and their ratio to ≥80-hour approvals increased 4.27-fold (3.28–5.57; permutation p = 0.0005), whereas a non-targeted contrast did not (0.96, 0.81–1.13). For mental disorders, approval rates rose after 2011 (odds ratio 1.63, 1.34–1.99). After 2023, claims (RR 1.43, 1.26–1.63) and approvals (RR 1.54, 1.37–1.74) increased with unchanged approval rates. Approvals made without examining hours rose from 139 to 657 per year, while hours-based approvals were stable; mean processing time lengthened from 216 to 277 days.

**Conclusions:** Japan's 2021 revision changed which workers were compensated without changing how many. Evaluations of recognition criteria should examine the categories they target, not only totals.

**Keywords:** workers' compensation; occupational disease; karoshi; long working hours; mental disorders; harassment; interrupted time series; Japan

---

## 1 | INTRODUCTION

Workers' compensation systems translate evidence on work-related disease into eligibility rules. Where those rules are narrow, many workers whose disease or disability was caused by work receive no compensation,¹ and each step from illness to an accepted claim filters out cases.² For diseases with multifactorial causes, such as cerebro-cardiovascular disease (CCVD) and mental disorders, recognition criteria are the decisive filter: they specify which exposures, and at what level, establish work-relatedness. Long working hours are an established cause of coronary heart disease and stroke,³,⁴ and Japan, the Republic of Korea and Taiwan have each adopted explicit criteria for compensating overwork-related CCVD.⁵

Japan introduced the first such criteria, in 1961. Since 2001, CCVD has been regarded as strongly work-related when overtime reached about 100 hours in the month before onset or averaged about 80 hours per month over 2–6 months, thresholds widely known as the "karoshi line".⁶,⁷ In September 2021, after a review by an expert committee, the Ministry of Health, Labour and Welfare (MHLW) revised these criteria for the first time in 20 years.⁸,⁹ The revision kept the hour thresholds but stated explicitly that overtime approaching them, combined with other workload factors, could establish work-relatedness. It also added new workload factors, such as short rest intervals between shifts and physically demanding work, clarified the criteria for short-term overload and extraordinary events, and added severe heart failure as a compensable disease.⁹ Criteria for mental disorders were codified in 2011, replacing earlier guidelines,¹⁰ and revised in 2020 to add power harassment¹¹ and in 2023 to add customer harassment and other events.¹² Each revision was intended to make compensation easier to claim and faster to decide.

Whether such revisions work as intended is rarely examined. Lin and colleagues compared rates of compensated overwork-related CCVD in the 5 years before and after new criteria were introduced in Japan (2001) and Taiwan (2010), reporting a 2.58-fold increase in Taiwan.¹³ In Korea, approval rates for occupational CCVD fell from 44.7% in 2006 to 12.9% in 2011 and rose to 41.3% by 2018 after successive changes to standards and procedures, but these changes were described rather than modelled.¹⁴ Outside East Asia, interrupted time series studies have evaluated reforms of Australian compensation systems,¹⁵,¹⁶ premium incentives in Finland¹⁷ and, most recently in this journal, presumptive coverage for post-traumatic stress disorder in Canada, which increased PTSD claims without spillover to other mental health conditions.¹⁸ We found no evaluation of Japan's 2020, 2021 or 2023 revisions.

These studies share a limitation that matters for criteria revisions in particular: they evaluate total counts. Revisions usually target a defined category of cases, here workers with overtime below the karoshi line, while other forces act on the rest of the caseload. Between 2019 and 2024, for example, Japan introduced statutory caps on overtime,¹⁹ which might be expected to reduce the number of workers with very long hours. If a revision added cases in its target category while long-hours cases declined for other reasons, totals could remain unchanged even though the revision worked as intended. Conversely, an increase in totals could reflect claiming behaviour rather than any change in adjudication.

We therefore evaluated the CCVD and mental disorder revisions using three complementary approaches with national data for fiscal years 2009–2025: (1) a decomposition of approvals into claims, decisions and approval rates, analysed with interrupted time series; (2) a within-category comparison contrasting the category targeted by the 2021 revision with untargeted categories decided in the same year; and (3) for mental disorders, an analysis of the composition of approvals and of processing time. We hypothesised that, if the 2021 revision operated as intended, approvals in the targeted category (<80 overtime hours per month) would increase relative to approvals with ≥80 hours, whereas a contrast between categories that the revision did not address (80–100 vs ≥100 hours) would not change.

## 2 | METHODS

### 2.1 | Setting

Japan's Industrial Accident Compensation Insurance covers employees of almost all private employers. Claims for overwork-related disease are filed with local Labour Standards Inspection Offices, which investigate working hours and workplace events and decide whether the disease is work-related. They apply recognition criteria issued as notifications by the MHLW. Approved claimants receive medical care and wage-replacement benefits; survivors receive benefits after death.

The 2021 CCVD revision (notification of 14 September 2021, applied from 15 September 2021) had four elements.⁹ First, cases with overtime approaching but not reaching the karoshi line could be recognised when other workload factors were present. Second, the list of other workload factors was revised; rest intervals of less than about 11 hours between shifts and physically demanding work were added. Third, the conditions under which short-term overload and extraordinary events establish work-relatedness were clarified. Fourth, severe heart failure was added to the compensable diseases. The mental disorder criteria are summarised in Supplementary Table S1:
- **2011:** introduced a structured table for rating psychological load and streamlined expert review.¹⁰
- **2020:** added power harassment as an event category, following legislation requiring employers to prevent harassment.¹¹
- **2023:** added customer harassment and other events, broadened the recognition of aggravated pre-existing disorders, and simplified the collection of medical opinions.¹²

### 2.2 | Data

We used the MHLW's annual reports on compensation for overwork-related disorders (*karoshi-tō no rōsai hoshō jōkyō*). Each report is published in June for the preceding fiscal year (April to March).²⁰ The reports give national numbers of claims, decisions and approvals for CCVD and mental disorders, including deaths and suicides. They also cross-tabulate approvals by the overtime recorded in the investigation, by disease type and by industry.

- **CCVD decisions:** decisions for FY2009–2012 were taken from a regional labour bureau's republication of the national tables.
- **Overtime categories for CCVD approvals:** approvals are classified by average monthly overtime in the evaluation period (<45, 45–60, 60–80, 80–100, 100–120, 120–140, 140–160 and ≥160 hours). A separate category covers short-term overload and extraordinary events.
  - FY2009–2019: tables combining the 1-month and 2–6-month evaluation periods, published by the expert committee.²¹
  - FY2020 onwards: we summed the period-specific tables in the annual reports.
- **Mental disorders:** approvals are classified by monthly overtime in the same bands, plus a category for cases judged work-related "without the need to examine working hours". In these cases the psychological load of a workplace event, typically harassment or violence, was rated strong on its own. These tables are available for FY2017–2025.
- **Processing time:** mean time from claim to decision for mental disorders.
  - FY2009–2020: reported in months by an expert committee;²² we converted to days by multiplying by 30, as in the source.
  - FY2021–2024: reported in days in the MHLW's policy evaluation documents.²³

All values were transcribed from the source documents and checked in three ways: across overlapping editions, by confirming that category tables summed to annual totals, and against the narrative text of the reports. Claims are counted by fiscal year of filing, and decisions and approvals by fiscal year of decision; none of the series is counted by year of onset.

### 2.3 | Outcomes

The outcomes were annual numbers of claims, decisions and approvals, and the approval rate (approvals divided by decisions). Approvals per claim equal the product of the decision ratio and the approval rate, so a change in approvals can be attributed to claiming, throughput or adjudication.

### 2.4 | Statistical analysis

**Interrupted time series.** We modelled annual counts with log-linear quasi-Poisson regression and the approval rate with logistic quasi-binomial regression weighted by decisions.²⁴⁻²⁶ Each model included a linear secular trend and a step indicator for the post-revision period. Dispersion was estimated from the Pearson χ² statistic.

- **CCVD:** the post-revision period was FY2022–2025. FY2021, during which the revision took effect, was excluded as a transition year.
- **Mental disorders:** all three revisions were modelled jointly over FY2009–2025, with steps from FY2012, FY2020 and FY2024. FY2023 was excluded as a transition year. FY2011, in which the criteria were issued in December, was treated as pre-revision.

Sensitivity analyses varied the analytic window and omitted the trend. For the 2023 revision, they also coded FY2023 as half-exposed or post-revision, added a change in slope from FY2020, refitted the models as ordinary least squares with Newey–West standard errors, and placed placebo steps in FY2014–2019.

**Within-category analysis (CCVD).** We modelled approvals in category *g* and year *t* as log E[*Y*ₜ_g] = α_t + γ_g + δ·(target_g × post_t), with quasi-Poisson errors. The year fixed effects α_t absorb any influence common to all categories in a year, such as the total number of claims, administrative capacity, the COVID-19 pandemic or general shifts in claiming. The exponentiated δ estimates the change in the ratio of targeted to reference approvals, comparing FY2022–2025 with FY2009–2020.

- **Main contrast:** <80 hours versus ≥80 hours per month.
- **Robustness checks:**
  - Exact permutation test: the observed difference in the mean log-ratio was compared with all 1,820 ways of choosing 4 "post-revision" years from the 16 non-transition years.
  - In-time placebo tests: pseudo-revisions defining 4-year windows wholly within the pre-revision period.
  - Group-specific linear trends.
  - Exclusion of single years (FY2013, an outlier; FY2020, the first pandemic year; FY2022, the first post-revision year).
  - Restriction of the pre-revision period to FY2015–2020.
  - Redefinition of the target as <100 hours.
- **Specificity check:** we contrasted two categories the revision did not target, 80–100 versus ≥100 hours. Before the revision, 95%–97% of approvals in the 80–100-hour band met the 2–6-month criterion (69%–90% afterwards). Any inflow of targeted 1-month cases into this band would bias the contrast towards showing a change.
- **Elements targeted by the other parts of the revision:**
  - short-term overload and extraordinary events versus ≥80 hours;
  - ischaemic heart disease and other cardiac conditions versus cerebrovascular disease (severe heart failure was added).

**Composition of mental disorder approvals.** For FY2017–2025, we used the same fixed-effects model to estimate changes in the ratio of approvals made without examining working hours to approvals with ≥80 hours, with steps at FY2020 and FY2024 (FY2023 excluded). Processing time was analysed descriptively.

**Supplementary analysis.** The 2023 revision added customer harassment. We therefore compared approvals and claims in four customer-facing industries (wholesale and retail; accommodation and food services; medical, health care and welfare; education) with three other industries (manufacturing; information and communications; finance and insurance). The model was a difference-in-differences Poisson model with employment from the Labour Force Survey as an offset. Inference used a wild cluster score bootstrap with Webb weights²⁷,²⁸ and permutation of industry labels (35 assignments).

Analyses used Python 3 (pandas, statsmodels). Reporting follows the STROBE and RECORD statements.²⁹,³⁰

### 2.5 | Ethics

The study used only publicly available aggregate statistics containing no information on identifiable individuals and therefore did not require ethical review.

## 3 | RESULTS

### 3.1 | Cerebro-cardiovascular disease: totals

From FY2009–2020 to FY2022–2025:
- mean annual claims rose from 826 to 1,028;
- decisions were stable (686 to 693);
- approvals fell from 268 to 217 (Table 1).

The crude approval rate fell from 39.1% to 31.3%, continuing a decline that began in FY2013 (Table 1). After accounting for the secular trends, the revision was not followed by a clear change in the level of claims (RR 1.13, 95% CI 0.93–1.36), approvals (RR 1.11, 0.93–1.33) or the approval rate (OR 1.17, 0.90–1.51). The approval rate estimate depended on the analytic window (Supplementary Table S2). Shorter pre-revision windows produced increases (OR 1.59–1.96) and a simple before–after comparison produced a decrease (OR 0.71). We therefore regard the effect on the overall approval rate as indeterminate.

### 3.2 | Cerebro-cardiovascular disease: composition

The composition of approvals changed markedly (Figure 1; Table 2).

| Approvals per year | FY2009–2020 | FY2022–2025 |
|---|---:|---:|
| <80 overtime hours/month | 18.6 | 48.5 |
| ≥80 overtime hours/month | 230.9 | 141.0 |
| Short-term overload and extraordinary events | 18.9 | 27.5 |

- The share of approvals with <80 hours averaged 7.0% before the revision and 22.5% afterwards.
- The ratio of <80-hour to ≥80-hour approvals increased 4.27-fold (95% CI 3.28–5.57) relative to the pre-revision period.
- The ratio increased 3.81-fold (2.22–6.53) when group-specific trends were allowed.
- Using the period-specific tables, approvals below either threshold (<100 hours in the 1-month table or <80 hours in the 2–6-month table) were 7.1%–12.0% of approvals in FY2017–2020, 20.9% in FY2021 and 22.7%–33.5% in FY2022–2025.

### 3.3 | Robustness and specificity

- **Permutation test:** the observed change (4.39-fold on the unweighted log-ratio scale) was the largest of all 1,820 possible assignments of post-revision years (p = 0.0005; Figure 3A).
- **In-time placebo tests:** placebo windows in the pre-revision period produced ratio changes of 0.71–1.12.
- **Excluding single years or restricting the pre-revision period:** estimates ranged from 4.01 to 4.54 (Table 2).
- **Non-targeted contrast:** 80–100 versus ≥100 hours did not change (0.96, 0.81–1.13; Figure 3B).
- **Short-term overload and extraordinary events:** approvals increased relative to ≥80-hour approvals (2.38, 1.46–3.89).
- **Disease type:** the ratio of cardiac to cerebrovascular approvals did not change (0.98, 0.86–1.11), consistent with the small number of approvals for severe heart failure (4 in FY2021 and 2 in FY2022).

### 3.4 | Mental disorders: totals

Claims rose from 1,136 in FY2009 to 4,958 in FY2025, and approvals from 234 to 1,082 (Figure 2A). The three revisions were associated with different components (Table 1).

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

### 3.5 | Mental disorders: composition and processing time

Approvals with ≥80 and <80 overtime hours each remained between about 150 and 230 per year from FY2017 to FY2025 (Figure 2C; Table 3). Approvals made without examining working hours rose from 139 per year in FY2017–2019 to 315 in FY2020–2022 and 657 in FY2024–2025. Their share of all approvals therefore rose from 24%–31% to 46%–51% and then to 58%–65%. Relative to ≥80-hour approvals:
- they increased 2.70-fold (1.90–3.82) after 2020 and a further 1.60-fold (1.15–2.21) after 2023;
- the ratio of <80-hour to ≥80-hour approvals changed little (1.25 and 0.90).

Mean processing time had fallen from 255 days in FY2011 to 216 days in FY2015–2017, after the 2011 criteria. It then rose to 255 days in FY2020, 261 days in FY2022 and 277–278 days in FY2023–2024, exceeding the 240-day standard (Figure 2D). Over the same period, annual decisions increased from 1,355 (FY2016) to 3,496 (FY2024).

In the supplementary industry analysis, claims increased more in customer-facing industries after 2023 (RR 1.24; wild bootstrap p = 0.033). For approvals the estimate was similar but imprecise (RR 1.33; p = 0.18; Supplementary Table S3).

## 4 | DISCUSSION

### 4.1 | Principal findings

Japan's 2021 revision of the criteria for overwork-related CCVD was not followed by more approvals overall. It was, however, followed by a 2.6-fold increase in approvals with overtime below 80 hours per month, the category the revision addressed. Their ratio to long-hours approvals rose more than 4-fold. Four features make it unlikely that this shift reflects chance or general trends:
- the change was the largest of all possible timings;
- placebo revisions produced no comparable change;
- a contrast between untargeted categories did not move;
- a second category clarified by the revision, short-term overload and extraordinary events, also increased.

For mental disorders, the three revisions acted on different components. The 2011 criteria raised the approval rate. The 2020 and 2023 revisions coincided with rising approvals, concentrated almost entirely in cases decided without examining working hours, and with rising claims and longer processing times.

### 4.2 | Comparison with previous studies

Lin and colleagues found that introducing new CCVD criteria in Taiwan in 2010 was associated with a 2.58-fold increase in compensated cases.¹³ Their outcome was the total. Our results show why totals can understate the effect of a revision. In Japan, approvals with ≥80 hours fell by about 40% across the study period, and the added below-threshold approvals roughly offset that fall. The Korean experience, in which approval rates more than tripled after changes to standards and procedures,¹⁴ similarly shows that recognition rules strongly shape compensated incidence. It cannot separate the contributions of individual changes.

Our within-category design parallels the finding of Durand-Moreau and colleagues in this journal: presumptive coverage restricted to PTSD increased PTSD claims without affecting other mental health conditions.¹⁸ In both settings, the effect of a rule change was confined to the category the rule addressed. An Australian reform that restricted eligibility reduced claims by 15%, more so for time-loss claims than for medical-only claims.¹⁵ Our results show the converse: an expansion confined to a defined group. Lane and colleagues found that a system overhaul halted a previous decline in insurer decision time.¹⁶ We observed processing time for mental disorders lengthening as caseloads rose, even though the revisions were explicitly intended to speed decisions.

### 4.3 | Interpretation

The year fixed effects in our within-category models absorb influences that act on all categories alike. They do not absorb influences that act differentially on long-hours cases. The decline in ≥80-hour approvals began before 2021 and probably reflects falling long working hours, including the overtime caps introduced in 2019–2020.¹⁹ A decline confined to the reference category would raise the ratio even without any revision. Three observations argue against this as the main explanation:
- allowing group-specific trends changed the estimate little (3.81);
- the absolute number of below-threshold approvals more than doubled, which a falling denominator cannot produce;
- in FY2009–2020, the share below 80 hours fluctuated between 4.8% and 10.6% without a sustained trend.

The increase was not entirely abrupt. The below-threshold share was already 10.6% in FY2019 and reached 16.9% in the transition year FY2021. This may reflect the expert committee's deliberations from 2020, decisions on pending claims under the new criteria during FY2021, or chance. Because counts are by year of decision, some approvals in FY2022 concern claims filed before the revision.

For mental disorders, the concentration of growth in approvals made without examining working hours is consistent with the revisions' focus on harassment. Under the criteria, a harassment event rated as strong establishes work-relatedness without investigation of hours. However, the same pattern would arise if investigators increasingly used this pathway to manage rising caseloads, or if growing awareness after the 2020 harassment-prevention legislation increased claims for harassment independently of the criteria. Our data cannot separate these mechanisms. The increase in claims also began before the 2023 revision. The step in claims attributed to 2023 is therefore fragile, whereas the step in approvals is more robust. The stability of suicide approvals suggests that the growth occurred mainly among surviving workers.

### 4.4 | Implications

For policymakers, our findings suggest that the success of a criteria revision should be judged by its effect on the categories it addresses, not only by total approvals or approval rates. These indicators should be monitored routinely:
- the share of approvals below the hour thresholds;
- the share of approvals decided without examining hours;
- processing time.

The rising processing times indicate that revisions that broaden eligibility require matching investigative capacity. For researchers, the within-category design offers a transferable approach wherever compensation statistics are cross-tabulated by the criterion under which cases were accepted. Examples include the hour-based criteria in Korea and Taiwan and presumptive coverage in North America and Australia. For occupational health practitioners, the revision means that workers with substantial but sub-threshold overtime and other workload factors, such as short rest intervals, are now more likely to be compensated. This underlines the importance of recording these factors in workplace health records.

### 4.5 | Strengths and limitations

The strengths of this study are its use of complete national statistics over 17 years and its separation of claiming, throughput and adjudication. It also combines interrupted time series with within-category comparisons, permutation inference and a specificity contrast. The analyses were not pre-registered.

It has several limitations.
- **Aggregate data:** we used published aggregate data and could not follow individual claims. Counts are by year of decision, so the approval rate is not a cohort measure, and some decisions in each year concern claims filed earlier.
- **Recorded overtime:** the overtime categories record hours established in the investigation, which may be underestimated. A revision could also change how hours are recorded.
- **Changes in data sources:** the CCVD category tables came from different sources before and after FY2020, although totals matched in overlapping years. Mental disorder category tables begin only in FY2017.
- **Concurrent events:** overtime caps, the COVID-19 pandemic, which coincided with low numbers of decisions in FY2021–2022, and harassment-prevention legislation may have affected categories differentially.
- **Short follow-up:** follow-up after the 2021 and 2023 revisions was 4 and 2 years.
- **Few clusters:** the industry analysis rests on 7 industries and should be regarded as exploratory.
- **Approved cases only:** we studied compensated cases, not the incidence of disease. An increase in compensated below-threshold cases indicates wider coverage, not more disease.

### 4.6 | Conclusions

Japan's 2021 revision of the recognition criteria for overwork-related CCVD substantially increased compensation for workers whose overtime fell below the karoshi line, while total approvals remained unchanged. Recent revisions of the mental disorder criteria coincided with growth in approvals based on workplace events rather than hours, and with longer processing times. Evaluations of recognition criteria should examine the categories that the criteria target.

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
19. [Author]. Statutory overtime caps and compensated mental disorders in Japan: two natural experiments in 10 years of national data, 2016–2025 [preprint]. medRxiv. 2026. [details withheld for anonymised review]
20. Ministry of Health, Labour and Welfare. Status of workers' compensation for karoshi and other overwork-related disorders, FY2009–FY2025 editions [in Japanese]. Tokyo: MHLW; 2010–2026.
21. Ministry of Health, Labour and Welfare. Materials of the 2nd meeting of the Expert Committee on Recognition Criteria for Cerebrovascular and Cardiovascular Diseases [in Japanese]. Tokyo: MHLW; 2020.
22. Ministry of Health, Labour and Welfare. Materials of the 1st meeting of the Expert Committee on Recognition Criteria for Mental Disorders [in Japanese]. Tokyo: MHLW; December 2021.
23. Ministry of Health, Labour and Welfare. Policy evaluation: pre-analysis sheets for policy objective III-3-1, FY2024 and FY2025 [in Japanese]. Tokyo: MHLW; 2024–2025.
24. Wagner AK, Soumerai SB, Zhang F, Ross-Degnan D. Segmented regression analysis of interrupted time series studies in medication use research. *J Clin Pharm Ther.* 2002;27(4):299-309.
25. Bernal JL, Cummins S, Gasparrini A. Interrupted time series regression for the evaluation of public health interventions: a tutorial. *Int J Epidemiol.* 2017;46(1):348-355.
26. Lopez Bernal J, Cummins S, Gasparrini A. The use of controls in interrupted time series studies of public health interventions. *Int J Epidemiol.* 2018;47(6):2082-2093.
27. Kline P, Santos A. A score based approach to wild bootstrap inference. *J Econom Methods.* 2012;1(1):23-41.
28. Webb MD. Reworking wild bootstrap-based inference for clustered errors. *Can J Econ.* 2023;56(3):839-858.
29. von Elm E, Altman DG, Egger M, et al. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. *Lancet.* 2007;370(9596):1453-1457.
30. Benchimol EI, Smeeth L, Guttmann A, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. *PLoS Med.* 2015;12(10):e1001885.

---

## TABLES (each to be uploaded as a separate editable file)

### Table 1. Claims, decisions and approvals before and after each revision, and level changes estimated by interrupted time series

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
- Mental disorders: three revisions modelled jointly over FY2009–2025, with FY2023 excluded.
- Abbreviations: CCVD, cerebro-cardiovascular disease; CI, confidence interval; FY, fiscal year (April–March); OR, odds ratio; RR, rate ratio.

### Table 2. Within-category analysis of approvals for cerebro-cardiovascular disease

| Analysis | Ratio change, FY2022–2025 vs pre-revision | 95% CI or p |
|---|---:|---|
| **Main: <80 h vs ≥80 h (year fixed effects; pre FY2009–2020)** | **4.27** | 3.28–5.57 |
| Group-specific linear trends | 3.81 | 2.22–6.53 |
| Pre-revision period FY2015–2020 | 4.54 | 3.11–6.63 |
| Excluding FY2013 | 4.51 | 3.51–5.79 |
| Excluding FY2020 | 4.36 | 3.32–5.73 |
| Excluding FY2022 | 4.01 | 3.01–5.34 |
| Target redefined as <100 h vs ≥100 h | 1.47 | 1.29–1.67 |
| Exact permutation test (1,820 assignments) | largest of all | p = 0.0005 |
| In-time placebo windows, FY2012–2020 | 0.71–1.12 | — |
| **Specificity: 80–100 h vs ≥100 h (not targeted)** | **0.96** | 0.81–1.13 |
| Short-term overload/extraordinary events vs ≥80 h | 2.38 | 1.46–3.89 |
| Cardiac vs cerebrovascular disease | 0.98 | 0.86–1.11 |

| Approvals per year | FY2009–2020 | FY2022–2025 |
|---|---:|---:|
| ≥80 h/month | 230.9 | 141.0 |
| <80 h/month | 18.6 | 48.5 |
| Short-term overload/extraordinary events | 18.9 | 27.5 |

*Notes:*
- Overtime is the average monthly overtime in the evaluation period, combining the 1-month and 2–6-month tables. FY2021 was excluded.
- Ratio changes are exponentiated interaction coefficients from quasi-Poisson models with year fixed effects.
- The permutation statistic is the difference in mean log-ratio. The observed value corresponds to a 4.39-fold change.

### Table 3. Approvals for mental disorders by monthly overtime category and processing time

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
- "Without examining hours" denotes cases judged work-related because the psychological load of a workplace event was rated strong without the need to investigate working hours.
- Processing time for FY2017–2020 is converted from months (×30); FY2021–2024 is reported in days.

---

## FIGURE LEGENDS

**Figure 1.** Approved claims for cerebro-cardiovascular disease by overtime category, Japan, FY2009–2025.
- (A) Approvals by average monthly overtime in the evaluation period: ≥80 hours, <80 hours (the category targeted by the 2021 revision), and short-term overload or extraordinary events.
- (B) Share of approvals with <80 hours. Dotted lines show the means for FY2009–2020 and FY2022–2025.
- The dashed line marks the revision of September 2021. FY2021 was treated as a transition year.

**Figure 2.** Workers' compensation for mental disorders, Japan.
- (A) Claims, decisions and approvals, FY2009–2025.
- (B) Approval rate for all approvals and for suicides, including attempts.
- (C) Approvals by monthly overtime category, FY2017–2025. Labels give the percentage approved without examining working hours.
- (D) Mean days from claim to decision, FY2009–2024. The dotted line marks the 240-day standard processing period.
- Dashed lines mark the revisions of December 2011, May 2020 and September 2023.

**Figure 3.** Robustness and specificity of the change in the composition of approvals for cerebro-cardiovascular disease.
- (A) Distribution of the change in the ratio of <80-hour to ≥80-hour approvals under all 1,820 assignments of 4 post-revision years among 16 non-transition years. The vertical line marks the actual revision.
- (B) Ratio changes (FY2022–2025 vs FY2009–2020) from quasi-Poisson models with year fixed effects.
  - Orange: categories addressed by the revision.
  - Blue: contrasts not targeted by the revision.

---

## SUPPLEMENTARY MATERIAL (Supporting Information for Review)

### Table S1. Content of the revisions

| Revision | Main content |
|---|---|
| CCVD, 14 Sep 2021 (applied from 15 Sep) | Hour thresholds kept (about 100 h in the month before onset, or about 80 h/month averaged over 2–6 months). Overtime approaching the thresholds plus other workload factors stated to establish work-relatedness. New workload factors: rest interval <~11 h, working without days off, physically demanding work, travel other than business trips; psychological load factors aligned with the mental disorder criteria. Short-term overload and extraordinary events clarified. Severe heart failure added. |
| Mental, 26 Dec 2011 | Criteria replaced the 1999 guidelines (revised 2009). Structured psychological load rating table with concrete examples; long hours (e.g., ≥160 h in the month before onset) rated strong on their own; expert panel review limited to difficult cases to shorten processing. |
| Mental, 29 May 2020 | "Power harassment" added as an event category and a specific event, following legislation requiring employers to prevent harassment (from June 2020 for large employers). |
| Mental, 1 Sep 2023 | Customer harassment added as an event; examples of harassment expanded; recognition of aggravation of pre-existing disorders broadened; medical opinion procedures simplified. |

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

*Notes:* FY2016–2022 vs FY2024–2025 (FY2023 excluded). Customer-facing industries: wholesale and retail; accommodation and food services; medical, health care and welfare; education. Comparison industries: manufacturing; information and communications; finance and insurance. Offset: employed persons (Labour Force Survey).

### Table S4. Data sources by series and fiscal year
Provided as a separate Supporting Information file (the data dictionary of the public repository): source document, table number and fiscal years for every series.
