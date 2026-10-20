# diagnose nli large paper discrepancy

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_nli-large-paper-discrepancy_20260522T161220_result.json`
- **Structured JSON:** [`65c26414500b2cb8405c.json`](../../sessions/65/65c26414500b2cb8405c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已完整。诊断结论如下：

## 诊断结果：+1.10pp 是正确的

**analysis.tex L8 的 +1.10pp 没有错误。** 问题出在 Reviewer 对比了错误的 baseline 数字。

### 精确数据溯源

论文在 appendix.tex L48 明确写了对比方式：

> yields only +1.10pp Ign-F1 (**45.33** vs. **44.23**, s42)

这是 **same-seed (s42) 对比**：

| 实验 | Registry exp_id | Ign-F1 | Rel-F1 | Evi-F1 | EDCR |
|------|----------------|--------|--------|--------|------|
| CED v3-base (s42) | `reeval_ced_s42` | **0.4423** | 0.4517 | 0.8175 | 0.6569 |
| CED v3-large (s42) | `plan010_nli_large_eval_r2` | **0.4533** | 0.4636 | 0.8194 | 0.6530 |
| **差值** | | **+1.10pp** | +1.19pp | +0.20pp | -0.39pp |

Registry 数字与论文 ablation 表 (appendix.tex L65, L77) 完全吻合。

### Reviewer 误差来源

用户任务描述中说"原始 RSFT CED baseline: ign_f1 约 0.4517"——这个 **0.4517 是 `reeval_ced_s42` 的 rel_f1，不是 ign_f1**。ign_f1 是 0.4423，比 0.4517 低近 1pp。混淆了 ign_f1 和 rel_f1 导致差值看起来只有 +0.16pp。

### 结论

- **+1.10pp 准确无误**，指 Ign-F1 same-seed s42 对比
- analysis.tex 无需修改
- 附录已有完整数据支撑（包含 seed noise 0.88pp 的对比论证）

---
