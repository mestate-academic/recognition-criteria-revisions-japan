**Article type:** Original article

**Title:** Changes in the composition of approved claims for overwork-related diseases after revisions of Japan's recognition criteria: national statistics for fiscal years 2009–2025

**Author:** Hironori UEMATSU

**Affiliation:** Uematsu Occupational Physician Office, Mestate LLC, Japan

**Correspondence:** Hironori Uematsu, Uematsu Occupational Physician Office, Mestate LLC, Ishikan Bldg. 4F-15, 280 Tenjinyama-cho, Nishikikoji-dori Muromachi Nishi-iru, Nakagyo-ku, Kyoto 604-8221, Japan. Tel: +81-75-275-5904. Fax: none. E-mail: office@mestate.jp

**Running title:** RECOGNITION CRITERIA AND OVERWORK-RELATED DISEASES



## Abstract

Japan revised its workers' compensation recognition criteria for overwork-related cerebro-cardiovascular disease (CCVD) in 2021 and for mental disorders in 2011, 2020, and 2023. Official analyses describe trends in claim categories but have not provided revision-aligned estimates. Using national statistics for fiscal years (FY) 2009–2025, we fitted interrupted time series models to annual totals and quasi-Poisson models with year fixed effects to ratios of counts between categories. For CCVD, no clear trend-adjusted level change in total approved claims was detected after the 2021 revision (level ratio, 1.11; 95% confidence interval [CI], 0.93–1.33), whereas the ratio of approved claims involving <80 h of monthly overtime to those involving ≥80 h increased 4.27-fold (95% CI, 3.28–5.57). For mental disorders, claims classified under harassment, bullying, or assault rose from 23% of approved claims in FY2017–2019 to 48% in FY2024–2025, and their ratio to other approved claims increased 2.04-fold (95% CI, 1.67–2.48) after the 2020 revision. About half of decided claims in this group were approved, compared with 3%–7% of claims classified under other interpersonal conflicts, whose decisions more than tripled. Aggregate data cannot distinguish changes in eligibility, exposure, recording, or adjudication. Monitoring should examine decisions and approvals within the categories relevant to each revision.

**Key words:** Workers' compensation, Recognition criteria, Karoshi, Overtime work, Cerebrovascular and cardiovascular diseases, Mental disorders, Interrupted time series analysis



## INTRODUCTION

Workers' compensation systems use recognition rules to determine which diseases qualify as work-related, and these rules determine who is compensated. Evidence from the United States indicates that restrictive compensability rules contribute to nonreceipt of workers' compensation benefits^1)^, and cases are lost at successive stages between illness onset and claim approval^2)^. Recognition rules are particularly important for multifactorial diseases, such as cerebro-cardiovascular disease (CCVD) and mental disorders. For these diseases, work-relatedness cannot be inferred from the diagnosis alone, so recognition criteria must specify which exposures and exposure levels are sufficient to establish it. Long working hours are associated with a higher risk of coronary heart disease and stroke^3, 4)^, and Japan, the Republic of Korea, and Taiwan have established explicit criteria for awarding compensation for CCVD attributed to overwork^5)^.

Japan compensates overwork-related CCVD on the basis of overtime thresholds, and in 2021 it revised its criteria for the first time in 20 yr. Since 2001, CCVD has been regarded as strongly work-related when overtime reached about 100 h in the month before onset or averaged about 80 h per month over the preceding 2 to 6 months. These thresholds are widely known as the "karoshi line"; karoshi means death from overwork^6, 7)^. The revision, effective September 15, 2021, kept the thresholds but stated explicitly that overtime close to them, combined with other workload factors, could establish work-relatedness^8, 9)^. For mental disorders, recognition criteria replaced earlier guidelines in 2011^10)^ and were revised in 2020 to add an explicit category for workplace harassment involving a power imbalance ("power harassment")^11)^ and in 2023 to add harassment by customers and other events^12)^. Under these criteria, a sufficiently severe workplace event can establish the required psychological stress without reference to working hours. The 2023 revision also reduced the number of cases requiring review by a specialist panel, with the aim of faster decisions.

Previous work has described the characteristics of compensated workers in Japan. The Ministry of Health, Labour and Welfare (MHLW) publishes annual counts of claims, decisions, and approved claims, and tabulates approved claims by recorded overtime^13)^. The Research Center for Overwork-Related Disorders of the National Institute of Occupational Safety and Health, Japan, has analyzed the case files of compensated claims and described the industries, occupations, and workloads involved, for CCVD and mental disorders together^6, 7)^. More recent case-file reports cover CCVD and mental disorder cases approved through FY2022^14, 15)^, and a commentary has described the revised criteria^16)^.

Previous official reports have also described these changes. In December 2025, the MHLW presented to the Council for the Promotion of Measures to Prevent Karoshi separate trends for approved CCVD claims involving <80 and ≥80 h of overtime, noting that the former had risen from about 20 per year through FY2021 to between 40 and 59 per year from FY2022^17)^. A council member had earlier pointed out the increase just below 80 h and the decrease at 80–<100 h and had questioned how working hours were being ascertained^18)^. For mental disorders, a case-file analysis of 5,805 cases approved in FY2012–2022 estimated average annual changes of −2.2% for cases involving ≥80 h of overtime and +16.0% for cases in the "Other" overtime category^15)^. These analyses describe trends. They do not estimate changes aligned with the dates of the revisions together with their uncertainty, they do not extend beyond FY2022 for case-file data, and they do not compare revision-associated changes across both CCVD assessment periods. For mental disorders, the 2026 white paper on measures to prevent karoshi noted that decided claims had increased most in the interpersonal-relations category of events, particularly "trouble with a superior"^19)^, but it did not report how often claims in each category were approved.

Evaluations of recognition criteria themselves are few. An earlier cross-country evaluation examined the introduction of CCVD recognition criteria in Japan in 2001 and Taiwan in 2010 and reported increases in the rate of compensated cases of 2.81-fold in Japan, 2.53-fold in Taiwan, and 2.58-fold in a pooled model^20)^. In Korea, approval rates for occupational CCVD fell and then rose again after successive changes to standards and procedures; these changes were described but were not evaluated with an intervention model^21)^. Neither study examined changes in the distribution of approved claims across recorded-overtime categories.

Outside East Asia, interrupted time series studies have evaluated compensation reforms in Australia^22, 23)^, premium incentives in Finland^24)^, and presumptive coverage for posttraumatic stress disorder (PTSD) in Canada^25)^. Some of these studies examined subgroups, such as PTSD versus other mental health conditions^25)^, claim types^22)^, or claim severity^24)^. These studies show that changes following compensation reforms may differ across claim categories.

This matters for the Japanese revisions because totals can obscure a change that is confined to one category of cases. The 2021 revision clarified recognition when overtime was close to, but below, the existing thresholds and additional workload factors were present. Over the same years, statutory caps on overtime, phased in from 2019^26)^, may have reduced the number of workers with very long hours. The distribution of approved claims by overtime could therefore change even if the total did not. For mental disorders, the revisions added events that do not depend on working hours, so the mix of approved claims across the reported overtime categories could also change. The problem is not specific to Japan: compensation systems that use working-hour thresholds or presumptions of work-relatedness face it whenever those thresholds or presumptions are revised or reinterpreted.

We therefore examined, for each disease group, how the composition of approved claims changed after the revisions and whether analyses of totals would describe those changes. Using national statistics for fiscal years 2009 to 2025, we estimated changes in total claims, decisions, and approved claims; as the primary analysis, we estimated the change in the ratio of approved CCVD claims involving <80 versus ≥80 h of overtime per month after the 2021 revision; and, as a secondary analysis, we examined annual totals and processing times for mental disorders across the three revisions and described the reported overtime categories and the event categories of decided and approved claims around the 2020 and 2023 revisions. The study adds revision-aligned estimates from a 17-yr national series through FY2025, sensitivity analyses, comparisons showing how the interpretation of CCVD overtime categories depends on whether the two assessment periods are combined or analyzed separately, and, for mental disorders, approval proportions by event category. Given the aggregate data and the absence of an untreated comparison series, we interpret the findings as temporal associations rather than causal effects.

## SUBJECTS AND METHODS

### Setting

Japan's Industrial Accident Compensation Insurance covers the employees of almost all private employers. Claims for overwork-related disease are filed with local Labour Standards Inspection Offices. Inspectors investigate working hours and workplace events and decide whether the disease is work-related by applying criteria issued by the Ministry of Health, Labour and Welfare (MHLW).

The 2021 revision of the CCVD criteria had four elements^9, 16)^. First, overtime close to but below the thresholds could establish work-relatedness when other workload factors were present. Second, new workload factors were listed, such as rest intervals of less than about 11 h between shifts and physically demanding work. Third, the criteria for short-term overload and extraordinary events were clarified. Fourth, severe heart failure was added to the list of compensable diseases.

The revisions of the mental disorder criteria are summarized in Supplementary Table S1. Under these criteria, a single workplace event, such as severe harassment or violence, can independently warrant a rating of "strong" psychological stress; claim approval also requires the other recognition conditions to be met^10, 12)^. The annual statistics include an "Other" overtime category for approved claims, described below^13)^.

### Data

We used the MHLW's reports on compensation for overwork-related disorders, which are published annually for the preceding fiscal year (FY; April to March)^13)^. The reports provide national counts of claims, decisions (adjudicated claims, whether approved or denied), and approved claims for CCVD and mental disorders. Approved claims are also tabulated by the overtime hours established during the investigation. Overtime is not tabulated for denied claims.

*Approved CCVD claims by overtime.* Claims approved for long-term overload are reported in categories of average monthly overtime: <45, 45–<60, 60–<80, 80–<100, 100–<120, 120–<140, 140–<160, and ≥160 h. Overtime is averaged over the applicable preonset assessment period: either 1 month (threshold, about 100 h) or 2 to 6 months (threshold, about 80 h per month). A separate category covers claims approved for short-term overload or extraordinary events. For FY2009–2019, we used tables that combine the two assessment periods, published by an expert committee^27)^. Separate tables for each assessment period are available from FY2017; we summed the category counts across these tables for FY2020 onward. For FY2017–2019, these sums matched the combined tables.

*Approved mental disorder claims by overtime.* Approved claims are reported in categories of average monthly overtime during the psychological-stress assessment period (<20, 20–<40, 40–<60, 60–<80, 80–<100, 100–<120, 120–<140, 140–<160, and ≥160 h), with an additional "Other" category (FY2017–2025). Footnotes to the annual reports describe this category as claims judged work-related without an investigation of working hours, such as claims in which the psychological stress of an event was judged to be extreme^13)^. A ministry document presenting the same counts for FY2017 and FY2018 states instead that reporting of overtime was not mandatory and that cases without reported overtime were counted in "Other"^28)^. The administrative meaning of the category is therefore not entirely clear, and we refer to it as the "Other" category.

*Processing time for mental disorders.* We obtained mean times from claim filing to decision from expert committee materials for FY2009–2020^29)^ and MHLW policy evaluation documents for FY2021–2024^30)^. The former reported time in months, which we converted to days by multiplying by 30; the latter reported time in days.

*Mental disorder claims by event.* For each decided claim, the reports identify one "specific event" from the list in the recognition criteria, a "special event" (extreme psychological stress or extremely long working hours), or the residual "Other" event category, which includes claims for which no assessable event was identified; decisions and approved claims are tabulated by event, and the items sum to the annual totals^13)^. We used the tables for FY2017–2025, taking FY2019 from the 2020 white paper^31)^ and FY2020 from expert committee material^29)^. The list of events changed in June 2020, when "power harassment involving a power imbalance" was added, and in September 2023, when "serious misconduct by customers or clients" was added and other items were merged; FY2022 was restated on the 2023 list. For exploratory comparisons across the changing lists, we combined items into eight groups. This grouping does not eliminate differences caused by the introduction, merger, or reassignment of event items. The harassment group comprised power harassment, assault or severe bullying or harassment (before June 2020, "[severe] harassment, bullying, or assault"), sexual harassment, and serious misconduct by customers. The other groups were other interpersonal conflicts (trouble with a superior, coworker, or subordinate and changes in workplace relationships), workload (changes in the quantity or quality of work, including overtime of ≥80 h per month and consecutive work for ≥2 weeks), accidents and disasters, work failures and excessive responsibility, changes in role or position, special events, and the residual "Other" event category (Supplementary Table S9). The tables record one main event category per decided claim, including denied claims, rather than every event experienced by the claimant. Approval proportions describe outcomes conditional on the recorded administrative category; differences between groups may reflect severity, evidence, and classification as well as adjudication.

All values other than the event counts were transcribed by hand, with the source recorded for each value, and were checked against overlapping editions, annual totals, and the text of the reports. The event counts were transcribed from the published tables with the AI tool described below. For every year, the items summed to the published totals of decisions and approved claims. Counts agreed across editions using the same item list. FY2022 was taken from the restated 2023 list; its group-level decision counts differed slightly from those on the earlier list, whereas approved-claim counts were unchanged. Values were available throughout the periods analyzed. Processing time for FY2025 was unavailable in the sources consulted as of November 18, 2026. The policy evaluation documents report 3,509 decisions for FY2024, compared with 3,496 in the series that we used, so the processing-time statistics may cover a slightly different set of claims. Claims are counted by fiscal year of filing, and decisions and approved claims by fiscal year of decision. Since September 2020, the reports have tabulated a separate multiple-employment-factor category for workers whose combined workload across employers is assessed. Claim filings do not distinguish employment-injury claims from claims subsequently assessed under this category, whereas the decision and approval counts that we used exclude it (fewer than 10 approved CCVD claims in any year). Sources for the original series are listed in Supplementary Table S2; sources and grouping rules for the event-category series are given in Supplementary Table S9.

### Statistical analysis

*Primary analysis: distribution of approved CCVD claims by overtime.* The primary estimand was the relative change in the ratio of approved claims involving <80 versus ≥80 overtime hours per month, comparing FY2022–2025 with FY2009–2020. Counts from the two assessment periods were combined. We selected 80 h because it is the lower of the two overtime thresholds in the criteria and can be applied consistently throughout the study period; classification using the threshold specific to each assessment period was available only from FY2017. FY2021 was excluded as a transition year because the revision took effect in the middle of it. We fitted a quasi-Poisson model to the annual count in each category:

log E(count) = α(year) + β × Low + δ × (Low × Post),

where α(year) is a fixed effect for each fiscal year, Low indicates the <80-hour category, and Post indicates FY2022–2025; exp(δ) is the relative change in the ratio. This estimand describes the composition of approved claims; it is not a ratio of approval probabilities or an estimate of disease incidence. The ≥80-hour category was subject to the same policy environment and is not an untreated control. The year fixed effects absorb factors that changed both categories by the same proportion in a given year, such as the overall volume of claims. They do not remove factors that affected the two categories differently. We assessed robustness to category-specific linear trends, alternative standard errors, changes in the years included, and placebo intervention dates. Alternative specifications used standard errors clustered by year or ordinary least squares models of the annual log ratio with a linear trend and Newey-West standard errors (lag 1)^32)^. We also repeated the analysis after excluding each year in turn and after restricting the prerevision period to FY2015–2020. The first set of placebo models used 4-yr pseudo-postrevision periods beginning in each year from FY2012 through FY2017, compared with all preceding years from FY2009. The second set used pseudo-postrevision periods beginning in each year from FY2012 through FY2018 and ending in FY2020. Clustering by year allows for correlation between the two categories within a year but not for serial correlation across years.

*Totals.* We analyzed annual claims, decisions, and approved claims with quasi-Poisson segmented regression, and the approval proportion (approved claims divided by decisions) with quasi-binomial regression weighted by the number of decisions^33–35)^. Each model included a linear time trend and a postrevision indicator. The exponentiated indicator coefficient represents a level ratio (the ratio of expected annual counts after versus before the revision, given the trend) for the count models and an odds ratio for the approval-proportion model. For CCVD, the models covered FY2009–2025, the postrevision period was FY2022–2025, and FY2021 was excluded. For mental disorders, the three revisions were modeled together over FY2009–2025, with indicators from FY2012, FY2020, and FY2024; FY2023 was excluded because the 2023 revision took effect in the middle of it, whereas the 2011 and 2020 revisions took effect near the end and the beginning of a fiscal year, respectively. The study period began in FY2009 because decisions for mental disorders are available from that year. In sensitivity analyses, we changed the analytic window, removed the trend, coded the transition year differently, added a change in slope, and used ordinary least squares with Newey-West standard errors (Supplementary Table S3).

*Assessment periods (exploratory).* Using the separate tables for FY2017–2025, we compared claims approved below the threshold for their own assessment period (<100 h for 1 month; <80 h for 2 to 6 months) with claims approved at or above it, and we examined each assessment period separately. These categories are defined operationally by the hour thresholds; the revision addressed overtime close to the thresholds in combination with other factors, not every case below a threshold. The separate tables cover only 4 yr before and 4 yr after the revision, and the contrasts use overlapping data, so they are not independent confirmation of the primary analysis. For the pooled below-versus-at-or-above-threshold contrast, we also fitted models with category-specific trends and calculated confidence intervals using year-clustered or Newey-West standard errors (Supplementary Table S4). These analyses were added after critical review of an earlier draft and are post hoc.

*Other elements of the revision.* We compared claims approved for short-term overload or extraordinary events with those involving ≥80 h. Because severe heart failure was added to the compensable diseases, we also compared approved claims for cardiac disease with those for cerebrovascular disease.

*Mental disorders (secondary).* For FY2017–2025, excluding FY2023 as a transition year, we used the same fixed-effects model with indicators beginning in FY2020 and FY2024. We estimated changes in two ratios: approved claims in the "Other" category versus approved claims involving ≥80 h, and approved claims involving <80 versus ≥80 h. Processing time was described without modeling. For the event groups, we tabulated mean annual decisions, mean annual approved claims, and the approval proportion (approved claims divided by decisions) for FY2017–2019, FY2020–2022, and FY2024–2025. With the same fixed-effects model, we estimated changes in the ratio of approved claims in the harassment group to approved claims in all other groups and in the ratio of decisions in the other-interpersonal-conflicts group to decisions in all other groups. The event-group analyses were added after the other analyses had been completed and are post hoc.

We report 95% confidence intervals without adjustment for multiple comparisons; all analyses other than the primary analysis should be interpreted as secondary or exploratory. Dispersion estimates for the primary model and the models of annual totals are given in the table footnotes. Analyses were performed in Python 3 with the pandas and statsmodels packages. Reporting was guided by the applicable recommendations of the STROBE and RECORD statements^36, 37)^; the completed checklist is provided as Supplementary material 2.

### Ethical considerations

The study used only publicly available aggregate statistics that contain no information on identifiable individuals. Ethical review and informed consent were therefore not required, and no ethics committee approval was sought. The study was conducted in accordance with the principles of the Declaration of Helsinki.

### Use of generative artificial intelligence

Generative artificial intelligence (AI) tools were used in this study. Under the author's direction, Claude (Anthropic, San Francisco, CA; Claude Opus 5.5 and Claude Fable 5.2 models, accessed through the claude.ai application in November 2026) was used to develop and execute Python code for data tabulation, statistical modeling, and figure generation. It was also used to draft and edit the English text of all sections of the manuscript and to search for, compile, and format the references. ChatGPT (OpenAI, San Francisco, CA; GPT-6 Astra model) was used in November 2026 for critical review of drafts, AI-assisted reanalysis of the public data, and English-language editing. The AI tools did not supply any data values: every numerical result is the output of the archived code applied to the transcribed data. No personal or proprietary data were entered into the tools, and no model was trained or fine-tuned for this study. Because generative AI tools can produce incorrect code, inaccurate statements, and nonexistent references, their output was validated as follows. The author selected the data sources, transcribed the values (except the event counts, as described above) and verified all values against the original government documents, reviewed the code and its output, checked every reported result against the output files, and manually checked every reference against its original source. The key estimates were also recalculated from the public data in a separate AI-assisted reanalysis and agreed with the reported values. The author takes full responsibility for the integrity of the content.

## RESULTS

### CCVD: totals

For FY2009–2020 versus FY2022–2025, mean annual counts were 826 versus 1028 for claims, 686 versus 693 for decisions, and 268 versus 217 for approved claims. The corresponding approval proportions were 39.1% and 31.3% (Table 1). In models with a linear time trend for each outcome, no clear change in level was detected for claims (level ratio [RR], 1.13; 95% CI, 0.93–1.36), decisions (RR, 1.02; 95% CI, 0.84–1.23), approved claims (RR, 1.11; 95% CI, 0.93–1.33), or the approval proportion (odds ratio [OR], 1.17; 95% CI, 0.90–1.51) (Table 2). Although the mean annual number of approved claims was lower after the revision, no clear level change was detected after adjustment for a common linear time trend. The confidence interval was compatible with changes ranging from a 7% decrease to a 33% increase. The estimate for the approval proportion depended on the analytic window (Supplementary Table S3), and we regard it as uncertain.

>>> <Tables 1 and 2 near here>

### CCVD: distribution by overtime

The distribution of approved claims by overtime changed (Fig. 1; Table 3). The mean annual number of approved claims involving <80 h of overtime per month rose from 18.6 in FY2009–2020 to 48.5 in FY2022–2025, whereas the corresponding number involving ≥80 h fell from 230.9 to 141.0. Claims approved for short-term overload or extraordinary events rose from 18.9 to 27.5. The mean annual share of approved claims involving <80 h rose from 7.0% to 22.5%.

>>> <Fig. 1 and Table 3 near here>

The ratio of approved claims involving <80 h to those involving ≥80 h increased 4.27-fold (95% CI, 3.28–5.57). The estimate was 3.81 (95% CI, 2.22–6.53) with category-specific trends, 4.27 (95% CI, 2.95–6.20) with standard errors clustered by year, and 3.81 (95% CI, 1.73–8.37) when both were used. The ordinary least squares model of the annual log ratio, with a linear trend and Newey-West standard errors, yielded an estimate of 3.88 (95% CI, 2.33–6.48). When each year was excluded in turn, the estimate ranged from 4.01 to 4.60, and it was 4.54 (95% CI, 3.11–6.63) when the prerevision period was shortened to FY2015–2020 (Table 3; Supplementary Table S5). In the placebo models with 4-yr windows, estimates ranged from 0.71 to 1.12, and one of the six confidence intervals excluded 1 (FY2015–2018: 0.71; 95% CI, 0.53–0.94). In the second set of placebo models, estimates ranged from 0.90 to 1.33, and all confidence intervals included 1 (Supplementary Table S6).

The ratio of claims approved for short-term overload or extraordinary events to those involving ≥80 h also increased (relative change, 2.38; 95% CI, 1.46–3.89). No clear change was detected in the ratio of cardiac to cerebrovascular cases (0.98; 95% CI, 0.86–1.11).

### CCVD: assessment periods

Fig. 2A and Supplementary Table S7 show approved claims separately for the two assessment periods in FY2017–2025. Among claims assessed over 1 month, those involving ≥100 h fell from a mean of 75.8 per year in FY2017–2020 to 44.3 in FY2022–2025, and those involving <100 h rose from 3.8 to 17.3. Among claims assessed over 2 to 6 months, those involving 80–<100 h fell from 82.3 to 48.3 per year, and those involving <80 h rose from 17.0 to 42.5. In this group, mean annual counts involving ≥100 h were similar before and after the revision (33.8 and 37.3), as was the group total (133.0 and 128.0).

>>> <Fig. 2 near here>

Claims approved below the threshold for their assessment period accounted for 7.1%–12.0% of all approved claims in FY2017–2020 and 22.7%–33.5% in FY2022–2025. Their ratio to claims approved at or above the thresholds increased 4.26-fold (95% CI, 2.84–6.37; Fig. 2B; Supplementary Table S7). Allowing category-specific trends reduced precision (3.60; 95% CI, 1.25–10.35), and the confidence interval included 1 when standard errors were also clustered by year (95% CI, 0.50–25.87; Supplementary Table S4). With only 4 yr on each side of the revision, these analyses are descriptive; they are consistent with the primary analysis but do not confirm it independently.

In the combined tables, no clear change was detected in the ratio of approved claims involving 80–<100 h to those involving ≥100 h (0.96; 95% CI, 0.81–1.13; Fig. 2B). Mean annual counts decreased by similar proportions in the two categories, from 99.8 to 59.5 and from 131.1 to 81.5, respectively. The estimate was similar when the prerevision period was limited to FY2017–2020 (0.93; 95% CI, 0.75–1.15). The separate tables show that this combined ratio conceals different patterns in the two assessment periods. Among claims assessed over 2 to 6 months, the ratio fell (0.53; 95% CI, 0.40–0.71), because claims involving 80–<100 h decreased while those involving ≥100 h did not. Among claims assessed over 1 month, the decrease was in claims involving ≥100 h.

### Mental disorders

Claims rose from 1136 in FY2009 to 4958 in FY2025, and approved claims from 234 to 1082 (Fig. 3A; Table 1). After the 2011 criteria were introduced, the approval proportion increased (OR, 1.63; 95% CI, 1.34–1.99), and no clear change in claims was detected (Table 2). After the 2020 revision, approved claims increased (RR, 1.22; 95% CI, 1.06–1.40). The estimates for the 2023 revision depended on how the trend was specified. In the main model, claims (RR, 1.43; 95% CI, 1.26–1.63) and approved claims (RR, 1.54; 95% CI, 1.37–1.74) were higher after the revision. When the slope was allowed to change from FY2020, the estimate for claims was 1.00 (95% CI, 0.85–1.18) and that for approved claims was 1.32 (95% CI, 1.02–1.71) (Supplementary Table S3). The estimated level change in claims was thus not robust to allowing a slope change from FY2020. The estimate for approved claims was attenuated but remained above 1; the short follow-up and the sensitivity to trend specification limit attribution to the 2023 revision.

>>> <Fig. 3 near here>

Most of the increase was in the "Other" overtime category. Mean annual counts in this category increased from 139 in FY2017–2019 to 315 in FY2020–2022 and 657 in FY2024–2025. These claims accounted for 24%–31% of all approved claims in FY2017–2019 and 58%–65% in FY2024–2025 (Fig. 3C; Supplementary Table S8). In the fixed-effects models, the ratio of approved claims in the "Other" category to those involving ≥80 h increased 2.70-fold (95% CI, 1.90–3.82) after the 2020 revision and a further 1.60-fold (95% CI, 1.15–2.21) after the 2023 revision. The corresponding estimates for the ratio of approved claims involving <80 h to those involving ≥80 h were 1.25 (95% CI, 1.02–1.52) and 0.90 (95% CI, 0.72–1.11). Approved claims involving ≥80 h and those involving <80 h each stayed between about 150 and 230 per year. Mean processing time was approximately 255 d in FY2011 and 216 d in FY2015–2017, compared with 277–278 d in FY2023–2024 (Fig. 3D). The recent values exceed both the 8-month standard processing period (about 240 d) and the administrative target of 215 d^30)^. Annual decisions increased from 1355 in FY2016 to 3496 in FY2024. Annual approved claims involving suicide or attempted suicide ranged from 63 to 99 over FY2009–2025.

### Mental disorders: event categories

Table 4 shows decisions and approved claims by event group. Approved claims classified under harassment, bullying, or assault increased from a mean of 115.3 per year in FY2017–2019 to 248.7 in FY2020–2022 and 509.5 in FY2024–2025, and their share of all approved claims rose from 23.4% to 38.3% and 47.7%. The ratio of approved claims in this group to approved claims in all other groups increased 2.04-fold (95% CI, 1.67–2.48) after the 2020 revision and a further 1.47-fold (95% CI, 1.25–1.72) after the 2023 revision. Within the group, approved claims for power harassment numbered 99 in FY2020, the year in which the item was introduced, and 222 in FY2025; those for serious misconduct by customers numbered 52 in FY2023 and 127 in FY2025; and those for sexual harassment rose from 35 in FY2017 to 127 in FY2025 (Supplementary Table S9).

>>> <Table 4 near here>

Approval proportions differed widely between event groups and also changed within several groups. In the harassment group, 46.8% of decided claims were approved in FY2017–2019, 54.5% in FY2020–2022, and 53.7% in FY2024–2025. In the other-interpersonal-conflicts group, the corresponding proportions were 6.6%, 4.5%, and 3.5%. Decisions in the latter group rose from a mean of 385.0 per year in FY2017–2019 to 1,298.5 in FY2024–2025, and their share of all decisions rose from 25.2% to 35.4%; the ratio of decisions in this group to decisions in all other groups increased 1.20-fold (95% CI, 1.04–1.39) after the 2020 revision and a further 1.35-fold (95% CI, 1.20–1.53) after the 2023 revision. Decisions on claims classified under trouble with a superior alone rose from 320 in FY2017 to 1,061 in FY2025, of which 22 and 36 were approved. The overall approval proportion was 32.2% in FY2017–2019 and 29.1% in FY2024–2025. In the workload group, mean annual approved claims were 145.7 in FY2017–2019 and 196.5 in FY2024–2025, and the group's share of approved claims fell from 29.5% to 18.4%.

Approved claims in the harassment group (123 in FY2017 and 538 in FY2025) and approved claims in the "Other" overtime category (144 and 699) increased over the same years. The two classifications are not cross-tabulated in the reports, so the overlap between them is unknown.

## DISCUSSION

### Main findings

The composition of approved claims changed differently in the two disease groups: toward lower recorded-overtime categories for CCVD and toward the reported "Other" overtime category for mental disorders. After Japan's 2021 revision of the CCVD criteria, no clear trend-adjusted level change was detected in the total number of approved claims, but approved claims involving <80 h of overtime per month rose 2.6-fold and their ratio to those involving ≥80 h rose about 4-fold. This estimate was stable when single years were excluded, and placebo models within the prerevision period gave estimates between 0.71 and 1.33. In both assessment periods, approved claims involving overtime below the applicable threshold increased. Among claims assessed over 1 month, those involving overtime at or above the threshold decreased; among claims assessed over 2 to 6 months, those just above the threshold (80–<100 h) decreased. For mental disorders, the "Other" category increased from about one-quarter of approved claims in FY2017–2019 to about three-fifths in FY2024–2025, whereas approved claims involving ≥80 h ranged from 149 to 227 per year. Because overtime is not quantified in the "Other" category, this change does not show that compensated workers with mental disorders worked less overtime. In the tables by event, claims classified under harassment, bullying, or assault rose from about one-quarter to about one-half of approved claims. About half of decided claims in this group were approved in every period, whereas the group with the largest absolute increase in decisions, other interpersonal conflicts, had an approval proportion of 3%–7%. Processing times in FY2023–2024 were longer than in the mid-2010s, but only 1 complete year of processing-time data was available after the 2023 revision.

### Possible explanations for the change in CCVD claims

At least three explanations are possible, and they are not mutually exclusive.

One possible explanation is broader recognition of claims involving overtime below the thresholds. Under the revised criteria, claims that might previously have been denied could have been approved for workers with overtime below the thresholds and additional workload factors. Such a pattern would be consistent with the revision's clarification of recognition below the thresholds.

A second possible explanation is a reduction in working hours. Overtime caps introduced in April 2019 (April 2020 for small and medium-sized employers) limit overtime, including work on statutory holidays, to less than 100 h in any single month and to an average of no more than 80 h over 2 to 6 months^26)^. These limits are close to the thresholds of the criteria. From April 2019, employers were also required to ascertain working hours for occupational health purposes, generally using objective records^38)^. If overtime fell to just below the thresholds among workers who subsequently developed CCVD, the revision may have maintained their access to compensation rather than extended eligibility to new groups. Because decisions are made some time after onset, an effect of the caps could overlap in time with the revision. Sector-specific implementation dates, however, limit the extent to which the overtime caps alone can explain the national pattern. The caps took effect in the construction sector and for motor-vehicle drivers only in April 2024. For drivers, the ceiling is 960 h of overtime per year, excluding work on statutory holidays, and the general monthly and multimonth ceilings do not apply^39)^, yet road freight transport accounts for the largest share of approved CCVD claims^13)^.

A third possible explanation is a change in how hours were recorded. Changes in the documentation or assessment of overtime may have shifted the distribution of recorded overtime among approved claims relative to the thresholds, without corresponding changes in actual hours or eligibility. This possibility has been raised in the Council for the Promotion of Measures to Prevent Karoshi^17, 18)^.

The number of approved claims involving <80 h more than doubled, so the change in the ratio was not produced solely by a decline in the reference category. The prerevision share of such claims also showed no sustained upward trend (range, 4.8%–10.6% in FY2009–2020). These observations do not, however, distinguish among the three explanations. Among claims assessed over 2 to 6 months, the decrease was concentrated just above the threshold, whereas counts involving ≥100 h and the total count changed little. This pattern is compatible with a shift in recorded overtime from just above to just below the threshold. It is also compatible with wider eligibility combined with fewer workers recording 80–<100 h. Other events during this period, including the COVID-19 pandemic, may also have affected the overtime categories differently. Distinguishing among these explanations would require counts of denied claims stratified by recorded overtime or individual claim records.

### Mental disorders

The tables by event give a clearer picture than the overtime categories. After the 2020 revision, which added power harassment as an explicit item, and the 2023 revision, which added serious misconduct by customers, approved claims classified under harassment, bullying, or assault increased relative to all other approved claims. This pattern is compatible with the content of the revisions. It also coincided with legislation that required large employers to implement measures to prevent power harassment from June 2020 and small and medium-sized employers from April 2022^40)^, which may have increased awareness and claiming. The data cannot separate these influences. Part of the increase may also reflect reclassification: an event that would have been recorded as trouble with a superior before June 2020 may have been recorded as power harassment afterward. Concurrent increases in both groups do not rule out a substantial contribution from reclassification, because total decisions also increased. The aggregate tables cannot quantify movements between categories.

The growing share of decisions in the other-interpersonal-conflicts group, which had a low approval proportion, may have contributed to the decline in the overall approval proportion from 32.2% in FY2017–2019 to 29.1% in FY2024–2025. Approval proportions also changed within several groups, and these analyses do not quantify the relative contributions of changes in composition and within-group approval proportions. Claims classified under conflicts with superiors or coworkers, of which few are approved, made up a growing share of decisions. These claims still require investigation, which may be relevant to the longer processing times in recent years; however, processing time is not tabulated by event, data were available for only 1 full year after the 2023 revision, and the contributions of investigative complexity and rising caseloads could not be determined. Growth in the "Other" overtime category paralleled growth in the harassment group, which is compatible with the recognition of severe workplace events independently of working hours, but the reports do not cross-tabulate the two classifications.

### Comparison with previous studies and what this study adds

Lin and colleagues found that new CCVD criteria in Japan in 2001 and in Taiwan in 2010 were each followed by a more than 2.5-fold increase in the rate of compensated cases^20)^. Japan's 2021 revision was followed by a change in the distribution of approved claims without a clear trend-adjusted level change in their total number. An analysis restricted to total approved CCVD claims would not describe the redistribution across overtime categories. The absence of a clear adjusted level change does not, however, establish that the total was unaffected. Durand-Moreau and colleagues found that presumptive coverage restricted to PTSD in Canada was associated with a higher proportion of PTSD claims among all lost-time claims; no clear association was detected for the corresponding proportion of other mental health claims^25)^. The Canadian study illustrates the value of examining claim categories separately; our analysis applies this principle to recorded-overtime and assessment-period categories, although our overtime groups only approximate the cases addressed by the Japanese revision.

The counts analyzed here are published every year, and official analyses have already described the increase in approved CCVD claims involving <80 h and the growth of the "Other" category for mental disorders^15, 17)^. The present analysis builds on those descriptions in four ways. First, it estimates changes aligned with the dates of the revisions and gives their size and uncertainty. For CCVD, the change was measured against 12 prerevision years, and the estimate was robust to category-specific trends, alternative standard errors, the exclusion of single years, and placebo revision dates. Second, it extends the national series through FY2025. Third, the exploratory analysis by assessment period showed that a change in one category was accompanied by an opposite change in the adjacent category. In the combined tables, the ratio of approved claims involving 80–<100 h to those involving ≥100 h appeared unchanged (0.96), whereas among claims assessed over 2 to 6 months it fell by about half (0.53). Adjacent categories should therefore be examined together and within each assessment period. Fourth, for mental disorders, it reports approval proportions by event group. The 2026 white paper described the growth of decided claims in the interpersonal-relations category^19)^; the present analysis shows that this growth was concentrated in claims of which 3%–7% were approved, whereas the growth in approved claims was concentrated in the harassment group, of which about half were approved.

The study also complements analyses of the case files of compensated claims. Earlier case-file reports described prerevision cases^6, 7)^, whereas more recent work includes cases approved through FY2022^14, 15)^. National statistics cover every year before and after the revisions but contain no information on the workload factors recorded in individual cases. Case-file data for claims decided after the 2021 revision could establish what our data cannot: which workload factors supported approval when overtime was below the thresholds, and which events underlie the "Other" category for mental disorders.

### Implications

The 2021 revision kept the existing hour thresholds and clarified that overtime close to them, together with other workload factors, could support recognition. After this clarification, the distribution of approved claims across the overtime categories changed substantially, although no clear trend-adjusted level change was detected in their total number. This finding supports monitoring claims by recognition category, but it does not establish that the revision increased an individual claimant's probability of receiving compensation.

Systems in Korea and Taiwan use overtime-based recognition criteria^5)^, and several Canadian jurisdictions use presumptive coverage for specified mental health conditions^25)^. For such systems, evaluations should examine the exposure, diagnosis, or occupational categories addressed by a revision, together with relevant comparison categories, not only total approved claims or approval proportions. Reporting approved and denied claims within those categories, alongside processing time, would make changes in compensation outcomes more interpretable. The Japanese statistics for mental disorders show what such reporting makes possible: because decisions and approved claims are both tabulated by event, approval proportions can be calculated for each event group. For CCVD, by contrast, only approved claims are tabulated by recorded overtime. Tabulating decided CCVD claims by recorded overtime in the same way would allow approval proportions to be calculated for each overtime category.

Further research should assess whether investigative capacity has kept pace with the increasing number of mental disorder claims. For occupational health practice, the revised criteria mean that a worker who develops CCVD after substantial overtime below the thresholds may still be compensated when other workload factors are present. Documenting these factors, such as short rest intervals between shifts, in workplace health records may therefore help workers and adjudicators.

### Strengths and limitations

The study used complete national statistics spanning 17 yr, distinguished claim filings from decisions and approved claims, and analyzed the two assessment periods separately. The data and code are publicly available.

The study has several limitations. First, the data are aggregate. Although approval proportions could be calculated for recorded event categories, overtime was tabulated only for approved claims, so approval proportions by overtime category could not be calculated. Individual claims could not be followed. Second, the overtime categories reflect the hours established in the investigation, which may be underestimated and may themselves change after a revision. Third, there was no control series, because all claims in Japan are decided under the same criteria, and several events coincided with the revisions: the overtime caps, the requirement to record working hours, the COVID-19 pandemic, and the harassment-prevention legislation. We therefore report associations, not causal effects. Fourth, the series are short and may be serially correlated. The primary analysis included 16 fiscal years, whereas the assessment-period and mental disorder composition analyses included only 8. Confidence intervals from these short series, particularly those based on 8 year clusters, should be interpreted cautiously. The assessment-period tables and the mental disorder categories begin in FY2017, and follow-up after the 2021 and 2023 revisions was 4 and 2 yr, respectively. Fifth, we made many comparisons without adjustment for multiplicity, and the assessment-period analyses were post hoc. Sixth, the combined CCVD tables came from different sources before and after FY2020, although they matched in the overlapping years. Seventh, each mental disorder claim is assigned to a single event, the list of events changed in 2020 and 2023, and our event groups were defined after the data had been seen; reclassification between items may have contributed to the changes between groups. Eighth, the published descriptions of the mental disorder "Other" category are not entirely consistent. Changes in its frequency may reflect both adjudication and reporting practices and cannot be interpreted as changes in the prevalence of low overtime. Finally, the findings come from one country, and the size of any change after a revision will depend on how each system defines its thresholds.

### Conclusions

After the 2021 revision, approved CCVD claims were more frequently classified below 80 h of monthly overtime relative to those classified at or above 80 h: the ratio increased about 4-fold, whereas no clear trend-adjusted level change was detected in the total number of approved claims. Approved claims for mental disorders were increasingly classified under harassment, bullying, or assault, of which about half of decided claims were approved, whereas the largest absolute increase in decisions occurred in the other-interpersonal-conflicts group, in which few claims were approved. Approved claims also increasingly belonged to the reported "Other" overtime category, which does not establish the amount of overtime worked. These aggregate data cannot establish whether the changes reflect broader access to compensation, reduced overtime, changes in recording or adjudication, or a combination of these processes. Evaluations of recognition criteria should examine the categories that the criteria address together with the adjacent categories, and compensation statistics should report decided as well as approved claims by the same categories.

## Funding

This study received no funding.

## Conflict of interest

The author receives income from Mestate LLC, which provides contracted occupational physician services to companies, and from Nara Central Hospital, where he works as a physician. Neither organization funded this study or had any role in it. The author declares no other conflicts of interest.

## Data availability

All data analyzed are publicly available statistics of the Ministry of Health, Labour and Welfare, Japan. The transcribed data, the analysis code (Python), and the outputs are publicly available at https://github.com/mestate-academic/recognition-criteria-revisions-japan.



## REFERENCES

1) Spieler EA, Burton JF Jr (2012) The lack of correspondence between work-related disability and receipt of workers' compensation benefits. Am J Ind Med **55**, 487‒505.

2) Azaroff LS, Levenstein C, Wegman DH (2002) Occupational injury and illness surveillance: conceptual filters explain underreporting. Am J Public Health **92**, 1421‒9.

3) Kivimäki M, Jokela M, Nyberg ST, Singh-Manoux A, Fransson EI, Alfredsson L, Bjorner JB, Borritz M, Burr H, Casini A, Clays E, De Bacquer D, Dragano N, Erbel R, Geuskens GA, Hamer M, Hooftman WE, Houtman IL, Jöckel KH, Kittel F, Knutsson A, Koskenvuo M, Lunau T, Madsen IEH, Nielsen ML, Nordin M, Oksanen T, Pejtersen JH, Pentti J, Rugulies R, Salo P, Shipley MJ, Siegrist J, Steptoe A, Suominen SB, Theorell T, Vahtera J, Westerholm PJM, Westerlund H, O'Reilly D, Kumari M, Batty GD, Ferrie JE, Virtanen M, for the IPD-Work Consortium (2015) Long working hours and risk of coronary heart disease and stroke: a systematic review and meta-analysis of published and unpublished data for 603 838 individuals. Lancet **386**, 1739‒46.

4) Pega F, Náfrádi B, Momen NC, Ujita Y, Streicher KN, Prüss-Üstün AM, Descatha A, Driscoll T, Fischer FM, Godderis L, Kiiver HM, Li J, Magnusson Hanson LL, Rugulies R, Sørensen K, Woodruff TJ, Technical Advisory Group (2021) Global, regional, and national burdens of ischemic heart disease and stroke attributable to exposure to long working hours for 194 countries, 2000–2016: a systematic analysis from the WHO/ILO Joint Estimates of the Work-related Burden of Disease and Injury. Environ Int **154**, 106595.

5) Park J, Kim Y, Cheng Y, Horie S (2012) A comparison of the recognition of overwork-related cardiovascular disease in Japan, Korea, and Taiwan. Ind Health **50**, 17‒23.

6) Yamauchi T, Yoshikawa T, Takamoto M, Sasaki T, Matsumoto S, Kayashima K, Takeshima T, Takahashi M (2017) Overwork-related disorders in Japan: recent trends and development of a national policy to promote preventive measures. Ind Health **55**, 293‒302.

7) Takahashi M (2019) Sociomedical problems of overwork-related deaths and disorders in Japan. J Occup Health **61**, 269‒77.

8) Ministry of Health, Labour and Welfare. Report of the expert committee on recognition criteria for cerebrovascular and cardiovascular diseases, July 16, 2021 (in Japanese). https://www.mhlw.go.jp/stf/newpage_19809.html. Accessed November 16, 2026

9) Ministry of Health, Labour and Welfare. Recognition criteria for cerebrovascular diseases and ischemic heart diseases, etc., caused by work that markedly aggravates vascular lesions, etc. Notification Kihatsu 0914 No. 1, September 14, 2021, as amended in 2023 (in Japanese). https://www.mhlw.go.jp/content/001157873.pdf. Accessed November 19, 2026

10) Ministry of Health, Labour and Welfare. Recognition criteria for mental disorders caused by psychological load. Notification Kihatsu 1226 No. 1, December 26, 2011 (in Japanese). https://www.mhlw.go.jp/stf/houdou/2r9852000001z3zj-att/2r9852000001z43h.pdf. Accessed November 16, 2026

11) Ministry of Health, Labour and Welfare. Partial revision of the recognition criteria for mental disorders caused by psychological load. Notification Kihatsu 0529 No. 1, May 29, 2020 (in Japanese). https://www.mhlw.go.jp/content/11201000/000636671.pdf. Accessed November 19, 2026

12) Ministry of Health, Labour and Welfare. Recognition criteria for mental disorders caused by psychological load. Notification Kihatsu 0901 No. 2, September 1, 2023 (in Japanese). https://www.mhlw.go.jp/stf/newpage_34888.html. Accessed November 16, 2026

13) Ministry of Health, Labour and Welfare. Status of workers' compensation for karoshi and other overwork-related disorders, FY2009–FY2025 editions (in Japanese). Latest edition (July 15, 2026): https://www.mhlw.go.jp/stf/newpage_74476.html. Accessed November 16, 2026

14) Takami T. Analysis of consecutive work, night work and irregular work in approved workers' compensation cases of cerebrovascular and cardiovascular disease. JILPT Research Material Series No. 297, February 6, 2026 (in Japanese). https://www.jil.go.jp/institute/siryo/2026/297.html. Accessed November 16, 2026

15) Takami T. Analysis of events causing work-related psychological load in approved workers' compensation cases of mental disorders. Research report for fiscal year 2025, Research Center for Overwork-Related Disorders, National Institute of Occupational Safety and Health, Japan, October 1, 2026 (in Japanese). https://records.johas.go.jp/report/194. Accessed November 19, 2026

16) Koyano F (2022) Trends and commentary on revision of certification criteria for brain/heart disease and mental disorders. J Occup Health Law **1**, 105‒16. (in Japanese)

17) Ministry of Health, Labour and Welfare. Minutes of the 31st meeting of the Council for the Promotion of Measures to Prevent Karoshi, December 5, 2025 (in Japanese). https://www.mhlw.go.jp/stf/newpage_69379.html. Accessed November 19, 2026

18) Ministry of Health, Labour and Welfare. Minutes of the 30th meeting of the Council for the Promotion of Measures to Prevent Karoshi, June 27, 2025 (in Japanese). https://www.mhlw.go.jp/stf/newpage_64218.html. Accessed November 19, 2026

19) Ministry of Health, Labour and Welfare. White paper on measures to prevent karoshi, 2026 edition: summary (in Japanese). https://www.mhlw.go.jp/content/11200000/001757395.pdf. Accessed November 19, 2026

20) Lin RT, Lin CK, Christiani DC, Kawachi I, Cheng Y, Verguet S, Jong S (2017) The impact of the introduction of new recognition criteria for overwork-related cardiovascular and cerebrovascular diseases: a cross-country comparison. Sci Rep **7**, 167. Author correction (2018) Sci Rep **8**, 4654.

21) Kim UJ, Choi WJ, Kang SK, Lee W, Ham S, Lee J, Lee Y, Han E, Lee S, Kim Y, Kim I (2022) Standards for recognition and approval rate of occupational cerebro-cardiovascular diseases in Korea. Ann Occup Environ Med **34**, e30.

22) Collie A, Beck D, Gray SE, Lane TJ (2020) Impact of legislative reform on benefit access and disability duration in workers' compensation: an interrupted time series study. Occup Environ Med **77**, 32‒9.

23) Lane TJ, Di Donato MF, Collie A (2023) Injured worker outcomes after compensation system overhaul: an interrupted time series study. J Epidemiol Community Health **77**, 515‒20.

24) Rautiainen RH, Ledolter J, Sprince NL, Donham KJ, Burmeister LF, Ohsfeldt R, Reynolds SJ, Phillips K, Zwerling C (2005) Effects of premium discount on workers' compensation claims in agriculture in Finland. Am J Ind Med **48**, 100‒9.

25) Durand-Moreau Q, Descatha A, Adisesh A, Smith P (2026) Presumptive coverage policies and workers' compensation of post-traumatic stress disorder and other mental health conditions: a retrospective time-series study in Canada 2001–2019. Am J Ind Med **69**, 1027‒36.

26) Labour Standards Act (Act No. 49 of 1947), Article 36, as amended by Act No. 71 of 2018, in force April 1, 2019 (April 1, 2020, for small and medium-sized enterprises). (in Japanese)

27) Ministry of Health, Labour and Welfare. Status of workers' compensation for cerebrovascular and cardiovascular diseases. Material 1, 2nd meeting of the expert committee on recognition criteria for cerebrovascular and cardiovascular diseases, July 21, 2020 (in Japanese). https://www.mhlw.go.jp/content/11201000/000650614.pdf. Accessed November 16, 2026

28) Ministry of Health, Labour and Welfare. Status of workers' compensation for mental disorders. Material 2-1 (data through fiscal year 2018) (in Japanese). https://www.mhlw.go.jp/content/11201000/000576807.pdf. Accessed November 19, 2026

29) Ministry of Health, Labour and Welfare. Status of workers' compensation for mental disorders. Material 2, 1st meeting of the expert committee on recognition criteria for mental disorders, December 7, 2021 (in Japanese). https://www.mhlw.go.jp/content/11201000/000862995.pdf. Accessed November 16, 2026

30) Ministry of Health, Labour and Welfare. Policy evaluation: pre-analysis sheets for policy objective III-3-1, FY2024 and FY2025 (in Japanese). https://www.mhlw.go.jp/wp/seisaku/hyouka/dl/r06_jizenbunseki/31_III-3-1.pdf and https://www.mhlw.go.jp/wp/seisaku/hyouka/dl/r07_jizenbunseki/30_III-3-1.pdf. Accessed November 18, 2026

31) Ministry of Health, Labour and Welfare. White paper on measures to prevent karoshi, 2020 edition (in Japanese). https://www.mhlw.go.jp/wp/hakusyo/karoushi/20/dl/hakusho-zentai.pdf. Accessed November 19, 2026

32) Newey WK, West KD (1987) A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica **55**, 703‒8.

33) Wagner AK, Soumerai SB, Zhang F, Ross-Degnan D (2002) Segmented regression analysis of interrupted time series studies in medication use research. J Clin Pharm Ther **27**, 299‒309.

34) Lopez Bernal J, Cummins S, Gasparrini A (2017) Interrupted time series regression for the evaluation of public health interventions: a tutorial. Int J Epidemiol **46**, 348‒55.

35) Lopez Bernal J, Cummins S, Gasparrini A (2018) The use of controls in interrupted time series studies of public health interventions. Int J Epidemiol **47**, 2082‒93.

36) von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP, for the STROBE Initiative (2007) The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Lancet **370**, 1453‒7.

37) Benchimol EI, Smeeth L, Guttmann A, Harron K, Moher D, Petersen I, Sørensen HT, von Elm E, Langan SM, RECORD Working Committee (2015) The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med **12**, e1001885.

38) Industrial Safety and Health Act (Act No. 57 of 1972), Article 66-8-3, as amended by Act No. 71 of 2018, in force April 1, 2019, and Ordinance on Industrial Safety and Health, Article 52-7-3. (in Japanese)

39) Ministry of Health, Labour and Welfare. Hatarakikata Susume: work-style reform for construction, drivers and physicians (in Japanese). https://hatarakikatasusume.mhlw.go.jp/. Accessed November 16, 2026

40) Act on Comprehensive Promotion of Labour Policies (Act No. 132 of 1966), Article 30-2, as amended by Act No. 24 of 2019, in force June 1, 2020 (April 1, 2022, for small and medium-sized enterprises). (in Japanese)



**Table 1.** Annual mean numbers of claims, decisions, and approved claims for overwork-related disease before and after each revision of the recognition criteria, Japan

| Disease and revision | Period | Fiscal years | Claims | Decisions | Approved claims | Approval proportion, % |
|---|---|---|---:|---:|---:|---:|
| CCVD, September 2021 | Before | 2009–2020 | 826.1 | 686.4 | 268.4 | 39.1 |
| | After | 2022–2025 | 1027.5 | 692.8 | 217.0 | 31.3 |
| Mental disorders, December 2011 | Before | 2009–2011 | 1196.3 | 995.7 | 289.0 | 29.0 |
| | After | 2012–2014 | 1374.0 | 1239.0 | 469.3 | 37.9 |
| Mental disorders, May 2020 | Before | 2017–2019 | 1870.7 | 1530.7 | 493.3 | 32.2 |
| | After | 2020–2022 | 2360.0 | 1948.3 | 649.0 | 33.3 |
| Mental disorders, September 2023 | Before | 2020–2022 | 2360.0 | 1948.3 | 649.0 | 33.3 |
| | After | 2024–2025 | 4369.0 | 3667.5 | 1069.0 | 29.1 |

CCVD indicates cerebro-cardiovascular disease. Counts are annual means. Fiscal years run from April to March. Decisions are adjudicated claims (approved or denied). The approval proportion is pooled over the period (total approved claims divided by total decisions). The transition years (fiscal year 2021 for CCVD and fiscal year 2023 for mental disorders) are not shown.



**Table 2.** Estimated level changes following each revision, from interrupted time series analysis

| Disease and revision | Claims, RR (95% CI) | Decisions, RR (95% CI) | Approved claims, RR (95% CI) | Approval proportion, OR (95% CI) |
|---|---|---|---|---|
| CCVD, September 2021 | 1.13 (0.93–1.36) | 1.02 (0.84–1.23) | 1.11 (0.93–1.33) | 1.17 (0.90–1.51) |
| Mental disorders, December 2011 | 0.88 (0.74–1.06) | 1.08 (0.97–1.20) | 1.50 (1.28–1.77) | 1.63 (1.34–1.99) |
| Mental disorders, May 2020 | 0.99 (0.85–1.16) | 1.13 (1.03–1.23) | 1.22 (1.06–1.40) | 1.12 (0.94–1.33) |
| Mental disorders, September 2023 | 1.43 (1.26–1.63) | 1.62 (1.50–1.75) | 1.54 (1.37–1.74) | 0.94 (0.81–1.08) |

CCVD indicates cerebro-cardiovascular disease; CI, confidence interval; OR, odds ratio; RR, level ratio (ratio of expected annual counts after vs before the revision, given the linear trend). Estimates are exponentiated coefficients for the postrevision indicators in segmented regression models with a linear time trend (quasi-Poisson models for counts and quasi-binomial models weighted by the number of decisions for the approval proportion). The CCVD models used fiscal years 2009–2025 and excluded fiscal year 2021. The three mental disorder revisions were modeled together over fiscal years 2009–2025, excluding fiscal year 2023. Dispersion estimates (Pearson χ² divided by residual degrees of freedom) for claims, decisions, approved claims, and the approval proportion were 9.5, 7.2, 2.3, and 2.9 for CCVD and 10.6, 3.2, 2.4, and 2.5 for mental disorders. When the model additionally allowed the slope to change from fiscal year 2020, the estimated 2023 level change in claims was 1.00 (95% CI, 0.85–1.18) (Supplementary Table S3).



**Table 3.** Approved claims for cerebro-cardiovascular disease by monthly overtime before and after the 2021 revision (assessment periods combined)

| Outcome | Fiscal years 2009–2020 | Fiscal years 2022–2025 |
|---|---:|---:|
| Approved claims involving <80 overtime hours per month, mean per year | 18.6 | 48.5 |
| Approved claims involving ≥80 overtime hours per month, mean per year | 230.9 | 141.0 |
| Claims approved for short-term overload or extraordinary events, mean per year | 18.9 | 27.5 |
| Share involving <80 overtime hours per month, mean of annual % | 7.0 | 22.5 |

| Analysis | Relative change in the count ratio, fiscal years 2022–2025 vs the prerevision period (95% CI) |
|---|---|
| Primary analysis: <80 h vs ≥80 h (prerevision period, fiscal years 2009–2020) | 4.27 (3.28–5.57) |
| Category-specific linear trends | 3.81 (2.22–6.53) |
| Standard errors clustered by year | 4.27 (2.95–6.20) |
| Category-specific trends and standard errors clustered by year | 3.81 (1.73–8.37) |
| Annual log ratio, OLS with trend and Newey-West standard errors (lag 1) | 3.88 (2.33–6.48) |
| Prerevision period shortened to fiscal years 2015–2020 | 4.54 (3.11–6.63) |
| Each year excluded in turn (16 models), range of estimates | 4.01 to 4.60 |
| Placebo, 4-year windows beginning in fiscal years 2012–2017 (6 models), range of estimates | 0.71 to 1.12 |
| Placebo, pseudo-postrevision periods beginning in fiscal years 2012–2018 (7 models), range of estimates | 0.90 to 1.33 |
| Short-term overload or extraordinary events vs ≥80 h | 2.38 (1.46–3.89) |
| 80–<100 h vs ≥100 h | 0.96 (0.81–1.13) |
| Cardiac vs cerebrovascular disease | 0.98 (0.86–1.11) |

CI indicates confidence interval; OLS, ordinary least squares. Overtime hours are averaged over the applicable assessment period; counts from the 1-month and 2- to 6-month tables are combined. Fiscal year 2021 was excluded. Relative changes are from quasi-Poisson models with year fixed effects unless stated otherwise; the dispersion estimate for the primary model was 1.55. Full results for the excluded-year and placebo models are in Supplementary Tables S5 and S6. The contrast of 80–<100 h vs ≥100 h combines two assessment periods with different thresholds and is not a negative control (see Supplementary Table S7).



**Table 4.** Decisions and approved claims for mental disorders by event group before and after the 2020 and 2023 revisions

| Event group | FY2017–2019, D | A | % | FY2020–2022, D | A | % | FY2024–2025, D | A | % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Harassment, bullying, or assault | 246.7 | 115.3 | 46.8 | 456.7 | 248.7 | 54.5 | 948.5 | 509.5 | 53.7 |
| Other interpersonal conflicts | 385.0 | 25.3 | 6.6 | 561.3 | 25.3 | 4.5 | 1298.5 | 46.0 | 3.5 |
| Workload | 317.3 | 145.7 | 45.9 | 283.7 | 136.3 | 48.1 | 514.0 | 196.5 | 38.2 |
| Accidents and disasters | 176.3 | 88.0 | 49.9 | 218.0 | 120.7 | 55.4 | 267.5 | 144.0 | 53.8 |
| Work failures and excessive responsibility | 129.0 | 33.3 | 25.8 | 126.7 | 34.7 | 27.4 | 196.5 | 55.0 | 28.0 |
| Changes in role or position | 125.3 | 25.3 | 20.2 | 136.3 | 24.0 | 17.6 | 273.0 | 42.0 | 15.4 |
| Special events | 60.3 | 60.3 | 100.0 | 59.3 | 59.3 | 100.0 | 76.5 | 76.0 | 99.3 |
| Other event category | 90.7 | 0.0 | 0.0 | 106.3 | 0.0 | 0.0 | 93.0 | 0.0 | 0.0 |
| All claims | 1530.7 | 493.3 | 32.2 | 1948.3 | 649.0 | 33.3 | 3667.5 | 1069.0 | 29.1 |

| Relative change in the count ratio | After the 2020 revision (95% CI) | Further change after the 2023 revision (95% CI) |
|---|---|---|
| Approved claims: harassment group vs all other groups | 2.04 (1.67–2.48) | 1.47 (1.25–1.72) |
| Decisions: other interpersonal conflicts vs all other groups | 1.20 (1.04–1.39) | 1.35 (1.20–1.53) |

A indicates mean annual approved claims; CI, confidence interval; D, mean annual decisions; FY, fiscal year; %, approved claims as a percentage of decisions, pooled over the period (total approved claims divided by total decisions). Each decided claim is assigned to one event in the source tables. The harassment group comprises power harassment involving a power imbalance (item added in June 2020), assault or severe bullying or harassment (before June 2020, "[severe] harassment, bullying, or assault"), sexual harassment, and serious misconduct by customers or clients (item added in September 2023). Other interpersonal conflicts are trouble with a superior, coworker, or subordinate and changes in workplace relationships. Workload comprises changes in the quantity or quality of work, overtime of ≥80 h per month, consecutive work for ≥2 weeks, and related items. Special events are events with extreme psychological stress or extremely long working hours. Relative changes are from quasi-Poisson models with year fixed effects for fiscal years 2017–2025, excluding fiscal year 2023 as a transition year; dispersion estimates were 1.68 and 2.82. Annual counts are given in Supplementary Table S9.



## Figure legends

**Fig. 1.** Approved claims for cerebro-cardiovascular disease by monthly overtime, Japan, fiscal years (FY) 2009–2025. A, Approved claims involving ≥80 and <80 h of average monthly overtime and claims approved for short-term overload or extraordinary events; the 1-month and 2- to 6-month assessment periods are combined. B, Share of approved claims involving <80 h; dotted lines show the means for FY2009–2020 and FY2022–2025. The dashed line marks the revision of September 2021. FY2021 was a transition year.

**Fig. 2.** Approved claims for cerebro-cardiovascular disease by assessment period, Japan. A, Approved claims by assessment period and monthly overtime, fiscal years (FY) 2017–2025; solid lines represent claims assessed over 2 to 6 months (threshold, about 80 h per month), and dashed lines represent claims assessed over 1 month (threshold, about 100 h). B, Postrevision change in the ratio of approved-claim counts between categories, estimated using quasi-Poisson models with year fixed effects. Orange, contrasts in which the numerator is a category below a threshold or claims approved for short-term overload or extraordinary events; blue, other contrasts. Comparisons marked with an asterisk use the separate assessment-period tables and compare FY2022–2025 with FY2017–2020. Unmarked comparisons compare FY2022–2025 with FY2009–2020; overtime-category counts are combined across assessment periods, whereas the cardiac-versus-cerebrovascular contrast uses disease-type counts.

**Fig. 3.** Workers' compensation for mental disorders, Japan. A, Claims, decisions, and approved claims, fiscal years (FY) 2009–2025. B, Approved claims as a percentage of decisions, overall and for claims involving suicide or attempted suicide. C, Approved claims by monthly overtime category, FY2017–2025; labels show the percentage in the "Other" category (claims described in the annual reports as judged work-related without an investigation of working hours; see Methods). Dashed lines mark the beginning of FY2020 and of FY2024; FY2023 was treated as a transition year. D, Mean time from claim filing to decision, in days, FY2009–2024; the dotted line indicates the 8-month standard processing period (about 240 d). In panels A, B, and D, dashed lines mark the revisions notified in December 2011, May 2020 (applied from June 1, 2020), and September 2023.

