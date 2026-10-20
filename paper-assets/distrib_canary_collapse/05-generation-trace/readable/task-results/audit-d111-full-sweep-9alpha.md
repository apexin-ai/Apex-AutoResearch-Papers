# audit d111 full sweep 9alpha

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_d111_full_sweep_9alpha_20260519T232440_result.json`
- **Structured JSON:** [`158e01ce88ddaa6864c1.json`](../../sessions/15/158e01ce88ddaa6864c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D111 方向检查审计完成。汇总：

**全部 9 个 α 值均需修正**，核心发现：

| α | naive | diff | K≥3 | K≥4 |
|---|-------|------|-----|-----|
| 0.00 | 1.000→0.625 | 0.500→0.000 | 0.375→0.125 | 0→0 |
| 0.05 | 0.875→0.375 | 0.375→0.000 | 0.375→0.000 | 0→0 |
| 0.10 | 0.875→0.500 | 0.750→0.125 | 0.500→0.250 | 0.250→0 |
| 0.25 | 1.000→0.625 | 0.375→0.250 | 0.500→0.250 | 0→0 |
| 0.35 | 1.000→1.000 | 0.500→0.000 | 0.750→0.500 | 0.250→0 |
| 0.50 | 1.000→0.625 | 0.875→0.125 | 0.875→0.625 | 0.750→0.250 |
| 0.60 | 0.875→0.500 | 1.000→0.000 | 1.000→0.750 | 0.875→0.125 |
| 0.75 | 0.875→0.000 | 0.750→0.000 | 0.875→0.750 | 0.750→0 |
| 1.00 | 1.000→0.000 | 0.750→0.000 | 0.750→0.750 | 0.750→0 |

**关键发现**：
- **diff_fwd 在 7/9 个 α 值为 0** — 几乎所有 diff_xcorr 显著峰都在负 lag
- **α≥0.75 时 naive_fwd 也为 0** — 高污染时交叉相关一致性地在反方向达峰
- **K≥4 从 0.750 降至 0.000 (α=0.75, 1.00)** — 但 K≥3 仍维持 0.750，因为 threshold+permG+TY 不受影响
- 方向检查后，高 α 的 forward evidence 完全由 threshold onset、PermG 和 TY 承载

已完成：
1. 审计报告 → `artifacts/d111_full_sweep_audit.md`
2. CSV 更新 → `dose_response_5method_regime.csv` + `consensus_heatmap_data.csv`
3. Registry → 8 个实验的 note 已标注 D111 direction-checked

---
