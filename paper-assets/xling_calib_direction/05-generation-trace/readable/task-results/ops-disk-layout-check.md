# ops disk layout check

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-layout-check_20260521T110448_result.json`
- **Structured JSON:** [`de2bccbc5435623ee5d4.json`](../../sessions/de/de2bccbc5435623ee5d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- `/root/xling_calib_direction/` 是 **symlink** → `/root/autodl-tmp/xling_calib_direction/`，实际在**数据盘**上
- 数据盘 `/dev/md0`：350G 总量，已用 269G，**剩余 82G (77%)**
- root 分区 overlay：30G 总量，已用 1.4G，剩余 29G
- `activations/` 目录当前 **9.1G**

**结论：不需要改 output path。** 项目已经正确放在数据盘上，82G 剩余空间充足。

---
