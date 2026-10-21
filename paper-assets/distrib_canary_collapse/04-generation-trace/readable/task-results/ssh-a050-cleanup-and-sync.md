# ssh a050 cleanup and sync

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a050_cleanup_and_sync_20260517T064601_result.json`
- **Structured JSON:** [`4d569b98ecda1192add2.json`](../../sessions/4d/4d569b98ecda1192add2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

---

## 产出汇报

### 1. 标记 INVALID 的文件
**无**。a050_s44/analysis/ 目录仅含 `5method_leadlag.json` 和 `5method_summary.txt`，无 Worker B 产出的额外分析文件。

### 2. 权威分析文件路径及 PermG sig 确认

| Seed | 路径 | PermG forward sig | PermG reverse sig |
|------|------|-------------------|-------------------|
| s42 | `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/analysis/5method_leadlag.json` | **4/8** | 0/8 |
| s43 | `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/analysis/5method_leadlag.json` | **7/8** | 0/8 |
| s44 | `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44/analysis/5method_leadlag.json` | **4/8** | 0/8 |

**注意：实际值与预期（0/8, 6/8, 3/8）不一致。** 论文中 Table 5 脚注写的 "s42=0/8, s43=6/8, s44=3/8" 需要核实/更新。实际 3-seed 结果是 4/8, 7/8, 4/8 (median 4/8)。

### 3. 编译结果
- Errors: **0**
- Undefined citations: **0**
- 页数: **22 pages** (423,658 bytes)

---
