# ssh verify remaining checkpoints

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_remaining_checkpoints_20260524T040804_result.json`
- **Structured JSON:** [`8604a4f1b2d9ccba7139.json`](../../sessions/86/8604a4f1b2d9ccba7139.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 checkpoints found. Also checked running evals and script existence.

| Checkpoint | 路径 | 存在? | 服务器 |
|------------|------|-------|--------|
| grpo_alpha0p5_20 | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20` | ✅ | westb-23072 |
| sft_alpha3p0_20 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20` | ✅ | westb-23072 |
| grpo_alpha4_20 | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20` | ✅ | westd-32935 |
| grpo_alpha3p0_20 | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2` | ✅ | westd-32935 (注意 `_v2` 后缀) |
| sft_cka_only_25 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25` | ✅ | westd-32935 |

**eval script**: `/root/recovery_aware_struct_prune/src/eval_math500.py` 存在于 westd-32935 ✅

**当前运行的 eval_math500 进程**:

| 服务器 | 实验 | GPU | CPU 时间 |
|--------|------|-----|----------|
| westd-32935 | sft_rasp_alpha0p5_20_fixed | cuda:1 | 97min |
| westd-32935 | sft_rasp_alpha4p0_20_fixed | cuda:2 | 66min |
| westd-32935 | sft_standard_25_fixed_v2 | cuda:0 | (刚启动) |
| westd-32935 | sft_rasp_alpha1p0_20_v2 | tmux session | (状态不明) |
| westb-23072 | grpo_random_20_fixed | cuda:1 | 391min |
| westb-23072 | sft_random_20_fixed_v3 | cuda:0 | 303min |

注意：`grpo_alpha3p0_20` 在 westd 上的目录名是 `grpo_rasp_alpha3p0_20_v2`（带 `_v2`），启动 eval 时需要用这个路径。westb 上有 `pruned_rasp_alpha3p0_20` 但没有 GRPO 训练后的 checkpoint。

---
