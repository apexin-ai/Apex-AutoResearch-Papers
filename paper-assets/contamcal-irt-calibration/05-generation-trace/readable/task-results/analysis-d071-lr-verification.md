# analysis d071 lr verification

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d071-lr-verification_20260515T194854_result.json`
- **Structured JSON:** [`e973ce7be5e901648813.json`](../../sessions/e9/e973ce7be5e901648813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**D071 确认：lr 不一致，d000_v3 需用 lr=5e-5 重训。**

核实结果：
- `d000_s42`: lr=**2e-4**, lora_alpha=**32** — 非标准配置
- `d000_v2_s42`: lr=**5e-5**, lora_alpha=**16** — 标准配置

两个参数都不同，d000_s42 的 checkpoint 及下游 eval 数据均存疑。已更新 registry notes。

---
