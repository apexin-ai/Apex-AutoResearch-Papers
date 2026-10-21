# analysis r14 a5 residualized control

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_a5_residualized_control_20260518T164827_result.json`
- **Structured JSON:** [`25daed596285732c16f2.json`](../../sessions/25/25daed596285732c16f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A5 完成。结果汇总：

| Model | Orig BA | Orig Rnd BA | Orig Sel | Resid BA | Resid Rnd BA | Resid Sel | >5pp |
|-------|---------|-------------|----------|----------|--------------|-----------|------|
| R1-8B | 0.8259 | 0.6848±0.009 | 14.1pp | 0.6991 | 0.4706±0.015 | **22.8pp** | **Y** |
| OT-7B | 0.7006 | 0.5900±0.010 | 11.1pp | 0.6110 | 0.5070±0.014 | **10.4pp** | **Y** |
| R1-32B | 0.7265 | 0.5586±0.015 | 16.8pp | 0.5302 | 0.5002±0.021 | **3.0pp** | **N** |
| QwQ-32B | 0.7455 | 0.5828±0.012 | 16.3pp | 0.6051 | 0.5050±0.025 | **10.0pp** | **Y** |

3/4 模型通过 >5pp 阈值，确认 residualized HS 中存在 genuine safety signal。R1-32B 失败（3.0pp），因为 W=1 时去除位置信息后几乎无剩余信号（BA 降至 0.53，接近随机）。R1-8B 的 residualized selectivity（22.8pp）反而高于 original（14.1pp），因为 random baseline 在去位置后跌到近 0.47。

输出目录：`/root/autodl-tmp/contrastive_trace_safety/artifacts/r14_a5_residualized_control/`

---
