# verify 410m s43 canonical

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_410m_s43_canonical_20260523T000320_result.json`
- **Structured JSON:** [`377efbfcb5bb70df659e.json`](../../sessions/37/377efbfcb5bb70df659e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

---

## 验证结果

### 1. alpha_sweep/a050_s43_fp32 (canonical full run) — 17855

**数据完整性：✅ 完整**
- gen_0 到 gen_10 全部 11 个目录存在
- 所有 metrics.json 非空（418–427 bytes，一致）

### 2. D102 分析结果 (canonical)

| 指标 | 值 |
|------|-----|
| PermG fwd (FDR) | **6/8** |
| PermG rev (FDR) | **0/8** |
| K≥3 robust_pairs | **6/8** |
| threshold_criterion | `true_3sigma_d105` ✅ (符合 C008) |

Consensus K≥3 的 6 对: token_entropy→{distinct_1,2,3}, ece→{distinct_1,2,3}。两个 mauve 对 K=1，低于阈值。

### 3. phase_diagram/t10_a050_s43_fp32 (resume 实验) — 19828

**config.json 确认 `start_gen: 6`**，即从第 6 代恢复，不是 full run。虽然目录有 gen_0–gen_10（11个），但 gen_0–5 的数据来源不明（可能是复制或之前中断的部分结果）。

Resume 实验的 D102 分析结果：

| 指标 | 值 |
|------|-----|
| PermG fwd (FDR) | **0/8** |
| PermG rev (FDR) | **0/8** |
| K≥3 robust_pairs | **0/8** |

### 4. 对比结论

| | Canonical (full run) | Resume (start_gen=6) |
|---|---|---|
| 路径 | alpha_sweep/a050_s43_fp32 @17855 | phase_diagram/t10_a050_s43_fp32 @19828 |
| PermG fwd | 6/8 | 0/8 |
| PermG rev | 0/8 | 0/8 |
| K≥3 | 6/8 | 0/8 |

**Reviewer #114 的发现是正确的**：之前报告的 s43 PermG=0/8 来自 resume 实验（start_gen=6），该实验仅训练了 gen_6–10（5 代），时间序列太短导致 Granger 检验全部失效。Canonical full run（gen_0–10，完整 11 代）的 PermG 为 6/8 fwd、0/8 rev，方向性强且一致，K≥3=6/8。

---
