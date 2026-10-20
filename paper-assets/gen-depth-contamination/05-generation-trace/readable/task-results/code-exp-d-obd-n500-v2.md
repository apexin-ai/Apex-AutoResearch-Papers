# code exp D obd n500 v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_D_obd_n500_v2_20260515T104206_result.json`
- **Structured JSON:** [`3c9f5da4ee6db47ead94.json`](../../sessions/3c/3c9f5da4ee6db47ead94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 方法 | N=500 Accuracy | 95% CI |
|------|---------------|--------|
| **OBD-LightGBM** | **0.380** | [0.340, 0.424] |
| GPT-5.5 | 0.332 | — |
| Claude | 0.331 | — |

验证通过：
- Full OBD accuracy = 0.3856，与 exp-010 报告的 0.3856 完全一致（复现成功）
- N=500 子集 accuracy = 0.380，在合理范围内（接近 full 的 0.386，且 CI 覆盖此值）
- 所有 500 个样本均匹配成功
- 使用了正确的 OBD 方法（K-1 binary classifiers），不是 plain multiclass
- 超参数与 exp-010 一致（n_estimators=200, max_depth=6, num_leaves=31）

输出已保存到 `artifacts/exp_D_obd_n500_v2.json`，脚本在 `scripts/exp_D_obd_n500_v2.py`。

---
