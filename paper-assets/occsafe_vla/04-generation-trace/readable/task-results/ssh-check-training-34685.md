# ssh check training 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-training-34685_20260528T223031_result.json`
- **Structured JSON:** [`1e23466bc2043c98be31.json`](../../sessions/1e/1e23466bc2043c98be31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**`full_occ_bn_v2_s2_r2` 训练状态汇报：**

| 项目 | 状态 |
|------|------|
| 进程 | **Alive**，PID 19218，已运行 2h59m |
| 当前进度 | **step 10879 / 50005 (21.8%)** |
| 速度 | ~1.02 it/s（约 1.06 s/it 近期略有波动） |
| 预计剩余 | ~11h 30m（约北京时间 5/29 凌晨 ~5:30 完成） |
| Checkpoint | 已保存 step 10000 checkpoint (`--10000_chkpt/lora_adapter/`) |
| GPU 占用 | cuda:0 被 PID 19300（子进程）占用 62152 MiB |

**结论：** 训练正常进行中，预计 5/29 05:30 (UTC+8) 左右完成 50005 步，在 DDL（5/28 20:00 UTC+8）**之后约 9.5 小时**。

⚠️ 这个实验无法在 DDL 前完成。如果需要在 DDL 前拿到结果，需要考虑提前终止或使用中间 checkpoint (step 10000/20000/30000)。

---
