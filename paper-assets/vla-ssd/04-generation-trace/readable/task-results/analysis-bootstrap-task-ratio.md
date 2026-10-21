# analysis bootstrap task ratio

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_task_ratio_20260519T154920_result.json`
- **Structured JSON:** [`9933a180161af06893ad.json`](../../sessions/99/9933a180161af06893ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：**2.5× [1.0, 11.1]**

95% CI 下界 > 1.0，ratio 显著大于 1。但 CI 极宽（上界 11.1×），主要因为 simple 组 n=4 且含 outlier "cream cheese in bowl"（|ΔR²|=0.159 远高于其余 simple tasks）。当 bootstrap 重采样到该 outlier 占比低时 simple 均值很小，推高 ratio。

输出已写入 `artifacts/bootstrap_task_ratio.json`。

---
