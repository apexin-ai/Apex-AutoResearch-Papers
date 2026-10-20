# ops check ckpt3600 mutation result

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-ckpt3600-mutation-result_20260515T233318_result.json`
- **Structured JSON:** [`734cbc62c2b347a5fb6d.json`](../../sessions/73/734cbc62c2b347a5fb6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## ckpt-3600 Mutation Breakdown Eval 结果

**Overall (9784 test samples, unparseable=0)**

| Metric | Value |
|--------|-------|
| Accuracy | **84.48%** |
| F1_macro | **78.17%** |
| F1_fail / F1_pass | 66.43% / 89.91% |
| Precision_fail / Precision_pass | 80.06% / 85.53% |
| Recall_fail / Recall_pass | 56.76% / 94.76% |
| Majority baseline | 72.96% |
| Gap vs majority | +11.53pp |

**Per-Mutation-Type Accuracy**

| Mutation Type | Correct | Total | Accuracy |
|---------------|---------|-------|----------|
| gold (no mutation) | 4459 | 4633 | **96.24%** |
| off_by_one | 159 | 183 | **86.89%** |
| operator_swap | 2732 | 3357 | **81.38%** |
| return_value | 424 | 562 | **75.44%** |
| boundary_removal | 492 | 1049 | **46.90%** |

注意：test set 中无 `variable_swap` 类型样本（只有 4 种 mutation + gold）。

**boundary_removal 是明显短板**（46.9%），模型对边界条件移除的判别能力弱；off_by_one 反而最好（86.9%）。

---

**Registry**: `cls8b-s42-resume-ckpt3600-mutation` → DONE/success，metrics 含完整 per-mutation breakdown

**Cron**: 本 session 无活跃 cron，无需删除

**cuda:1 已空闲** — GPU 0/1 均 0 MiB 占用，可用于 CWM 4B seed123 训练。GPU 2/3 仍在占用中。

---
