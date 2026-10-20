# check eval v3 extract

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-v3-extract_20260514T105518_result.json`
- **Structured JSON:** [`0d310f888c68702397ad.json`](../../sessions/0d/0d310f888c68702397ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志已确认两个 eval 均完成（202/202 samples）。完整结果如下：

## eval-base-v3 (base model)

| Metric | Mean | 90% CI |
|--------|------|--------|
| debug_accuracy | **0.748** | [0.693, 0.797] |
| probe_generation_rate | **1.000** | — |
| probe_executed | **0.599** | [0.545, 0.653] |
| probe_diagnostic | **0.104** | [0.069, 0.139] |
| probe_dependent | **0.153** | [0.109, 0.198] |

## eval-sft-v2 (SFT model)

| Metric | Mean | 90% CI |
|--------|------|--------|
| debug_accuracy | **0.767** | [0.718, 0.817] |
| probe_generation_rate | **0.990** | — |
| probe_executed | **0.594** | [0.540, 0.653] |
| probe_diagnostic | **0.129** | [0.089, 0.163] |
| probe_dependent | **0.149** | [0.104, 0.193] |

**对比要点：** SFT 在 debug_accuracy 上提升 +1.9pp（0.748→0.767），probe_diagnostic 提升 +2.5pp（0.104→0.129），CI 有重叠。probe_executed 和 probe_dependent 基本持平。probe_generation_rate SFT 略降（1.000→0.990）。

---
