# analysis d108 mbr within rho

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d108_mbr_within_rho_20260516T070432_result.json`
- **Structured JSON:** [`1b9ba86127b7213e8519.json`](../../sessions/1b/1b9ba86127b7213e8519.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**SciERC NER (N=8, 551 instances)**
| | Within-ρ (rich, ≥3 unique) | Across-ρ |
|---|---|---|
| SJ | median=0.47, n=251 | 0.55 |
| EM | median=0.33, n=109 | 0.37 |

- 21% instances 所有 sample F1 相同（无选择余地）
- SJ selection 关闭 oracle gap 的 22.6%

**CoNLL NER (N=16, 3453 instances)**
| | Within-ρ (rich, ≥3 unique) | Across-ρ |
|---|---|---|
| SJ | median=0.94, n=605 | 0.48 |
| EM | median=0.83, n=436 | 0.45 |

- 58% instances 所有 sample F1 相同
- SJ selection 关闭 oracle gap 的 41.0%

**关键发现**：within-instance ρ 实际上是**正的且中等偏强**，与论文原声称（"utility correlates across but not within"）不一致。建议修改论文 framing：utility 在 within/across 两个层面都正相关，但 within-instance 选择增益有限（仅关闭 23-41% oracle gap），原因是 (a) 大量 instances 无 within-instance F1 方差，(b) 相关性虽正但不完美。

产出已保存在 `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/d108_mbr_within_rho/` 并注册为 artifact `d108_mbr_within_instance_rho`。

---
