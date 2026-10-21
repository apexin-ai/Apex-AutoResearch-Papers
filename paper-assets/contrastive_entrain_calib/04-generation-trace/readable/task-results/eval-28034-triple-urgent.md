# eval 28034 triple urgent

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-triple-urgent_20260523T061702_result.json`
- **Structured JSON:** [`67dd7fa52b2a6bd6e8a3.json`](../../sessions/67/67dd7fa52b2a6bd6e8a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 eval 全部正常运行中，都在处理 362 对数据。

| GPU | PID | 任务 | Checkpoint | 输出目录 |
|-----|-----|------|------------|----------|
| 0 | 51827 | ACT s2 ckpt-2500 | `/root/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2/checkpoint-2500` | `eval_results/exp004_s2_ckpt2500_v2/` |
| 1 | 30011 | reduced-lora 训练（不碰） | — | — |
| 2 | 52330 | reduced-lora ckpt-6000 | `/root/autodl-tmp/outputs/exp-004-reduced-lora/checkpoint-6000` | `eval_results/exp004_reduced_lora_ckpt6000_v2/` |
| 3 | 52840 | reduced-lora ckpt-6500 | `/root/autodl-tmp/outputs/exp-004-reduced-lora/checkpoint-6500` | `eval_results/exp004_reduced_lora_ckpt6500/` |

GPU 0 已跑到 20/362，GPU 2/3 刚开始推理。日志分别在 `/tmp/eval_s2_ckpt2500_v2.log`、`/tmp/eval_rl_ckpt6000.log`、`/tmp/eval_rl_ckpt6500.log`。

---
