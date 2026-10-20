# code mvp sva gpt2 k3

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-sva-gpt2-k3_20260513T055713_result.json`
- **Structured JSON:** [`38576d11dc2098ebde6c.json`](../../sessions/38/38576d11dc2098ebde6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE, artifact registered. Here's the final report:

---

## mvp_sva_gpt2_k3 — Complete

**Gate Verdict: PASS_MAIN** | Off-diagonal: **91.8%** [89.9%, 93.4%]

### Key Metrics (Mean Ablation)
| Circuit | Edges | CPR | CMD |
|---------|-------|-----|-----|
| **stable_core** | **80** | **1.177** | **0.540** |
| css_1.00 | 46 | 1.174 | 0.532 |
| css_0.67 | 46 | 1.174 | 0.532 |
| method_edge_pruning | 100 | 1.168 | 0.514 |
| method_eap_ig | 100 | 1.168 | 0.513 |
| css_0.33 | 153 | 1.165 | 0.506 |
| method_acdc | 100 | 1.162 | 0.495 |
| circus_core | 975 | 0.994 | 0.017 |

### Cross-Method Agreement
- CSS distribution: 52 (0.33) / 55 (0.67) / **46 (1.00)**
- 3-way Jaccard: **0.301** (46/153)
- Pairwise: EAP-IG×EP=0.65, ACDC×EP=0.43, ACDC×EAP-IG=0.37

### Deliverables
- **Script**: `/root/min_necessary_circuit_css/run_sva.py`
- **Dataset**: 500 auto-generated SVA prompts
- **ACDC binarization**: top-100 confirmed (NOT isinf)
- **Runtime**: ~1h50m (ACDC 5-threshold sweep dominated)
- **Server**: cqa1-21977, GPU cuda:5
- **Results**: `/root/min_necessary_circuit_css/sva_results.json`

### D025 Score: IOI PASS + Arithmetic FAIL + **SVA PASS** = 2/3 conditions met

---
