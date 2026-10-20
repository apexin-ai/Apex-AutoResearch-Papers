# Rohingya Corpus Real-Data Feasibility

Date: 2026-05-31
Target: C_REALDATA_FEASIBILITY
Plan: plan_004_realdata_feasibility
Verdict: 部分可支撑

## 判定

Rohingya/Bengali host interview corpus can partially support EC-HTE real-data validation. It supports a differential-misclassification feasibility study if anonymized transcripts and record-level expert/LLM labels are obtained from the authors or World Bank. Public-only reproduction is not currently supported, because transcripts are not publicly downloadable and record-level expert labels, LLM labels, and split IDs were not found in the public repository.

## Evidence Matrix

| Field | Status | Evidence |
|---|---|---|
| Data availability | Partial | Article data availability states code is public at https://github.com/worldbank/iQual, interview transcripts cannot be public for privacy, and an anonymized version will be available on request. DOI: https://doi.org/10.1177/00491241251338246. |
| Schema | Partial | Paper reports 2,407 open-ended interviews, 32,463 QA pairs, baseline household/adult survey variables, and 19 main code labels from a coding tree. DOI: https://doi.org/10.1177/00491241251338246. |
| Text | Partial | Interviews were conducted in Bengali/Rohingya dialect, transcribed into Bengali, translated to English by Google Translate, and manually corrected for coding; raw text requires request due privacy. DOI: https://doi.org/10.1177/00491241251338246. |
| LLM annotation | Supported by method, not by public labels | Paper documents GPT-3.5-turbo, GPT-4o mini, Llama-2 13B, and Llama-3 8B annotation with code-specific few-shot and chain-of-thought prompts; record-level labels were not located in the GitHub tree. DOI: https://doi.org/10.1177/00491241251338246; repo: https://github.com/worldbank/iQual. |
| Expert labels | Partial | 789 transcripts were human-coded in Atlas.ti by two annotators with reviewer resolution, from 400 R2 and 400 R3 sampled interviews minus 11 unannotated cases; public record-level labels were not found. DOI: https://doi.org/10.1177/00491241251338246. |
| Subgroup variables | Supported in paper; data linkage pending | Required variables are explicitly used: refugee status, eldest child's gender, and parent's years of education. Quantitative table also reports refugee status, female eldest child, female household head, parent education, and related variables. DOI: https://doi.org/10.1177/00491241251338246. |
| Split | Partial / 待核验 | Paper reports R2/R3 sampling, an 80/20 train/test split and 3-fold CV for iQual modeling, but public split IDs for expert/LLM validation were not found. DOI: https://doi.org/10.1177/00491241251338246. |
| License / IRB | Partial / 待核验 | iQual code license is MIT: https://github.com/worldbank/iQual/blob/main/LICENSE.md. Public CBPS baseline Dataverse metadata reports CC0 1.0 for baseline survey DOI https://doi.org/10.7910/DVN/V614VB. Interview transcript license, data-use terms, and IRB/consent constraints remain 待核验. |

## Feasibility For EC-HTE

可支撑:
- Differential LLM misclassification analysis by respondent characteristics, because the paper explicitly tests whether LLM prediction errors are associated with subject characteristics including refugee status, gender, and education. DOI: https://doi.org/10.1177/00491241251338246; World Bank summary: https://documents1.worldbank.org/curated/en/099348304162431121/pdf/IDU1271bc2541c5e8144f51b8cc1be231f985cc6.pdf.
- Leave-expert-out or budget subsampling design in principle, because 789 expert-coded transcripts exist and the code labels are binary at QA/interview level. DOI: https://doi.org/10.1177/00491241251338246.

部分可支撑:
- Reproducing schema and subgroup covariates from public sources, because the CBPS baseline/HFT public data describe host/camp status and household/individual variables, but linkage to restricted transcripts and coded labels must be obtained. Yale CBPS page: https://macmillan.yale.edu/refugee/coxs-bazar-panel-survey; World Bank HFT DOI: https://doi.org/10.48529/2zfw-ht33.
- LLM annotation reproduction, because prompts and method are described in the paper/supplement, but exact record-level LLM outputs are not in the public iQual repository as checked via GitHub API on 2026-05-31. Repo: https://github.com/worldbank/iQual.

暂不可支撑:
- Public-only real-data experiment with auditable unit-level confusion matrices, because raw/anonymized transcripts, expert labels, LLM labels, and split IDs are not currently public. Source: data availability statement in https://doi.org/10.1177/00491241251338246.
- Any causal accuracy claim such as real-data PEHE/GATE RMSE, because the corpus supplies annotation labels and respondent covariates, not ground-truth treatment effects. Source: project scope plus corpus description in https://doi.org/10.1177/00491241251338246.

## Matrix Provenance

```yaml
- target_id: C_REALDATA_FEASIBILITY
  row: rohingya_corpus
  col: fields_and_label_sources
  metric_key: data_schema_summary
  exp_id: null
  source: "partial_support: public paper documents 2,407 interviews, 32,463 QA pairs, binary QA/interview code labels, 789 expert-coded transcripts, and LLM annotation methods; raw transcripts and record-level labels require request. DOI https://doi.org/10.1177/00491241251338246; repo https://github.com/worldbank/iQual"
- target_id: C_REALDATA_FEASIBILITY
  row: rohingya_corpus
  col: expert_split_available
  metric_key: expert_split_status
  exp_id: null
  source: "partial_support_pending_access: expert-coded sample and train/test/CV design are described, but public split IDs and record-level labels were not found. DOI https://doi.org/10.1177/00491241251338246"
- target_id: C_REALDATA_FEASIBILITY
  row: rohingya_corpus
  col: subgroup_variables_available
  metric_key: subgroup_variable_coverage
  exp_id: null
  source: "support_for_variables_pending_linkage: refugee status, eldest-child gender, and parent education are explicitly used in the paper; public CBPS survey metadata supports host/camp and household/individual variables, but transcript-label linkage requires restricted/anonymized data access. DOI https://doi.org/10.1177/00491241251338246; CBPS https://macmillan.yale.edu/refugee/coxs-bazar-panel-survey; HFT DOI https://doi.org/10.48529/2zfw-ht33"
```

