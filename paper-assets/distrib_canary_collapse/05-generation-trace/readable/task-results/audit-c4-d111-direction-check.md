# audit c4 d111 direction check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_c4_d111_direction_check_20260519T223059_result.json`
- **Structured JSON:** [`22d0ac585aec6817f125.json`](../../sessions/22/22d0ac585aec6817f125.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**c4_a050**: naive 8/8→**4/8**, diff 8/8→**0/8**, K≥3 8/8→**6/8**, K≥4 8/8→**2/8** — 需更新 registry

**c4_a075**: naive 8/8→**0/8**, diff 8/8→**0/8**, K≥3 8/8→**6/8**, K≥4 8/8→**0/8** — 需更新 registry。所有 naive/diff peak_lag 均为负值，方向完全反转。

**c4_a025**: 已有 D111 修正，验证通过 ✓

**分析脚本 bug**: `batch_analysis.py` 和 `run_5method_s43.py` 均**未内置 D111 方向检查**。需在 `compute_consensus`（L375-378）和 summary 计数（~L445-446）两处加 `peak_lag > 0` 过滤。具体修复代码已写在报告中。

**C4 特有现象**: diff_xcorr 在三个 C4 实验中 peak_lag 全部 ≤ 0（几乎都是 -1），说明 C4 数据集上差分互相关系统性检测到下游→canary 方向。

---
