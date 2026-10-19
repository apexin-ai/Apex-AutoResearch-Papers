# eval perlayer kl k4 50 s42 ppl v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_perlayer_kl_k4_50_s42_ppl_v2_20260522T184218_result.json`
- **Structured JSON:** [`fa7fbdc9cfd94e0a4abd.json`](../../sessions/fa/fa7fbdc9cfd94e0a4abd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 已更新为 DONE (negative)。

**总结：**

- 原始失败原因：不是 EXIT_CODE=127（command not found），而是 EXIT_CODE=2 — `--sparsity` 缩写歧义（匹配 `--sparsity_mode` 和 `--sparsity_target`）
- 重试使用完整参数名，成功执行
- **结果：K=4 50% PPL = 44.23**，比 K=1（34.85）更差，远高于 E2E KL（11.84）
- 结论 (negative)：增大 per-layer context window K 在 50% sparsity 下不仅无法缩小与 E2E 的差距，反而恶化了 PPL。genuine inter-layer coupling 在高 sparsity 下占主导。

---
