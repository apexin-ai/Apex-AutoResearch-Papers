# fix gpu0 collision

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu0_collision_20260521T223650_result.json`
- **Structured JSON:** [`ede20b0dd8af45ccb655.json`](../../sessions/ed/ede20b0dd8af45ccb655.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. GPU 0 碰撞 — 已解决
- 杀掉 eval_math500 子进程 PID 426650（父进程 426645 的 SIGTERM 未传播到子进程，需额外杀子进程）
- GPU 0 现在只有 eval_gsm8k_sft_alpha4_20_v4 (PID 426311, 12712 MiB)

### 2. westb-23072 磁盘状况
- **250G 总量，237G 已用，14G 可用 (95%)**
- 大量 12G 级模型 checkpoint（约 17 个 × 12G = 204G），另有 9 个 1.5B 模型（各 2.8G ≈ 25G）
- 可用空间不足以复制一个完整的 7B 模型（~12G）

### 3. westd-29022 GPU 全览
| GPU | 进程 | 显存占用 |
|-----|------|---------|
| 0 | eval_gsm8k (426311) | 12712 MiB |
| 1 | python (382472) | 17930 MiB |
| 2 | python (412822) | 17518 MiB |
| 3 | python (385685) | 17642 MiB |

### 4. 建议：eval_math500_grpo_standard_20_fair_2048 在哪跑
- **westd-29022 GPU 0**：等 eval_gsm8k 完成后立即重新提交。模型已在 westd 本地（`/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair/`），无需跨机复制。
- westb 14G 剩余空间装不下 12G 模型，不建议往 westb 复制。
- 如果 GPU 1/2/3 有任务先结束，也可以用，但 GPU 0 的 eval 是轻量评测应该很快完成。

---
