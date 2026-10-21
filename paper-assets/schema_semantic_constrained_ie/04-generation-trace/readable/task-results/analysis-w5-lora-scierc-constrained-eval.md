# analysis w5 lora scierc constrained eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w5_lora_scierc_constrained_eval_20260515T162340_result.json`
- **Structured JSON:** [`46600dca3ea60b4fc1e4.json`](../../sessions/46/46600dca3ea60b4fc1e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the analysis:

---

## w5_lora_scierc_constrained_eval 结果

### Metrics 汇总

| Metric | Fine-tuned Constrained | Fine-tuned Unconstrained | Base Constrained | Base Unconstrained |
|--------|----------------------|------------------------|-----------------|-------------------|
| **Entity F1** | **0.6705** | 0.6705 | 0.3098 | 0.3101 |
| **Relation F1** | **0.4377** | 0.4386 | 0.0836 | 0.0823 |
| ET | 0% | — | — | — |
| RV | 0% | — | — | — |
| **DR** | **0.00%** | 1.95% | 0.93% | 15.37% |
| **CF** | **1.18%** | 0% | 9.90% | 0.08% |
| JSON parse | 100% | — | — | — |
| Samples | 551 | 551 | 551 | 551 |

运行时间：~28 分钟（551 samples, wall_clock 1665s）

### 关键分析

**1. Composability 验证：完全成功**
- DR: 1.95% → **0.00%** — 约束解码彻底消除了 domain-range 违规
- ET/RV 均为 0% — grammar constraint 完美约束了词汇表

**2. F1 代价：几乎为零**
- Entity F1: 0.6705 → 0.6705 (±0.00pp) — 完全无损
- Relation F1: 0.4386 → 0.4377 (-0.09pp) — 可忽略

**3. 相比 base model 的提升幅度**
- Entity F1: 0.3098 → 0.6705 (**+36.07pp**)
- Relation F1: 0.0836 → 0.4377 (**+35.41pp**)

**4. CF 趋势**
- Base constrained CF=9.90% → Fine-tuned constrained CF=1.18% (**-8.72pp**)
- Fine-tuned 模型学会了更一致的实体类型标注，大幅降低了 cross-field 不一致
- CF 从 unconstrained 的 0% 上升到 1.18%，说明 constrained decoding 在改变生成路径时引入了少量类型不一致（21 例，主要是 Generic vs 具体类型的歧义，如 "parsing" 既标 Generic 又标 Task）

### 结论

**Composability 完全验证通过。** Fine-tuning + constrained decoding 是正交且可组合的：fine-tuning 提升 F1（+36pp entity, +35pp relation），constrained decoding 消除 schema 违规（DR → 0%），两者组合无 F1 代价。

---
