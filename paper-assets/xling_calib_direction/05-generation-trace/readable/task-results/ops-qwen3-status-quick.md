# ops qwen3 status quick

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen3-status-quick_20260521T114642_result.json`
- **Structured JSON:** [`10a2e55a9a7209a65ed0.json`](../../sessions/10/10a2e55a9a7209a65ed0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Qwen3-235B-GPTQ-Int4 下载状态：未完成**

| 指标 | 值 |
|------|-----|
| Safetensors | **28/32**（根目录 28 个） |
| Temp 目录 | **1 个**，含 4 个未完成 shard（00026, 00027, 00029, 00031） |
| 当前总大小 | **134G** |
| Config 路径 | `/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4/config.json` |
| 层数 | **94** |
| hidden_size | **4096** |
| experts | **128**（每 token 激活 8 个，MoE 架构） |

还差 4 个 shard 在 `._____temp/` 中，下载进程可能仍在跑或已中断，需要确认是否有活跃的下载进程。

---
