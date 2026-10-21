# launch 70b lora scierc

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_70b_lora_scierc_20260521T115419_result.json`
- **Structured JSON:** [`e2a29b0d7b06cccc8650.json`](../../sessions/e2/e2a29b0d7b06cccc8650.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动并在正常运行。

**实验 r16_70b_lora_scierc 状态:**

| 项目 | 值 |
|------|-----|
| PID | 836206 |
| 进度 | 2/663 steps (~0.3%) |
| 速度 | ~15.2s/step |
| 预计总时间 | ~2.8 小时 |
| VRAM | GPU0: 43GB, GPU1: 50GB (device_map auto 分布到两卡) |
| 日志 | `/root/autodl-tmp/checkpoints/70b_lora_scierc/train.log` |
| Checkpoint | `/root/autodl-tmp/checkpoints/70b_lora_scierc/` |
| Cron 监控 | 每 5 分钟自动检查 (job a5e943ca) |

注意：`device_map="auto"` 把模型分布到了两张卡上（GPU0 + GPU1）。如果需要保留 GPU1 给其他任务，需要改成 `CUDA_VISIBLE_DEVICES=0` 并用自定义 device_map 限制单卡。目前两卡都不紧张，先继续。

---
