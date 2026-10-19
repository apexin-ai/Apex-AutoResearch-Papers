# analysis advantage ratio multistep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_advantage_ratio_multistep_20260524T234830_result.json`
- **Structured JSON:** [`20bfe75f795b8b0f0dab.json`](../../sessions/20/20bfe75f795b8b0f0dab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 四个目标时间点（hsweep_h2_seed2）

| Step | Ratio |Â_correct| / |Â_wrong| | n_correct | n_wrong | |Â_correct| | |Â_wrong| |
|------|------|-----------|---------|-------------|-----------|
| 1 | **N/A** | 0 | 200 | — | — |
| 5 | **2.6360** | 30 | 170 | 0.025291 | 0.009594 |
| 10 | **2.1570** | 4 | 196 | 0.037390 | 0.017334 |
| 15 | **5.6396** | 30 | 170 | 0.035052 | 0.006215 |

### 完整 15 步趋势

| Step | Ratio | n_c | n_w |
|------|-------|-----|-----|
| 1 | N/A | 0 | 200 |
| 2 | 9.54 | 20 | 180 |
| 3 | N/A | 0 | 200 |
| 4 | N/A | 0 | 200 |
| 5 | 2.64 | 30 | 170 |
| 6 | 4.13 | 32 | 168 |
| 7 | N/A | 0 | 200 |
| 8 | 5.40 | 15 | 185 |
| 9 | 26.25 | 4 | 196 |
| 10 | 2.16 | 4 | 196 |
| 11 | N/A | 0 | 200 |
| 12 | 6.47 | 9 | 191 |
| 13 | 12.53 | 4 | 196 |
| 14 | 2.54 | 100 | 100 |
| 15 | 5.64 | 30 | 170 |

### 关键发现

1. **Step 1 无 correct 样本**（所有 200 条 step_return ≤ 0），无法计算 ratio。
2. **Ratio 始终 > 1**（所有可计算的 step 均在 2.16–26.25 范围），说明 |Â_correct| 持续大于 |Â_wrong|，correct actions 始终获得更大的 advantage 幅度。
3. **之前报告的 step 5 ratio ≈ 1.32 无法复现**——实际值为 2.64，差距显著。可能之前用了不同的分组逻辑或不同的数据源。
4. **Seed1 数据不存在**，无法做双 seed 对比。
5. Step 14 是唯一 n_correct = n_wrong = 100 的步，ratio 仍为 2.54。n_correct 波动极大（0–100），correct 样本极度稀疏（多数 step 只有 0–30 个）。

---
