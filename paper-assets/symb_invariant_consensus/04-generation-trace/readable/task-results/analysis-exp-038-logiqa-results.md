# analysis exp 038 logiqa results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-038-logiqa-results_20260518T201603_result.json`
- **Structured JSON:** [`25046d6c66059d7d1502.json`](../../sessions/25/25046d6c66059d7d1502.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

监控已不存在（可能之前 auto-fail 时已清除）。

---

## exp-038 结果报告

**状态：成功完成 (200/200)，结论 = negative**

| Metric | Value |
|---|---|
| SICA accuracy | **78.00%** (156/200) |
| SC accuracy | **78.50%** (157/200) |
| Delta (SICA−SC) | **−0.50%** |
| McNemar p | **1.0000** (完全不显著) |

### Disagreement 分析

| | SC ✓ | SC ✗ |
|---|---|---|
| **SICA ✓** | 155 | 1 |
| **SICA ✗** | 2 | 42 |

仅 3 例 disagreement，SICA 和 SC 几乎完全一致。

### Pipeline 质量

| Metric | Value |
|---|---|
| Extraction rate | 86.4% (2073/2400) |
| Fail empty rate | 12.2% |
| Avg unique constraints | 26.7/题 |
| Contradiction rate | 0.8% (43/5348) |
| Wall time | 126.8 min |

### 解读

1. **SICA 在 LogiQA 上无增益**：delta = −0.5%，McNemar p=1.0，统计上完全等价
2. **Extraction 质量下降**：86.4% vs FOLIO ~90%+，12.2% 空提取——LogiQA 的非形式化推理更难提取 symbolic constraints
3. **矛盾检测几乎失效**：contradiction rate 仅 0.8%，constraint 之间几乎无冲突，MaxSAT 无法发挥筛选作用
4. **Capability trap 假设在此数据集未验证**：LogiQA 的多选逻辑推理与 FOLIO 的形式逻辑推理特性不同，constraint extraction 的价值依赖于问题的可形式化程度

---
