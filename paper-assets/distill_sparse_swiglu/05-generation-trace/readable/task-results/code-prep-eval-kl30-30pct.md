# code prep eval kl30 30pct

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_eval_kl30_30pct_20260516T052218_result.json`
- **Structured JSON:** [`24852368ed904524a8f7.json`](../../sessions/24/24852368ed904524a8f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存到 `artifacts/eval_kl30_30pct_command.md`。

关键修正：
- **参数名是 `--checkpoint`**，任务模板中的 `--predictor_path` 不存在
- **evaluate.py 没有 `--output_dir`**，结果输出到 stdout，命令已加日志重定向
- 两个脚本的 `--sparsity_target` 默认都是 0.5，所有命令都显式传了 0.3
- benchmark_eval.py 也需要传 `--sparsity_target 0.3`，已准备了 per_token 和 teal_global 两种模式的命令

---
