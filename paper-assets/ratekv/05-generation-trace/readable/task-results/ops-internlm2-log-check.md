# ops internlm2 log check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_internlm2_log_check_20260516T025129_result.json`
- **Structured JSON:** [`757d615a2fc1505a15c4.json`](../../sessions/75/757d615a2fc1505a15c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：success**

InternLM2-7B hires profiling 完成，耗时 0.96h，256 heads 全部扫完。

**关键指标：**
| 指标 | 值 |
|------|-----|
| Top-5% concentration | 0.2422 (12 heads) |
| Layer-0 dominance ratio | 2.19x |
| delta(2bit) CV | 1.2223 |
| Positive delta heads | 246/256 |
| Baseline PPL | 7.632 |

**Top-5 sensitive heads:** L2H6 (0.237), L2H2 (0.183), L0H3 (0.181), L31H1 (0.130), L7H1 (0.114)

**产出文件：**
- `/root/ratekv/artifacts/internlm2_profiles_hires.json` (21.8KB, 完整 profile)
- `/root/ratekv/artifacts/internlm2_hires_bf16_2bitonly_results.json` (1.4KB, 汇总)

**对 hypothesis 的判断：** concentration = 0.2422 < 0.50，不满足 Spread 条件——sensitivity 分布比较均匀，没有显著的少数 dominant heads。这是一个 **Diffuse** 模型。

---
