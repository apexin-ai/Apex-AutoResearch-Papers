# ops data migration probe

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_data-migration-probe_20260520T110456_result.json`
- **Structured JSON:** [`2f4b89aa03d495c2cb9d.json`](../../sessions/2f/2f4b89aa03d495c2cb9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## gpu-6000pro-2
- **项目总大小**: 18G
- **文件数**: 2,891
- **子目录明细**（按大小排序）:
  - `checkpoints/` — 16G
  - `results/` — 1.5G
  - `data/` — 1.2G
  - `paper/` — 11M
  - `logs/` — 9.7M
  - `artifacts/` — 6.3M
  - `scripts/` — 1.8M
  - `src/` — 784K
  - `results_filtered/` — 92K
  - `__pycache__/` — 88K
  - `baselines/` — 40K
  - `figures/` — 0
- **/root/autodl-tmp/ 其他数据**:
  - `models/` — 90G
  - `alfworld_data/` — 2.2G
  - `compresslink/` — 44M
  - `wild_data/` — 15M
- **磁盘使用率**: 250G 总量，175G 已用 (70%)，76G 可用

## westd-48862
- **项目总大小**: 2.9G
- **文件数**: 446
- **子目录明细**（按大小排序）:
  - `checkpoints/` — 2.2G
  - `data/` — 403M
  - `results/` — 322M
  - `scripts/` — 316K
  - `logs/` — 8K
  - `models/` — 0
  - `runs/` — 0
- **/root/autodl-tmp/ 其他数据**:
  - `models/` — 28G
  - `logs/` — 8K
- **磁盘使用率**: 250G 总量，47G 已用 (19%)，204G 可用

---

**迁移要点**：gpu-6000pro-2 数据量远大于 westd-48862（18G vs 2.9G），主要差异在 checkpoints（16G vs 2.2G）、results（1.5G vs 322M）和 data（1.2G vs 403M）。gpu-6000pro-2 还多了 paper/、artifacts/、baselines/ 等目录。westd-48862 磁盘余量充裕（204G 可用）。

---
