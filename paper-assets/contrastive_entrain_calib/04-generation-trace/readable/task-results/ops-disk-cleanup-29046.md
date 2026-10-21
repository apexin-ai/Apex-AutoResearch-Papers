# ops disk cleanup 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-29046_20260523T162139_result.json`
- **Structured JSON:** [`7091d670198b0258f75f.json`](../../sessions/70/7091d670198b0258f75f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 删除目录 | 大小 |
|---------|------|
| `checkpoints/exp002v2_dcgrpo_cosine/` | 5.4G |
| `checkpoints/exp002_dcgrpo_seed1/` | 719M |
| `checkpoints/exp008_dryrun/` | 682M |
| `checkpoints/exp008_dryrun_v4/` | 682M |
| `output/activations.pt` | 721M |
| `output/phase5/` | 721M |

**释放空间：~9G**（根分区从 82% → 53%，可用空间从 5.5G → 15G）

保护文件确认完好：`backups/act-s1/checkpoint-8000/`、`backups/reduced-lora/` 均在。

---
