# code plan 033 subject dif concentration

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_033_subject_dif_concentration_20260521T133500_result.json`
- **Structured JSON:** [`4202786b2dc389dded28.json`](../../sessions/42/4202786b2dc389dded28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

57 subjects in both CSVs (58 lines = 57 + header). All outputs validated. Key results:

**DIF concentration across subjects:**
- All 57 subjects have C-flagged items; range 20.7%–48.4%, mean 30.6%, SD 5.5%
- Highest: business_ethics (48.4%), human_aging (41.9%), formal_logic (40.4%)
- Lowest: computer_security (20.7%), marketing (20.9%)

**Domain differences:**
- STEM 30.9%, Humanities 31.1%, Social Science 31.6% — **no significant difference** (Kruskal-Wallis p=0.78)
- DIF distributes across domains, not concentrated in one

**Predictive model:**
- Higher discrimination → much higher DIF odds (OR=57.2, p<10⁻¹⁰⁰)
- Higher difficulty → much lower DIF odds (OR=0.086, p<10⁻¹⁰⁴)
- Pseudo R²=0.04 — item properties explain little, consistent with DIF being content-driven
- 5 subjects (professional_law, human_aging, world_religions, business_ethics, professional_medicine) show significantly **more** DIF than predicted by item properties alone

**Temporal asymmetry — the most striking finding:**
- STEM DIF items lean 55.4% toward favoring 2024 models (mean_delta_mh positive)
- Humanities DIF items lean 64.4% toward favoring 2023 models (mean_delta_mh negative)
- world_religions (83% favor 2023) and logical_fallacies (80% favor 2023) show near-unidirectional asymmetry
- This STEM↔Humanities directional split answers Q4 directly: the **direction** of DIF is domain-dependent even though the **rate** is not

---
