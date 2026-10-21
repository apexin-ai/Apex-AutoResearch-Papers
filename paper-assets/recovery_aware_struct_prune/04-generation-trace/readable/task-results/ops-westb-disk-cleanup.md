# ops westb disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-disk-cleanup_20260515T150841_result.json`
- **Structured JSON:** [`4ea37021eba555c9afe7.json`](../../sessions/4e/4ea37021eba555c9afe7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果：**
- 释放：59G（222G → 163G）
- 使用率：89% → **65%**
- 可用空间：29G → **88G**

已删除：
- `pruned_rasp_25/` (11G)、`pruned_standard_25/` (11G) — 25% 剪枝变体
- `pruned_rasp_20/` (12G)、`pruned_standard_20/` (12G) — 20% 剪枝中间产物
- `DeepSeek-R1-Distill-Qwen-7B/` (15G) — 原始 base model

88G 可用空间足够 step 50 的双 checkpoint 保存（每个 18-24GB，两个实验共 ~48GB）。

**额外发现：** SFT 目录内有 4 个中间 checkpoint（每个 35G，共 140G），GRPO 进程不引用它们。如需进一步释放可删除，但因在标记为 protected 的父目录内，暂不动。

---
