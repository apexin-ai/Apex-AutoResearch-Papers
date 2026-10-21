# fix exp002v3 output dir to datadisk

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp002v3-output-dir-to-datadisk_20260519T133514_result.json`
- **Structured JSON:** [`4f88c5b435b5f391080b.json`](../../sessions/4f/4f88c5b435b5f391080b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。汇总：

**OUTPUT_DIR 已修改** — 两个文件都已从根分区改到数据盘：
- `launch_exp002v3.sh` 第 9 行: `LOG_DIR=/root/autodl-tmp/checkpoints/exp002v3_dcgrpo_scaled_cosine`
- `run_exp002v3_dcgrpo_scaled_cosine.py` 第 28 行: `OUTPUT_DIR = "/root/autodl-tmp/checkpoints/exp002v3_dcgrpo_scaled_cosine"`

**新目录已创建**，可写验证通过。

**根分区 checkpoint 占用（共 7.5GB）**：

| 目录 | 大小 |
|------|------|
| `exp014_probe_baseline` | 5.6G |
| `exp008v3_binary_probe_grpo` | 1.9G |
| `exp016_actadd` | 2.4M |
| `exp003_r3only_seed2` | 0 (空) |

如果 exp014 和 exp008v3 的 checkpoint 已不需要，清理后可释放约 7.5GB 根分区空间。

---
