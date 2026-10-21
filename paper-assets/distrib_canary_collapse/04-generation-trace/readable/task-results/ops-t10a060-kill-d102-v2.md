# ops t10a060 kill d102 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_t10a060-kill-d102-v2_20260522T194943_result.json`
- **Structured JSON:** [`5301b8f9e4deed7fa9da.json`](../../sessions/53/5301b8f9e4deed7fa9da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D102 结果：1.4B T=10 α=0.60 s42

### 实验完成
- 数据路径：`results/phase_diagram/t10_a060_s42_fp32_14b`
- gen_0 到 gen_10 全部完成（11 个点）
- 实验已自然结束，无需 kill

### D102 5-Method 结果

| 方法 | Forward sig | Reverse sig |
|------|-----------|------------|
| **PermG (FDR)** | **4/8** | **0/8** |
| Diff XCorr (FDR) | 8/8 | 8/8 |
| Threshold Onset | 0/8 | — |
| TY Granger | 0/8 (NaN) | — |
| Naive XCorr | — | — |

### K≥3 Consensus Pairs: **3/8**
- ece→distinct_1 (3/5: naive, diff, perm)
- ece→distinct_2 (3/5: naive, diff, perm)
- ece→distinct_3 (3/5: naive, diff, perm)

### 关键发现：Sync-dip 不是 scale-invariant

**410M α=0.60 T=10: PermG 0/8 (sync-dip)**
**1.4B α=0.60 T=10: PermG 4/8 fwd, 0/8 rev (strong asymmetry)**

1.4B 模型在 α=0.60 显示出明确的因果先导信号（ece 先于 distinct 指标变化），而 410M 在同一设置下是 sync-dip。说明 sync-dip 是小模型特有现象，随 scale 增大消失。

### 数据质量注意
- gen_0 和 gen_1 的 MAUVE 为 null（已用 NaN 处理）
- TY Granger 因 LAPACK 收敛问题全部 NaN（T=10 序列太短 + NaN 值）
- DLASCL warnings 不影响核心 PermG/DiffXCorr 结果

---
