# paper writing experiments d095

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_d095_20260522T043542_result.json`
- **Structured JSON:** [`27adc6228debab627d50.json`](../../sessions/27/27adc6228debab627d50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

2 tables + 3 figures = 5 floats. All labels, citations, and appendix references are correct. 

Summary of the complete `experiments.tex` rewrite:

- **6 subsections**: Setup, OpenVLA deep dive, R² exit collapse, counterfactual sensitivity, L1 priors, three-tier gradient
- **5 floats** (2 tables + 3 placeholder figures): `tab_cross_arch_matrix`, `tab_counterfactual`, `fig_r2_collapse`, `fig_cross_arch_l1`, `fig_three_tier`
- **All numbers verified** against `matrix_summary_table.md`
- **D096 qualification** correctly framed: exit collapse at VLM-to-VLA (6/6) vs VLA-to-VLA (1/3)
- **Style rules enforced**: no em-dashes, no -ing phrase endings, no banned words, booktabs only, `\centering` not `\begin{center}`, self-contained captions
- **Old floats removed** from main text (tab_dense_routing_main, tab_routing_gradient, tab_rsa_overview, fig_attention_profile, fig_layer_curves, fig_dose_response all moved to appendix references)

---
