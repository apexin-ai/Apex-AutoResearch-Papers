# ops data archive

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_data-archive_20260525T204544_result.json`
- **Structured JSON:** [`e3530a28cce6b79e74f7.json`](../../sessions/e3/e3530a28cce6b79e74f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**探测完成。空间不足，无法完成完整复制。**

## 探测结果汇总

| 目录 | 路径 | 大小 |
|------|------|------|
| 代码仓库 | `/root/trace-verdict-study/` | 510M（含 .git） |
| Checkpoints | `/root/autodl-tmp/trace-verdict-study-checkpoints/` | **102G**（~151 个实验目录） |
| 数据 | `/root/autodl-tmp/trace-verdict-study-data/` | 903M |
| Outputs | `/root/trace-verdict-study/outputs/` | 499M |
| Paper | `/root/trace-verdict-study/docs/paper/` | 2.2M |
| Figures | `/root/trace-verdict-study/figures/` | 2.2M |
| Results | `/root/trace-verdict-study/results/` | 1.1M |
| Logs | `/root/trace-verdict-study/logs/` | 1.8M（训练日志 140+ 个） |
| wandb | — | **不存在** |
| registry.yaml | — | **不存在** |
| runs/ | — | **不存在** |

## 磁盘空间

| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| `/`（根分区） | 30G | 23G | **7.7G** |
| `/root/autodl-tmp/`（数据盘） | 250G | 203G | **48G** |

## 问题：空间不足

归档所需空间估算：
- code + outputs + results + logs + paper + figures ≈ **1.5G**（可放根分区或数据盘）
- data ≈ **903M**（可复制）
- **checkpoints = 102G** → 根分区(7.7G)和数据盘(48G)均无法容纳副本

**方案选择：**

1. **在 autodl-tmp 创建归档**（推荐）：将非 checkpoint 文件（~2.5G）复制到 `/root/autodl-tmp/trace-verdict-study_archive/`，checkpoints 已在同一数据盘上，改用 **符号链接** 指向原位置
2. **只归档非 checkpoint 部分**：完整复制 code/data/results/paper，checkpoint 部分仅记录路径清单
3. **放弃归档**：等释放空间后再做

请指示如何处理 checkpoints。

---
