# fix westd gpu grpo 15pct

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd_gpu_grpo_15pct_20260520T050426_result.json`
- **Structured JSON:** [`86b55d2d6d6489f1668f.json`](../../sessions/86/86b55d2d6d6489f1668f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**修复完成。** 两个 GRPO 15% 训练已确认在 GPU 上运行：

| 实验 | PID | GPU | VRAM | Util |
|------|-----|-----|------|------|
| CKA-only 15% GRPO | 204464 | cuda:2 | 26663 MiB | 92% |
| Standard 15% GRPO | 204542 | cuda:3 | 26281 MiB | 91% |

**执行摘要：**
1. 旧进程 199774/199849 已 kill
2. `--gpu` 参数仅用于日志记录（`help="GPU index (for logging only, use CUDA_VISIBLE_DEVICES)"`），实际 GPU 通过 `device_map="auto"` + `CUDA_VISIBLE_DEVICES` 控制
3. 用 `train_grpo_v5.py` 重提交，参数与 20% fair run 一致（max_steps=100, max_completion_length=1024, save_steps=10, beta=0.01, loss_type=dapo, temperature=0.4, adamw_8bit）
4. tmux session: `grpo_cka15` (GPU 2), `grpo_std15` (GPU 3)
5. Registry `pipeline_cka_only_15` 和 `pipeline_standard_15` 已更新为 RUNNING

---
