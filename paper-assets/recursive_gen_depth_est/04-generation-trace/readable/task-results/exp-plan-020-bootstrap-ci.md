# exp plan 020 bootstrap ci

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_020_bootstrap_ci_20260517T140847_result.json`
- **Structured JSON:** [`70ed1638ccdf6db01813.json`](../../sessions/70/70ed1638ccdf6db01813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册。验证结果与 registry point estimates 的一致性：

**验证通过** - Bootstrap mean 与 point estimates 完全一致：

| Cell | RF Acc | RF 95% CI | LR Acc | LR 95% CI |
|---|---|---|---|---|
| pythia_nucleus095 | 0.787 | [0.782, 0.792] | 0.753 | [0.748, 0.758] |
| pythia_temp09 | 0.767 | [0.762, 0.773] | 0.742 | [0.736, 0.747] |
| pythia_topk50 | 0.688 | [0.682, 0.694] | 0.677 | [0.671, 0.682] |
| gpt2xl_nucleus095 | 0.841 | [0.836, 0.846] | 0.817 | [0.812, 0.822] |
| gpt2xl_temp09 | 0.859 | [0.854, 0.863] | 0.813 | [0.808, 0.818] |
| gpt2xl_topk50 | 0.759 | [0.754, 0.765] | 0.712 | [0.706, 0.718] |
| olmo_nucleus095 | 0.789 | [0.784, 0.795] | 0.763 | [0.757, 0.768] |
| olmo_temp09 | 0.821 | [0.816, 0.826] | 0.814 | [0.809, 0.819] |
| olmo_topk50 | 0.745 | [0.740, 0.750] | 0.749 | [0.744, 0.754] |

**关键观察：**
- CI 宽度 ~1.0-1.2pp（accuracy），~1.3-2.0pp（AUC），合理
- RF > LR 在 8/9 cells，唯一例外 olmo_topk50（LR 0.749 vs RF 0.745，CI 重叠）
- 最佳 cell: gpt2xl_temp09 RF 85.9% [85.4, 86.3]
- 最难 cell: pythia_topk50 RF 68.8% [68.2, 69.4]
- d1v2 AUC 一致 > d2v3 AUC（深层递归区分越来越难）

产出：`artifacts/bootstrap_ci_table1.json`（远程服务器 + artifact registry `art_20260517_64defb`）

---
