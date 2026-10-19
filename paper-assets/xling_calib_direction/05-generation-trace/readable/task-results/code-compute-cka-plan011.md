# code compute cka plan011

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compute-cka-plan011_20260521T091130_result.json`
- **Structured JSON:** [`fee7ba54164b31bfcd17.json`](../../sessions/fe/fee7ba54164b31bfcd17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`code/compute_cka.py` 已部署到服务器并通过验证。

- 语法检查: SYNTAX OK
- `--help`: 所有 CLI 参数正常显示
- 不依赖 pingouin（partial correlation 手动实现）
- 兼容新格式（npy）和旧格式（pt_flat）
- 四种分析均已实现：(a) same-layer cross-lang Spearman, (b) partial Spearman controlling for depth, (c) per-language Spearman, (d) subspace angle
- 所有 correlation 带 1000-resample bootstrap 95% CI
- 输出结构完整：JSON + CSV + report.txt

---
