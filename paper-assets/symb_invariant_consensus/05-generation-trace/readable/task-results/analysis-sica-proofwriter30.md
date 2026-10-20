# analysis sica proofwriter30

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sica_proofwriter30_20260515T221704_result.json`
- **Structured JSON:** [`3e7eaa32b17c8d4e492e.json`](../../sessions/3e/3e7eaa32b17c8d4e492e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

## sica_proofwriter30 分析结果：配置错误，完全失败

**根因**：`--max-tokens 16384` = vLLM `--max-model-len 16384`，留给 prompt 的空间为 0 tokens。所有 API 请求立即返回 400 Bad Request。

**结果**：
- 30/30 题全部失败，SICA = SC = 0%
- 0 条 trace 生成，0 条约束提取，0 次投票
- 4 分钟跑完（全是 retry 开销）
- 无 intermediates 产出

**无法评估 sanity check 标准**（提取率、矛盾检出等），因为没有任何推理发生。

**修复**：重跑时将 `--max-tokens` 降至 10240（AIME 实验验证可用）或 12288。ProofWriter 题目 prompt 约 900-1500 characters，10240 output tokens 绰绰有余。

---
