# ssh check phi3 profiling result

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_phi3_profiling_result_20260516T014722_result.json`
- **Structured JSON:** [`eb45bafa8004f1931077.json`](../../sessions/eb/eb45bafa8004f1931077.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验成功完成。** 无任何错误。

## 结果摘要

| 指标 | 值 |
|------|-----|
| 模型 | Phi-3-medium-14B |
| 总耗时 | 2.48h (149 min) |
| Baseline PPL | 4.783 |
| Top-5% concentration | **0.1742** (20 heads) |
| CV of delta(2bit) | 0.8905 |
| Layer-0 dominance | 0.04x (非 L0 主导) |

**Shape 分类：Early-middle concentrated**——敏感度集中在 L8-L11，不是常见的 L0/embedding 邻近层主导模式。

**Top-5 最敏感 heads：**
- L9H6: +0.1806
- L8H9: +0.1724
- L11H8: +0.1671
- L9H4: +0.1656
- L11H4: +0.0843

**t1/t5 指标：** concentration = 0.1742，CV = 0.89，属于中等非均匀分布（有明显热点但不极端集中）。

GPU 已释放（0 MiB used on both GPUs）。产出文件已保存到 `artifacts/`。

---
