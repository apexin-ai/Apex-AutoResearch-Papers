# analysis silhouette audit and fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_silhouette_audit_and_fix_20260521T031004_result.json`
- **Structured JSON:** [`0d5faec25d8c0ec81f93.json`](../../sessions/0d/0d5faec25d8c0ec81f93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。关键结论：

### 1. 原始 0.632 来源
- `ablation_322_partition.py` 用 **gen-0 vs gen-1+** 基线 → 得到 k=2 silhouette = **0.7352**（不是 0.632）
- `permutation_test_ddr.py` 用 **gen-1 vs gen-2+** 基线 → 得到 k=2 silhouette = **0.6603**（不是 0.632）
- `plot_instruct_ddr_comparison.py:96` 纯硬编码 `0.632`
- 穷举了所有基线 × d 公式 × 数据文件 × scaler 组合，**均无法复现 0.632**。该值来自初始 snapshot，原始数据已丢失。

### 2. 正确值（features_8gen.csv, gen-1 vs gen-2+, StandardScaler）

| 分区 | Silhouette | Rank |
|------|-----------|------|
| **k=2 binary** (drifting vs non-drifting) | **0.660** | **1/35**（最优二分法） |
| 3/1/3 fixed (论文原始) | 0.409 | 5/301 (top 1.7%) |
| 3/2/2 fixed (tail_decay → intermediate) | 0.253 | 13/301 |

### 3. 3/2/2 vs 3/1/3
在正确基线（gen-1 vs gen-2+）下，**3/1/3 > 3/2/2**（0.409 vs 0.253），确认论文原始选择正确。

### 4. 建议
- 论文中所有 `0.632` 替换为 `0.660`（共 5 处 tex + 1 处 py）
- 使用 gen-1 vs gen-2+ 作为统一基线

---
