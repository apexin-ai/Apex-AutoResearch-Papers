# analysis tost sensitivity

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-sensitivity_20260517T090419_result.json`
- **Structured JSON:** [`e7ffbdcaa91b3466e030.json`](../../sessions/e7/e7ffbdcaa91b3466e030.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Margin | Qwen3-4B p | eq? | DeepSeek p | eq? |
|--------|-----------|-----|-----------|-----|
| ±1.0pp | 0.871 | No | 0.274 | No |
| ±1.5pp | 0.113 | No | 0.209 | No |
| ±2.0pp | 0.007 | Yes | 0.166 | No |
| ±3.0pp | 0.000 | Yes | 0.116 | No |
| ±5.0pp | 0.000 | Yes | 0.071 | No |

关键发现：
- **Qwen3-4B**: 最小等价 margin = ±1.63pp（5 seeds 足够检测等价性）
- **DeepSeek-6.7B**: 最小等价 margin = ±7.19pp（2 seeds 功效不足，SE 太大无法在任何合理 margin 下确认等价）

DeepSeek 虽然观测差异极小（0.02pp），但 n=2 导致 SE=1.135，统计功效不足以在 ±5pp 内确认等价。这是 underpowered 的典型案例，不是方法差异的证据。

输出已保存至 `artifacts/tost_sensitivity.json`（`art_20260517_00b5af`）。

---
