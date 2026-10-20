# ops nve full recalculation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_nve-full-recalculation_20260518T224359_result.json`
- **Structured JSON:** [`48b3febdd77c78419487.json`](../../sessions/48/48b3febdd77c78419487.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果已写入服务器。以下是 **NVE 重算对照表总结**：

## 主要发现

### Baseline 问题
- `exp_001_baseline` 目录不存在，使用 `baseline_s1`（与 `exp_009d_baseline_walker_s1` 数值完全一致）

### Walker 实验（baseline = baseline_s1）

| exp_id | 论文值 | 重算peakNVE | peak_step | paper_matches | 说明 |
|--------|--------|-------------|-----------|---------------|------|
| 008d_s1 | 4.12x | **2.09x** | 45K | **MISMATCH** | 只有2个数据点(35K,45K)，实验可能截断 |
| 008d_s3 | 1.53x | 1.53x | 105K | peakNVE | OK |
| **008d_s4** | **3.03x** | **4.62x** | 105K | **ve@105K** | 论文报的是raw ve_ratio(3.03)，不是NVE；Reviewer算的4.62才是NVE |
| 009b | 1.62x | 1.62x | 45K | peakNVE | OK |
| 008a_orig | 0.93x | 0.93x | 55K | peakNVE | OK |
| **008a_s1** | **0.43x** | **0.83x** | 55K | **ve@105K** | 论文报的是raw ve_ratio(0.43)，不是NVE；Reviewer的0.83是peakNVE |
| **008a_s2** | 0.51x | 0.89x | 45K | **nve@105K** | 论文值=nve@105K(0.507)，不是peak |
| 008e_v3_s1 | 0.94x | 0.94x | 35K | peakNVE | OK |
| 008e_v3_s2 | 3.78x | 3.78x | 105K | peakNVE | OK; eval_return@105K=**136.96**(论文137.0 ✓) |
| 008e_v3_s3 | 4.02x | 4.01x | 105K | peakNVE | OK |
| 008e_v3_s4 | 0.99x | 0.99x | 95K | peakNVE | OK |
| 008f | 0.97x | 0.97x | 55K | peakNVE | OK |
| 015b | peak 1.45x | 1.45x | 55K | peakNVE | OK; **final@105K=0.42**(论文说0.55，不匹配) |
| 006 | 4.83x | --- | --- | NOT FOUND | 目录不存在 |
| 009c | 1.14x | 1.14x | 105K | peakNVE | OK |
| **009c_s3** | **0.52x** | **1.04x** | 95K | **MISMATCH** | peak和105K(0.587)都不匹配 |

### Cheetah 实验（baseline = avg(023a, 023b)）

| exp_id | 论文值 | 重算peakNVE | peak_step | paper_matches | 说明 |
|--------|--------|-------------|-----------|---------------|------|
| 010b | 8.27x | 8.27x | 65K | peakNVE | OK |
| **010b_s0** | **70.64x** | **108.52x** | 105K | **ve@105K** | 论文报的是raw ve_ratio(70.64)，不是NVE |
| 008a_ch_s0 | 0.49x | 1.08x | 35K | nve@105K | 论文值=nve@105K(0.49)，不是peak |
| 008a_ch_s1 | 0.48x | 1.29x | 35K | nve@105K | 论文值=nve@105K(0.48)，不是peak |

### 关键问题

1. **3个值报了 raw ve_ratio 而非 NVE**：008d_s4 (3.03)、008a_s1 (0.43)、010b_s0 (70.64)
2. **3个值报了 nve@105K 而非 peak NVE**：008a_s2、008a_ch_s0、008a_ch_s1
3. **2个完全不匹配**：008d_s1（数据截断）、009c_s3
4. **015b final NVE**: 重算=0.42，论文说0.55
5. **exp_006_variable_dt**: 目录不存在

---
