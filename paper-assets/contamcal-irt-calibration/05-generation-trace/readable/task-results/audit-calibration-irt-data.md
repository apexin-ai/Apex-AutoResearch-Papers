# audit calibration irt data

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_calibration-irt-data_20260523T102146_result.json`
- **Structured JSON:** [`76d47ebe9d5d8c72e44c.json`](../../sessions/76/76d47ebe9d5d8c72e44c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果写入 `artifacts/data_audit_part2_calibration.md`。

**核对 45 个数字，44 个一致，0 个不一致，1 个源文件缺失。**

两个需注意的问题：

1. **DIF JSON key 名称互换**: `analysis/dif_comparison/results.json` 中的 `uniform_dif` / `nonuniform_dif` key 与论文中的 "Non-uniform" / "Uniform" 标签恰好反转。所有 10 个数值本身完全正确——只是 JSON 的 key 命名与论文约定相反，复现时可能导致混淆。

2. **d005 Cohen's d 源文件缺失**: 论文称 Min-K%++ 在 d005 时 "|d| > 1.4"，但该数值未在任何已找到的 JSON 产出中持久化存储。d100 的 Cohen's d = −1.98 有完整溯源。

---
