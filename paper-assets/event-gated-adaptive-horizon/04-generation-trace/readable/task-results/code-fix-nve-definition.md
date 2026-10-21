# code fix nve definition

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-nve-definition_20260516T033935_result.json`
- **Structured JSON:** [`4a09cd28da5336885d85.json`](../../sessions/4a/4a09cd28da5336885d85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两种模式均验证通过：

1. **无 baseline**：列名 `ve_ratio`，无 NVE 字样，Summary 标注 "no baseline provided, pathological threshold not applied"
2. **有 baseline（自身作 baseline）**：NVE 全部为 1.0000，`pathological_steps = 0/37`，列名分别为 `ve_ratio (raw)` 和 `NVE (normalized)`，threshold 标注 "applies to baseline-normalized NVE only"

修改完成。变更摘要：
- `compute_nve` → `compute_ve_ratio`，变量名 `nve` → `ve_ratio`
- 新增 `--baseline-logdir` 参数、`compute_baseline_ve_ratios`、`interpolate_baseline_ve_ratio`（最近邻匹配）
- 无 baseline 时只输出 ve_ratio，不做 pathological 判断；有 baseline 时同时输出 raw ve_ratio 和 normalized NVE，阈值仅应用于 NVE

---
