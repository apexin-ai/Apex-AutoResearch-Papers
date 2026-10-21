# ops collect plan 022 results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_plan_022_results_20260517T135026_result.json`
- **Structured JSON:** [`db69d731d21b417b43e4.json`](../../sessions/db/db69d731d21b417b43e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## Plan_022 文本长度敏感性分析 — 已完成

| Truncation | 4-class Acc | 3-class Acc | d0 | d1 | d2 | d3 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 50 tokens | **51.5%** | 65.0% | 82.9% | 47.2% | 28.0% | 47.8% |
| 100 tokens | **56.3%** | 72.8% | 89.8% | 54.3% | 27.5% | 53.4% |
| 200 tokens | **60.4%** | 74.9% | 92.0% | 56.0% | 35.3% | 57.0% |
| 500 tokens | **61.0%** | 78.9% | 93.8% | 66.9% | 42.7% | 55.2% |

**关键发现：**

1. **50 tokens 已可检测 depth signal** — 4-class 51.5% 远高于 chance (25%)，d0 recall 达 82.9%
2. **收益递减明显** — 50→200 提升 ~9pp，200→500 仅 +0.7pp（4-class）；但 3-class 持续提升到 78.9%
3. **200 tokens 是性价比拐点** — 实际部署推荐最小长度
4. **d2 始终是瓶颈** — 即使 500 tokens 也仅 42.7% recall
5. **结论：success** — 假设成立，depth signal 在短文本中优雅退化而非断崖式消失

已注册：registry `text_length_sensitivity_001` (DONE/success)，artifact 已归档，memory.md 已更新。

---
