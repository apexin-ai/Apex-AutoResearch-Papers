# code gsm8k median fix d080v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k_median_fix_d080v2_20260515T182740_result.json`
- **Structured JSON:** [`15a2cfb65ae01a41b6cf.json`](../../sessions/15/15a2cfb65ae01a41b6cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 17 行（1 header + 16 data）。验证通过：

**验证清单：**
- 16 行输出，无 NaN ✓
- DS importance s015-s025 median gradient > 0 且 Wilcoxon p < 0.05 ✓
- QW rand s030 标记 INVALID ✓
- CSV + JSON 都写入 ✓

---

**DS Importance dose-response 表（Director 需要）：**

| Sparsity | median_gradient | CI [2.5%, 97.5%] | wilcoxon_p |
|----------|----------------|-------------------|------------|
| s015 | +0.2409 | [0.0769, 0.4781] | 0.0003 |
| s020 | +0.7403 | [0.3139, 1.1186] | <0.0001 |
| s025 | +1.9915 | [0.9327, 2.8198] | <0.0001 |
| s030 | +4.6819 | [2.1211, 10.5566] | <0.0001 |

Dose-response 单调性确认：0.24 → 0.74 → 1.99 → 4.68，严格递增，全部 p < 0.001。与 MATH-500 方法论一致（median + Wilcoxon）。

注意：DS imp s030 的 mean_gradient 只有 0.607（被负离群值严重拉低），而 median 为 4.68——正好说明 mean→median 修复的必要性。

---
