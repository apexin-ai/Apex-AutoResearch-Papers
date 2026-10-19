# code plan 007 benchmark prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_007_benchmark_prep_20260516T022847_result.json`
- **Structured JSON:** [`1f18fb0b3b6c7c52cff2.json`](../../sessions/1f/1f18fb0b3b6c7c52cff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已注册。

总结：
- 4 个 checkpoint 全部就位
- **核心风险**：运行中的 KL 30% 和 TEAL 50% 用的是旧脚本（0-shot），与已有 Dense/KL 50% 结果（标准 few-shot）不可比，完成后需用 benchmark_eval.py 重跑
- 6 个条件的 benchmark_eval.py 命令已就绪，双 GPU 并行 3 批约 135 分钟可完成

---
