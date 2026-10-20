# code d028 fpr null control

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d028_fpr_null_control_20260515T095308_result.json`
- **Structured JSON:** [`fe6490acb07cac584108.json`](../../sessions/fe/fe6490acb07cac584108.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D028 完成。

**产出汇总**：

### 服务器端
- `consensus_framework.py` 已更新（494 -> 644 行），新增 4 个函数：`_bh_fdr`、`load_null_control_data`、`compute_fpr_null_control`、`compute_phase2_fdr_sig_rates`。旧 `compute_fpr_fnr` 重命名为 `compute_fpr_fnr_diff`（deprecated）
- `results/analysis/d028_fpr_null_control.json` 和 `d028_fpr_null_control_full.json` 已生成

### 本地
- `consensus_framework.py` 已同步
- 报告写入 `artifacts/analysis/consensus_framework/d028_fpr_update.md`

### 关键结果

**alpha=0.0 Null Control FPR**：

| Method | FPR (raw) | FPR (BH) |
|--------|:-:|:-:|
| naive | 100% | 100% |
| differenced | 50% | 37.5% |
| threshold | 62.5% | 62.5% |
| **permG** | **0%** | **0%** |
| **TY** | **0%** | **0%** |

**Phase 2 FDR 关键变化**：permG 在 alpha=0.25/0.5 从 25% 降至 **0%**（BH 杀掉了边缘 p-values），进一步强化 permG 的特异性。TY 在 alpha=0.25 从 62% 降至 38%（C001 约束仍有效，不入论文）。

---
