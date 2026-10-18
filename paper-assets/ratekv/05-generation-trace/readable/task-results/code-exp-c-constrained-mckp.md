# code exp c constrained mckp

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_c_constrained_mckp_20260514T000238_result.json`
- **Structured JSON:** [`ff12a62596bd656a2b0a.json`](../../sessions/ff/ff12a62596bd656a2b0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。总结：

**exp_c_constrained_mckp: PASS (success)**

| 指标 | 值 |
|------|-----|
| Constrained MCKP PPL | **11.23** (pass: ≤14.95) |
| Uniform 4-bit PPL | 15.45 |
| PPL improvement | **+4.21** |
| Memory ratio | 0.2500 (pass: ≤0.25) |
| Bit distribution | 8bit:4 (L0), 4bit:100, 2bit:8 |
| Unconstrained MCKP PPL | 36.92 (collapsed) |

代码改动：
- `solver.py` — 新增 `_build_actions_no_pareto()` 和 `solve_mckp_constrained()`。跳过 Pareto 过滤保留所有 bit-width 选项，D009 约束：max_2bit=8 + L0 exclusion
- `run_exp_c.py` — 实验脚本，复用已有 PPL profiles

---
