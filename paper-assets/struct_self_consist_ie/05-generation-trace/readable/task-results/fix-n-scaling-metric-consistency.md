# fix n scaling metric consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_n_scaling_metric_consistency_20260516T154206_result.json`
- **Structured JSON:** [`9b8c10d7a3814b31e997.json`](../../sessions/9b/9b8c10d7a3814b31e997.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### N-scaling 表修正结果

**修改文件：**
1. `docs/paper/sections/appendix.tex` — 表格数据 + 上方总结文字
2. `docs/paper/sections/discussion.tex` — 引用数值

**数据源：** `/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/unified_results.json`（macro F1, 551实例, seed=42 inference, 10-trial subsampling for N<32）

### 修正前后对比

| N | 列 | 旧值 | 新值 | 问题 |
|---|---|------|------|------|
| 2 | Oracle | +3.3 | +4.4 | 数值错误 |
| 2 | SJ/FK/EM | -2.26/-1.79/-1.91 | -2.54/-2.54/-2.54 | N=2时3个信号必然相同（对称tie） |
| 4 | Degen | 24.6% | 22.4% | |
| 4 | EM | -0.58 | -1.27 | |
| 4 | VC | -2.18 | -1.30 | |
| 8 | Degen | 13.3% | 12.4% | |
| 8 | Oracle | +14.2 | +13.8 | |
| 8 | **EM** | **+0.35** | **-0.33** | **符号错误** |
| 8 | VC | -1.43 | -1.82 | |
| 16 | **EM** | **+0.40** | **-0.15** | **符号错误** |
| 16 | VC | -2.04 | -2.91 | |
| 32 | Oracle | ~+20 | +19.2 | |
| 32 | FK | +0.83 | +0.62 | |

### 与 Table 2 的关系

- **Table 2 greedy**: 0.645 macro F1 (529 instances, 2-seed mean)
- **N-scaling 表 greedy**: 0.614 macro F1 (551 instances, seed=42 only)
- Footnote 已说明差异来源（instance set + weighting）
- 表内只报告 deltas (pp)，无直接绝对值冲突
- **结论：metric 空间一致（都是 macro F1），baseline 差异已由 footnote 充分说明**

### 根因

旧表格由一个有 bug 的早期脚本生成（`n_ablation.py` 的 `results.json` 中 rank32 regime），未使用统一 N=32 数据源的正确 greedy field，且 N=2 时未正确处理 consensus 信号的对称 tie。

---
