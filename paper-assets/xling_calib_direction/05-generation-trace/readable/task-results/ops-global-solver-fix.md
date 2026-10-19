# ops global solver fix

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_global-solver-fix_20260521T093127_result.json`
- **Structured JSON:** [`b4363782841fc1f902e4.json`](../../sessions/b4/b4363782841fc1f902e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部语法检查通过。

**修改报告：3处 `solver="lbfgs"` → `solver="liblinear"`**

| 文件 | 行号 | 原内容 |
|------|------|--------|
| `code/compute_cka.py` | 276 | `solver="lbfgs"` |
| `code/train_caclr.py` | 240 | `solver="lbfgs"` |
| `code/transfer_eval.py` | 226 | `solver="lbfgs"` |

无残留，13个 `.py` 文件语法检查全部通过。

---
