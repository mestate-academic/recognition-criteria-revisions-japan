# -*- coding: utf-8 -*-
"""Mental disorders: decisions and approved claims by event (annual report Table 2-8), FY2017-2025.

Every value is (decisions, approved claims). Sources (MHLW, Status of workers' compensation for karoshi
and other overwork-related disorders, Table 2-8 unless stated):
  FY2017, FY2018 : FY2018 edition  https://www.mhlw.go.jp/content/11601000/000577651.pdf (p. 26)
  FY2019         : White paper on measures to prevent karoshi, 2020 edition, Table 1-23 (FY2018 and FY2019)
                   https://www.mhlw.go.jp/wp/hakusyo/karoushi/20/dl/hakusho-zentai.pdf (PDF p. 59; FY2018 column
                   agrees with the FY2018 edition)
  FY2020         : Material 2, 1st meeting of the expert committee (Dec 2021), section 7
                   https://www.mhlw.go.jp/content/11201000/000862995.pdf
  FY2021         : FY2022 edition  https://www.mhlw.go.jp/content/11402000/001269207.pdf (2020 item list)
  FY2022, FY2023 : FY2023 edition  https://www.mhlw.go.jp/content/11402000/001276199.pdf (2023 item list; FY2022 is
                   restated on the 2023 list). FY2023 agrees with the FY2024 edition
                   https://www.mhlw.go.jp/content/11402000/001704309.pdf
  FY2024, FY2025 : FY2025 edition  https://www.mhlw.go.jp/content/11402000/001723467.pdf (FY2024 agrees with the
                   FY2024 edition)
Checks: for every year the items sum to the published totals of decisions and approved claims (Table 2-1),
i.e., each claim is assigned to exactly one event. FY2022 is also available on the 2020 item list (FY2022 edition);
group totals on the two lists differ by at most 3 decisions and 0 approved claims.
Groups used in the analysis (constant across item lists):
  harassment = power harassment (item added June 2020) + assault/severe bullying/harassment (before 2020:
               "(severe) harassment, bullying, or assault") + sexual harassment + serious misconduct by customers
               (item added September 2023)
  conflict   = other interpersonal-relations items (trouble with a superior, coworker or subordinate; changes in
               workplace relationships)
  workload   = type 3 (quantity and quality of work, including overtime of >=80 h per month and >=2 weeks of
               consecutive work)
  accident   = type 1; failure = type 2; role = type 4; special = "special events"; none = "other" (no assessable event)
"""
import pandas as pd
OLD = dict(
 accident=['illness_injury','witnessed_accident'],
 failure=['caused_accident','serious_error','held_responsible','large_loss','forced_illegal','hard_quota','quota_unmet',
          'new_project','unreasonable_order','customer_complaint','forced_presentation','covered_for_superior'],
 workload=['workload_change','overtime_80h','consecutive_2wk','work_pattern_change','pace_change'],
 role=['forced_resign','reassignment','relocation','sole_charge','nonregular_discrimination','promotion',
       'fewer_subordinates','early_retirement','contract_expiry'],
 interpersonal=['bullying_assault','trouble_superior','trouble_coworker','trouble_subordinate','supporter_moved',
                'superior_changed','passed_over'])
NEW = dict(
 accident=['illness_injury','witnessed_accident'],
 failure=['caused_accident','serious_error','held_responsible','forced_illegal','hard_quota','new_project',
          'difficult_order','covered_for_others'],
 workload=['workload_change','overtime_80h','consecutive_2wk','infection_risk','work_pattern_change'],
 role=['forced_resign','reassignment_relocation','sole_charge','unfavourable_treatment','promotion','contract_expiry'],
 interpersonal=['bullying_assault','trouble_superior','trouble_coworker','trouble_subordinate','customer_misconduct',
                'relationship_change'])
N=None
D = {
2017:('old',dict(accident=[(86,26),(99,63)],
 failure=[(10,6),(24,8),(5,1),(2,0),(12,3),(13,1),(10,2),(8,5),(6,2),(34,4),(0,0),(1,0)],
 workload=[(185,64),(61,41),(71,48),(3,1),(2,0)],
 role=[(34,5),(67,11),(11,3),(5,0),(3,0),(5,1),(2,1),(0,0),(0,0)],
 interpersonal=[(186,88),(320,22),(67,1),(2,0),(3,1),(2,0),(3,0)],
 power_harassment=N, sexual_harassment=(64,35), special=(63,63), none=(76,0)), (1545,506)),
2018:('old',dict(accident=[(86,36),(92,56)],
 failure=[(5,2),(26,4),(12,4),(1,1),(9,2),(14,4),(9,1),(12,3),(13,2),(21,5),(2,0),(2,1)],
 workload=[(181,69),(68,45),(43,25),(8,0),(3,1)],
 role=[(19,3),(54,8),(21,7),(9,2),(7,1),(8,2),(2,1),(0,0),(3,0)],
 interpersonal=[(178,69),(255,18),(69,2),(18,3),(5,0),(2,0),(1,0)],
 power_harassment=N, sexual_harassment=(54,33), special=(55,55), none=(94,0)), (1461,465)),
2019:('old',dict(accident=[(72,28),(94,55)],
 failure=[(10,5),(21,7),(9,5),(4,0),(12,1),(19,4),(6,1),(11,5),(11,4),(29,5),(1,0),(3,2)],
 workload=[(207,68),(54,32),(63,42),(1,1),(2,0)],
 role=[(26,6),(55,13),(14,5),(10,5),(12,2),(4,0),(1,0),(1,0),(3,0)],
 interpersonal=[(174,79),(294,21),(91,5),(13,1),(5,1),(5,1),(0,0)],
 power_harassment=N, sexual_harassment=(84,42), special=(63,63), none=(102,0)), (1586,509)),
2020:('old',dict(accident=[(127,50),(120,83)],
 failure=[(7,2),(27,6),(9,4),(0,0),(8,4),(16,1),(3,0),(9,3),(9,0),(42,11),(0,0),(4,0)],
 workload=[(190,58),(52,31),(64,41),(1,0),(3,0)],
 role=[(19,5),(63,6),(21,5),(12,4),(11,3),(4,0),(0,0),(1,0),(2,0)],
 interpersonal=[(128,71),(388,14),(89,7),(16,2),(2,0),(0,0),(1,0)],
 power_harassment=(180,99), sexual_harassment=(90,44), special=(54,54), none=(134,0)), (1906,608)),
2021:('old',dict(accident=[(89,32),(100,66)],
 failure=[(6,3),(27,6),(6,2),(0,0),(16,8),(17,3),(9,2),(2,0),(5,2),(30,4),(4,0),(1,0)],
 workload=[(183,71),(36,28),(52,39),(4,2),(1,0)],
 role=[(34,9),(69,9),(13,2),(4,3),(11,2),(7,2),(2,0),(0,0),(6,0)],
 interpersonal=[(126,61),(451,17),(118,6),(15,1),(2,1),(1,0),(0,0)],
 power_harassment=(242,125), sexual_harassment=(97,60), special=(63,63), none=(104,0)), (1953,629)),
2022:('new',dict(accident=[(94,42),(124,89)],
 failure=[(11,7),(29,8),(10,6),(7,3),(22,7),(9,3),(33,8),(2,1)],
 workload=[(180,78),(27,21),(53,38),N,(5,2)],
 role=[(26,6),(78,12),(6,2),(18,2),(2,0),(0,0)],
 interpersonal=[(148,73),(475,23),(107,1),(12,4),N,(7,0)],
 power_harassment=(257,147), sexual_harassment=(102,66), special=(61,61), none=(81,0)), (1986,710)),
2023:('new',dict(accident=[(126,47),(154,111)],
 failure=[(12,3),(46,12),(13,4),(23,7),(17,4),(10,3),(35,11),(4,2)],
 workload=[(265,100),(61,35),(52,33),(11,2),(6,0)],
 role=[(38,9),(88,18),(18,5),(15,0),(11,2),(4,0)],
 interpersonal=[(118,59),(599,21),(143,7),(25,5),(83,52),(4,0)],
 power_harassment=(289,157), sexual_harassment=(156,103), special=(71,71), none=(86,0)), (2583,883)),
2024:('new',dict(accident=[(101,48),(145,87)],
 failure=[(20,8),(41,9),(25,9),(29,6),(23,8),(16,7),(29,10),(7,1)],
 workload=[(359,120),(88,51),(52,36),(10,2),(11,1)],
 role=[(67,18),(132,21),(13,5),(27,2),(16,2),(12,1)],
 interpersonal=[(101,44),(953,38),(217,4),(34,3),(207,108),(7,0)],
 power_harassment=(389,224), sexual_harassment=(191,105), special=(79,78), none=(95,0)), (3496,1056)),
2025:('new',dict(accident=[(125,43),(164,110)],
 failure=[(13,1),(46,11),(13,6),(28,9),(18,4),(25,6),(44,11),(16,4)],
 workload=[(353,113),(90,40),(44,30),(8,0),(13,0)],
 role=[(61,11),(136,12),(18,6),(35,1),(18,5),(11,0)],
 interpersonal=[(133,62),(1061,36),(257,5),(56,6),(240,127),(12,0)],
 power_harassment=(403,222), sexual_harassment=(233,127), special=(74,74), none=(91,0)), (3839,1082)),
}
HAR={'bullying_assault','customer_misconduct','power_harassment','sexual_harassment'}
rows=[]
for fy,(lst,d,tot) in D.items():
    names=OLD if lst=='old' else NEW
    for typ in ['accident','failure','workload','role','interpersonal']:
        assert len(d[typ])==len(names[typ]),(fy,typ)
        for nm,v in zip(names[typ],d[typ]):
            if v is None: continue
            g='harassment' if nm in HAR else ('conflict' if typ=='interpersonal' else typ)
            rows.append((fy,lst,typ,nm,g,v[0],v[1]))
    for nm in ['power_harassment','sexual_harassment','special','none']:
        v=d[nm]
        if v is None: continue
        g='harassment' if nm in HAR else nm
        rows.append((fy,lst,nm,nm,g,v[0],v[1]))
    s=[sum(r[5] for r in rows if r[0]==fy),sum(r[6] for r in rows if r[0]==fy)]
    assert tuple(s)==tot,(fy,s,tot)
E=pd.DataFrame(rows,columns=['fy','item_list','type','item','group','decisions','approvals'])
nat=pd.read_csv('data/mental_national.csv').set_index('fy')
for fy,g in E.groupby('fy'):
    assert g.decisions.sum()==nat.loc[fy,'decisions'] and g.approvals.sum()==nat.loc[fy,'approvals'],fy
E.to_csv('data/mental_events.csv',index=False)
print('mental_events.csv written:',len(E),'rows; totals agree with mental_national.csv for FY2017-2025')
