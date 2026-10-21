# ssh curriculum r2 fixed data

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_curriculum-r2-fixed-data_20260516T150006_result.json`
- **Structured JSON:** [`c739eecf0cdf338ce984.json`](../../sessions/c7/c739eecf0cdf338ce984.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

| 项目 | 状态 |
|------|------|
| 磁盘 | 140GB 可用 (45% used) |
| Config 修改 | `data_path` → `proofwriter_fol_100.jsonl`; `no_wandb: true` |
| GPU 0 (s42) | PID 866667, 82GB VRAM, step 20+ running, `[WARMUP]` 正常 |
| GPU 1 (s43) | PID 866741, 81GB VRAM, step 20+ running, `[WARMUP]` 正常 |
| Registry | 两个实验均标记 RUNNING |

早期 prove_rate 信号健康（s42 step5=0.375, s43 step1=1.0, step15=0.625），warmup 阶段工作正常。预计 500 步约 25-30 分钟完成。

---
