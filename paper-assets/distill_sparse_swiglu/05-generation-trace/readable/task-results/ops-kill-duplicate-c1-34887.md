# ops kill duplicate c1 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-duplicate-c1-34887_20260519T002529_result.json`
- **Structured JSON:** [`5b5a5642b5c2892cb1cf.json`](../../sessions/5b/5b5a5642b5c2892cb1cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

1. **PID 64486 已杀掉** — `ps aux` 无匹配输出，确认已终止。
2. **dense_baseline_hellaswag_piqa** — tmux session 正常运行，日志显示 HellaSwag 10-shot 评估已完成，当前正在 tokenize PIQA 数据集（进度 ~38%）。
3. **GPU 0 状态** — `nvidia-smi` 显示 GPU 0 上有两个 python 进程（PID 64493 占 63052 MiB，PID 65380 占 18252 MiB），两个都属于 dense baseline 评估（主进程 + lm-eval worker），无重复 C1 训练进程残留。

GPU 0 已清理干净，dense baseline 评估正常推进中。

---
