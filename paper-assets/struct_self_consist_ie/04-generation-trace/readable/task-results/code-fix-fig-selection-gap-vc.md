# code fix fig selection gap vc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_fig_selection_gap_vc_20260519T081132_result.json`
- **Structured JSON:** [`e02552283fc1a12eadbb.json`](../../sessions/e0/e02552283fc1a12eadbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已修复。验证一致性：

| Signal | 图中 ρ | tab:quality_estimation ρ | 一致？ |
|--------|-------|--------------------------|-------|
| SJ | .359 | .360 | ✓ (0.3599 四舍五入) |
| FK | .266 | .267 | ✓ (0.2665 四舍五入) |
| EM | .294 | .295 | ✓ (0.2945 四舍五入) |
| VC | **.379** | **.379** | ✓ **已修复** |
| LP | .205 | .205 | ✓ |

**根因总结：** 脚本引用了旧 pipeline `exp_016_rerun_1024/correlation_matrix.json` 的 ρ 值（VC=0.2524），而表格用的是 `analysis_unified_rho_full.json` 的 unified gold-filtered pipeline 值（VC=0.3792）。同时 EM 也有轻微偏差（0.2990→0.2945）。

**修正内容：**
- VC ρ: 0.2524 → 0.3792
- EM ρ: 0.2990 → 0.2945
- 数据源注释更新为正确来源

**Seed 来源：** ρ 来自 seed42（unified pipeline），ΔF1 来自 3-seed mean。图中显示的标签 `.379` 与表格的 `.379` 一致（均为 0.3792 三位小数截断显示）。

---
