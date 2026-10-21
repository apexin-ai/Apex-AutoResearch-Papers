# research task specificity

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_task_specificity_20260519T130406_result.json`
- **Structured JSON:** [`393dc6bb591358ac934c.json`](../../sessions/39/393dc6bb591358ac934c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出文件已生成。关键发现：

| Benchmark | Taxonomy | ρ | p (one-tailed) | Significant |
|-----------|----------|---:|---:|:---:|
| LAMBADA (acc) | Retrieval-dependent | **−1.00** | **0.008** | **Yes** |
| HellaSwag (acc_norm) | Reasoning-dependent | +0.30 | 0.742 | No |
| ARC-Challenge (acc_norm) | Reasoning-dependent | +0.60 | 0.883 | No |
| Winogrande (acc) | Reasoning-dependent | +0.10 | 0.608 | No |
| ARC-Easy (acc) | Mixed | −0.70 | 0.117 | No |
| MMLU (acc) | Mixed | −0.70 | 0.117 | No |

**结论**：

1. **LAMBADA 是唯一显著的 equalizer effect** (ρ=−1.0, p=0.008)：cross-arch std 从 pure 的 0.024 单调下降到 h3-1 的 0.005，完美负相关。这与其 retrieval-dependent 性质一致——full attention 层直接提供精确检索能力，使不同架构趋同。

2. **Reasoning-dependent tasks（HellaSwag、ARC-Challenge、Winogrande）完全没有收敛趋势**，ρ 甚至为正。这些任务的跨架构差异不受 attention ratio 影响，说明 reasoning 能力更多由非 attention 组件决定。

3. **Mixed tasks（ARC-Easy、MMLU）有中等负相关**（ρ=−0.7）但未达显著（p=0.117），可能因 n=5 统计功效不足。

---
