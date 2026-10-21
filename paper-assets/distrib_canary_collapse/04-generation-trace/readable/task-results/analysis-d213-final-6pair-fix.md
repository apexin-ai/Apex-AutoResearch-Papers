# analysis d213 final 6pair fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d213_final_6pair_fix_20260524T010536_result.json`
- **Structured JSON:** [`9ad99470ecf56ca9a1c0.json`](../../sessions/9a/9ad99470ecf56ca9a1c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 combined JSON 已写入。下面是汇总。

---

## 第五部分：汇报

### s42 全 8 条件（全部从 6-pair JSON 提取的真实值）

| T | α | PermG_fwd | PermG_rev | Robust_K3 (v2) | v1 Robust_K3 | 变更 |
|---|------|-----------|-----------|----------------|-------------|------|
| 10 | 0.45 | 0/6 | 0/6 | **0/6** | 0/6 | — |
| 10 | 0.50 | 4/6 | 0/6 | **2/6** | 3/6 | **↓ 3→2** |
| 10 | 0.60 | 4/6 | 0/6 | **0/6** | 3/6 | **↓ 3→0** |
| 10 | 0.75 | 5/6 | 0/6 | **0/6** | 5/6 | **↓ 5→0** |
| 15 | 0.45 | 3/6 | 0/6 | **3/6** | 4/6 | **↓ 4→3** |
| 15 | 0.50 | 3/6 | 0/6 | **1/6** | 2/6 | **↓ 2→1** |
| 15 | 0.60 | 6/6 | 0/6 | **4/6** | 6/6 | **↓ 6→4** |
| 15 | 0.75 | 6/6 | 0/6 | **6/6** | 6/6 | — |

**8 条件中 6 个 Robust_K3 被修正，全部下降。** PermG_fwd/rev 值未变。根因确认：v1 的 Robust_K3 分子直接复制自 8-pair 分析（含 MAUVE 的 pair 拉高了 consensus）。

### s43 T=10 × 4α

| T | α | PermG_fwd | PermG_rev | Robust_K3 | 来源 | v1 状态 |
|---|------|-----------|-----------|-----------|------|---------|
| 10 | 0.45 | 1/6 | 0/6 | **0/6** | 6-pair JSON | v1 写 2/6 → **↓ 修正** |
| 10 | 0.50 | 6/6 | 0/6 | **3/6** | 6-pair JSON | v1 标记 missing → **新增** |
| 10 | 0.60 | 4/6 | 6/6 | **0/6** | 6-pair JSON | v1 标记 missing → **新增** |
| 10 | 0.75 | 6/6 | 6/6 | **0/6** | 6-pair JSON | v1 标记 missing → **新增** |

3 个原标记 "missing" 的实验数据实际在 `results/scale/14b_t10_a{α}_s43_fp32`（非 `phase_diagram/`），已全部补跑。s43 α=0.60/0.75 出现 PermG_rev=6/6（强反向信号），Robust_K3=0/6。

### 产出文件

- `artifacts/D213_14b_s42_6pair_combined_v2.json` — 修正后的 s42 全 8 条件
- `artifacts/D213_14b_s43_t10_6pair_combined.json` — 更新为 4 条件完整版（v2）
- 服务器端新增分析文件：
  - westd-19828: `D102_14b_t10_a050_s43_fp32_14b_6pair.json`
  - westd-17855: `D102_14b_t10_a060_s43_fp32_14b_6pair.json`, `D102_14b_t10_a075_s43_fp32_14b_6pair.json`, `D102_14b_t10_a045_s43_fp32_14b_6pair.json`

---
