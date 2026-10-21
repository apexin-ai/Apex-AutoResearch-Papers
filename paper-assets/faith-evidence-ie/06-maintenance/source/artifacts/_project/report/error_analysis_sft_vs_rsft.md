# SFT→RSFT Error Analysis Comparison

Remote outputs:
- SFT: /root/autodl-tmp/analysis/error_analysis_sft/
- RSFT d102 k=1: /root/autodl-tmp/analysis/error_analysis_d102_k1/
- RSFT plan006 k=3: /root/autodl-tmp/analysis/error_analysis_plan006_k3/
- Full report: /root/autodl-tmp/analysis/error_analysis_comparison_report.md

## Three Improvement Mechanisms (consistent across scales)

1. **Truncation FN -16-22%** (largest): RSFT teaches compact output, reduces truncation loss. 1.7B: -841 FN
2. **Hallucinated FP -6-12%**: Rejection training reduces hallucination. LLaMA: -593 FP (-11.8%)
3. **Duplicates -11-20%**: Format regularization side-effect. 1.7B: -20.2%

## Unchanged
- Evidence quality: exact match change <0.4pp
- Relation confusion FP: stable (except LLaMA -11.4%)
- Rare relation FN: stable

## k=1 vs k=3
- 1.7B + LLaMA: k=1 better
- 8B: k=3 slightly better (+0.57 Ign-F1)

## Connection to Evidence Tax Analysis
Truncation and duplication mechanisms align with evidence_tax_analysis.md findings:
- 1.7B duplication 60.5%→33.0% with evidence (evidence_tax) ↔ RSFT duplicates -20.2% (error_analysis)
- 1.7B truncation 50.9%→31.9% with evidence ↔ RSFT truncation FN -22%
