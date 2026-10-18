# experiment plan 005 cross model loo detailed

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_plan_005_cross_model_loo_detailed_20260515T050435_result.json`
- **Structured JSON:** [`77b9a311df1576112696.json`](../../sessions/77/77b9a311df1576112696.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**4-class (d0-d3)**

| Rotation | Acc | 95% CI | d1v2 AUC | d2v3 AUC |
|---|---|---|---|---|
| Hold-out Pythia | 0.6242 | [0.621, 0.628] | 0.562 | 0.653 |
| Hold-out OLMo | 0.6921 | [0.688, 0.696] | 0.769 | 0.686 |
| Hold-out GPT-2 XL | 0.6756 | [0.672, 0.680] | 0.816 | 0.664 |
| **Mean** | **0.664** | | | |

**3-class (d1-d3 only)**

| Rotation | Acc | 95% CI |
|---|---|---|
| Hold-out Pythia | 0.499 | [0.494, 0.503] |
| Hold-out OLMo | 0.592 | [0.587, 0.597] |
| Hold-out GPT-2 XL | 0.572 | [0.568, 0.577] |
| **Mean** | **0.554** | |

**Per-class mean recall (4-class)**：d0=0.993, d1=0.665, **d2=0.409** (最低，符合预期), d3=0.590

Artifact 已注册 (`cross_model_loo_detailed`)，`cross_model_loo_v1` registry metrics 已更新。完整 JSON 在服务器 `results/cross_model_loo_detailed.json`。

---
