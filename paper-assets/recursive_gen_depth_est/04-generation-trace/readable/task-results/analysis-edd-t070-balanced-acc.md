# analysis edd t070 balanced acc

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edd_t070_balanced_acc_20260518T142916_result.json`
- **Structured JSON:** [`64ef75a6ab73d28563f2.json`](../../sessions/64/64ef75a6ab73d28563f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果文件已正确生成。以下是汇总：

---

## Task A: EDD at T=0.70

**9-Cell (4-class d0-d3):**

| Cell | d1v2 | d2v3 | EDD@.70 | EDD@.75 |
|------|------|------|---------|---------|
| pythia_nucleus | 0.8607 | 0.8005 | 3 | 3 |
| pythia_temp09 | 0.8327 | 0.7928 | 3 | 3 |
| pythia_topk50 | 0.7518 | 0.6918 | **2** | 2 |
| olmo_nucleus | 0.8673 | 0.8124 | 3 | 3 |
| olmo_temp09 | 0.9010 | 0.8214 | 3 | 3 |
| olmo_topk50 | 0.8305 | 0.7357 | **3** | **2** |
| gpt2xl_nucleus | 0.9131 | 0.8829 | 3 | 3 |
| gpt2xl_temp09 | 0.9367 | 0.8815 | 3 | 3 |
| gpt2xl_topk50 | 0.8259 | 0.7708 | 3 | 3 |

- T=0.70: **8/9 cells EDD=3**, mean=2.89
- T=0.75: **7/9 cells EDD=3**, mean=2.78
- 降低阈值多收回 olmo_topk50 (d2v3=0.7357 介于 0.70-0.75 之间)

**Depth Extension (binary classifiers, d1-d5):**

| Model | d3v4 | d4v5 | EDD@.70 | EDD@.75 |
|-------|------|------|---------|---------|
| Pythia | 0.7837 | 0.6832 | 4 | 4 |
| GPT-2 XL | 0.7501 | 0.6805 | 4 | 4 |
| OLMo | 0.7649 | 0.6843 | 4 | 4 |

**3/3 models EDD=4 at T=0.70**，与 T=0.75 完全一致（d3v4 已 >= 0.75, d4v5 仍 < 0.70）。

---

## Task B: d1-d3 Balanced Accuracy

**Within-Distribution (9-cell mean):** **0.7109**
- 最高: gpt2xl_temp09 = 0.8053
- 最低: pythia_topk50 = 0.5845

**Cross-Model Transfer (LOO mean):** **0.5544**
- Holdout Pythia: 0.4990
- Holdout OLMo: 0.5920
- Holdout GPT-2 XL: 0.5723

**最弱 d2 recall:**
- Within-distribution: pythia_topk50 = 0.4560
- Cross-model: holdout Pythia = **0.2677** (overall minimum)

---

产出文件:
- `results/reviewer_metrics/edd_t070.json`
- `results/reviewer_metrics/d1d3_balanced_acc.json`

---
