# exp xgb lgbm 3cell consistent

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_xgb_lgbm_3cell_consistent_20260515T194731_result.json`
- **Structured JSON:** [`387249281614e445e687.json`](../../sessions/38/387249281614e445e687.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**实验 `xgboost_lgbm_3cell_001`** — 3 cell × 3 classifier 统一评估

| Cell | RF | XGBoost | LightGBM | d1v2 AUC | d2v3 AUC |
|------|-----|---------|----------|----------|----------|
| **gpt2xl_temp09** | 85.8% | **86.2%** | 86.2% | 0.980 | 0.886 |
| **pythia_nucleus095** | 78.8% | **79.0%** | 78.9% | 0.931 | 0.816 |
| **pythia_topk50** | 68.9% | **68.9%** | 68.7% | 0.841 | 0.689 |

核心结论：
1. **评估协议一致性已修复** — 旧 RF d0v1 AUC=0.861 是评估 bug，统一后 RF d0v1=0.9996，与 XGBoost 0.9999 一致
2. **三种分类器每个 cell 内差距 ≤0.5pp** — 信号天花板在 19 维特征，非分类器选择
3. **d2 recall 持续最低**（43-73%），跨所有 cell 和分类器一致，是特征层面的限制
4. 脚本：`src/xgb_lgbm_3cell.py`，结果：`results/xgb_lgbm_3cell/results.json`

---
