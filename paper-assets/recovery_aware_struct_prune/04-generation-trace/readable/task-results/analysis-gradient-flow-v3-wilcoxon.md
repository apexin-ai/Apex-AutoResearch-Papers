# analysis gradient flow v3 wilcoxon

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_flow_v3_wilcoxon_20260519T162402_result.json`
- **Structured JSON:** [`7bfba986665b6f69fdee.json`](../../sessions/7b/7bfba986665b6f69fdee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

### Part A: RASP vs Standard Wilcoxon 配对检验

修改了 `gradient_flow_analysis.py` 的 `run_statistical_tests` 函数，从 ref-vs-others 改为全配对比较（`itertools.combinations`），并新增原始值保存。重跑完整分析（~6 分钟）。

**结果：**

| 比较 | 显著层 | 平均梯度 ratio |
|------|--------|---------------|
| CKA-only vs Standard | 55/56 | 2.89x |
| CKA-only vs RASP | 56/56 | 2.26x |
| **Standard vs RASP** | **45/56** | **1.28x (RASP > Standard)** |

Standard vs RASP 的 11 个非显著层集中在 deep layers（18-22, 24, 27），这些层梯度 norm 本身较小，差异不显著。

### Part B: Registry metrics 已更新

`gradient_flow_v3` registry 写入了完整指标，artifact 已注册。原始 per-sample 数据（`raw_gradient_norms.json`, 707KB）已保存，未来可直接做 post-hoc 分析无需重跑 GPU。

---
