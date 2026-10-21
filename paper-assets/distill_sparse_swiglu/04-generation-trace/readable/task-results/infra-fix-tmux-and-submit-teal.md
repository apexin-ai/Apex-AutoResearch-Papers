# infra fix tmux and submit teal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_tmux_and_submit_teal_20260517T155417_result.json`
- **Structured JSON:** [`66e6eb2528f6f7225a97.json`](../../sessions/66/66e6eb2528f6f7225a97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成：

1. **tmux** 已在 westd-41718 安装成功
2. **TEAL eval** (PID 6896) 正在 GPU 1 上运行，进度：wikitext2 已完成 (PPL=8.7332)，arc_challenge 已完成，MMLU 约 56%，剩余 winogrande 和 gsm8k
3. **Registry** 已更新为 RUNNING，记录了 PID、server、GPU、log_path 等元数据

注意：实际运行命令使用的是 `--baseline_mode teal_vanilla`（非 `--sparsity_mode teal_global`），这是之前 worker 启动时的配置。GPU 0 上还有一个 `downstream_ext_kl30_s42` eval 也在并行运行。

---
