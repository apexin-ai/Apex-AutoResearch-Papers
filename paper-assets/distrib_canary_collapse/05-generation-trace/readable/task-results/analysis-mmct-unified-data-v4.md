# analysis mmct unified data v4

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmct_unified_data_v4_20260518T161826_result.json`
- **Structured JSON:** [`1de9164d8e7a6929f0aa.json`](../../sessions/1d/1de9164d8e7a6929f0aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是结果总结。

## 完成情况

### 1. 参数差异根因

`5method_leadlag.json` 的 `_onset_gen` 和 `method_ablation.py`（Table 7）的实现有三处关键差异:

| | 旧 (5method_leadlag) | 新 (unified / Table 7) |
|---|---|---|
| sigma 来源 | `np.std(s[:3])` 前3点 | `np.std(s)` 全序列 |
| 方向 | `abs(s[i] - mu)` 双向 | `s[i] > base + 2σ` 单向上升 |
| 倍数 | 3x | 2x |

结果：旧实现下 canary 和 downstream 同时在 gen 1 触发 → lead_time=0 → 全部 not significant。

### 2. 修改的文件

- **`mmct/unified_analysis.py`** (新建) — 使用 Table 7 参数对 18 个条件重跑 5 种方法
- **`mmct/methods.py`** — 添加 `set_unified_data_dir()` 支持统一数据加载
- **`mmct/run_mmct.py`** — 使用统一数据，输出 v2 文件

### 3. Bug 检查

- **`consensus_test.py` L98**: 当前代码已正确使用 `direction="reverse"`，无需修改
- **Global weighting**: 已在现有代码中实现，无需修改

### 4. 统一数据结果 (unified_data/summary.json)

| 条件 | Naive | Diff | Thresh | PG | TY | K≥4 |
|------|-------|------|--------|----|----|------|
| **α=0.00 (null, 3 seeds)** | 7-8 | 3-5 | 3-5 | 0-2 | 0-1 | **0-2** |
| α=0.25 (2 seeds) | 8 | 4-5 | 3 | 1-2 | 0-2 | 0-1 |
| α=0.50 (3 seeds) | 8 | 6-8 | 6-8 | 4-7 | 0 | 3-5 |
| α=0.75 (3 seeds) | 8 | 8 | **8** | 6-8 | 0-1 | 6-8 |
| **α=1.0 generalize (7 conds)** | 7-8 | 6-8 | **8** | 5-6 | 0-2 | **5-7** |

Threshold 从 0/8 修复为 8/8，与 Table 7 一致。

### 5. MMCT v2 结果

| 模式 | FPR (α=0) | α=0.25 | α=0.50 | α=0.75 |
|------|-----------|--------|--------|--------|
| uniform_forward | **0** | 0 | 0 | 0.083 |
| uniform_bidir | **0** | 0 | 0 | 0.083 |
| **weighted_pair_fwd** | **0** | **0.438** | **0.583** | **0.792** |
| weighted_pair_bidir | **0** | 0.438 | 0.583 | 0.792 |
| weighted_global_fwd | **0** | 0 | 0 | 0.083 |
| weighted_global_bidir | **0** | 0 | 0 | 0.042 |

**Table 7 MMCT (α=1.0, weighted_pair_forward):** 6-8/8 across all 7 conditions.

### 6. 输出文件 (`artifacts/mmct_results/`)

| 文件 | 大小 |
|------|------|
| `unified_data/` (18 JSON) | 每个 ~15KB |
| `mmct_results_v2.json` | 839KB |
| `null_distribution_v2.json` | 3.9KB |
| `mmct_report_v2.md` | 46KB |
| `fpr_fnr_comparison_v2.md` | 1.6KB |
| `mmct_table7.md` | 4.4KB |
| `data_consistency_check.md` | 12KB |

### 7. 注意事项

- `weighted_global_forward` 在 α=1.0 下仅 0-2/8 significant — naive_xcorr 的 null FPR=95.8% 拉低了全局权重，导致过于保守
- `weighted_pair_forward` 是最优模式：FPR=0 且 α=0.75 检测率 79.2%
- 缺失条件: `a025_s42` (无数据)、`a010_s42` (无 all_metrics.json)
- 所有 110 处数据变更均为 threshold_onset 方法（3σ→2σ 全序列 std）

---
