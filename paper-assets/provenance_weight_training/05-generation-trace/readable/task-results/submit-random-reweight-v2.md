# submit random reweight v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_random_reweight_v2_20260516T190114_result.json`
- **Structured JSON:** [`acc07156f62127c6b7a8.json`](../../sessions/ac/acc07156f62127c6b7a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动。

**汇报：**

| 项目 | 值 |
|------|-----|
| PID | 353995 |
| GPU | cuda:0, 46523 MiB 已占用 |
| 速度 | ~2.12s/it |
| 总步数 | 6103 |
| 预计运行时间 | ~3.5 小时 |
| 进度 | 18/6103 (正常训练中) |

关键参数确认：
- WANDB_MODE=disabled ✓
- CUDA_VISIBLE_DEVICES=0 ✓
- output_dir=/root/autodl-tmp/output/models/random_reweight_v2_seed42 ✓
- weighting_method=random, seed=42, 200M tokens ✓

日志路径：`/root/autodl-tmp/output/models/random_reweight_v2_seed42/train.log`

---
