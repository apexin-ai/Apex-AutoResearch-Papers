# code kl extra seeds config

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kl-extra-seeds-config_20260515T172039_result.json`
- **Structured JSON:** [`3de82b6e539af86219dc.json`](../../sessions/3d/3de82b6e539af86219dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个脚本已创建并通过语法检查：

| 脚本 | 路径 | 内容 |
|------|------|------|
| KL extra seeds | `/root/distill_sparse_swiglu/scripts/run_kl_extra_seeds.sh` | s0→gpu0, s1→gpu1 并行，`kl_normalized`, 1000 steps |
| BCE extra seeds | `/root/distill_sparse_swiglu/scripts/run_bce_extra_seeds.sh` | s0→gpu0, s1→gpu1 并行，`bce`, 1000 steps |

注意事项：
- 之前存在的 `kl_only_s0` / `kl_only_s1` checkpoint 目录为空（之前运行中断在 ~20 步），新脚本会写入 `kl_norm_v2_s0` / `kl_norm_v2_s1` 以匹配 v2 命名
- 两个脚本均未启动，`chmod +x` 已设置，随时可以执行

---
