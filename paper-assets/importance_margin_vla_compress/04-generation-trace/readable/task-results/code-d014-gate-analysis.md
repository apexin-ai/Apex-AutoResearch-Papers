# code d014 gate analysis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d014-gate-analysis_20260515T200728_result.json`
- **Structured JSON:** [`dfb12f1bac9fb143733e.json`](../../sessions/df/dfb12f1bac9fb143733e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署到 `/root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py`，`--help` 验证通过。

功能概要：
- `--baseline` / `--imm`：接收两个 evaluate.py 产出的 JSON
- 默认聚合所有 eps>0 非剪枝条件计算 4 个 gate criteria（G1-G4）
- `--condition` 可指定单个条件评估
- `--output` 可导出详细 JSON 报告
- 退出码 0=PASS, 1=FAIL，可直接用于 CI

---
