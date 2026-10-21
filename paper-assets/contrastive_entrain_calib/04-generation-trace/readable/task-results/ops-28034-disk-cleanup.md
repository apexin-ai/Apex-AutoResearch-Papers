# ops 28034 disk cleanup

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_28034-disk-cleanup_20260520T102827_result.json`
- **Structured JSON:** [`d80eedc942c3484adb0b.json`](../../sessions/d8/d80eedc942c3484adb0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 清理报告

| 项目 | 值 |
|------|-----|
| **清理前** | 根分区 99%，可用 333MB |
| **清理后** | 根分区 97%，可用 1.1GB |
| **删除内容** | `/root/contrastive_entrain_calib/checkpoints/exp003/checkpoint-4000`（~0.8GB） |

### 根分区仍需关注的大目录

| 目录 | 大小 | 说明 |
|------|------|------|
| `outputs/exp-004-act-baseline/` | **12GB** | 最大占用 |
| `checkpoints/exp008v3_binary_probe_grpo/` | **5.6GB** | |
| `checkpoints/exp014_probe_baseline/` | **5.6GB** | |
| `results/exp001/` | 410MB | |
| `results/exp012_llama_direction/` | 91MB | |

根分区 29GB/30GB 仍然很紧张，`outputs/exp-004-act-baseline/`（12GB）和两个 checkpoint 目录（共 11.2GB）是大头，清掉可释放 ~23GB。

### 数据盘状态
- **ckpt-5000 确认位置**：`/root/autodl-tmp/checkpoints/exp003/checkpoint-5000/`（718MB）
- **数据盘剩余**：282GB 可用（20% 使用率）
- **eval 输出目录已创建**：`/root/autodl-tmp/results/exp003_unified_eval/` 和 `vanilla_d027_reeval/`

---
