# fix c2 preregistration b10000

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c2-preregistration-b10000_20260514T134718_result.json`
- **Structured JSON:** [`4e3b36b2936fc64496c9.json`](../../sessions/4e/4e3b36b2936fc64496c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完毕。汇总：

| 文件 | 修改 |
|------|------|
| `PRE_REGISTRATION_C2.md` | `B=1000` → `B=10,000` |
| `analysis/bootstrap_median_gradient.py` | 3处 `B=1000` → `B=10000` |
| `analysis/bootstrap_phase_gradient.py` | 3处 default/comment `1000` → `10000` |
| `analysis/analyze_v6_complete.py` | 3处 `n_bootstrap=1000` → `10000` |
| `analysis/bootstrap_ci_results.json` | `"B": 1000` → `"B": 10000` |

所有 B 值现在统一为 10,000，与论文和 n=50 实验一致。

---
