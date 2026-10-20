# ops w7 qwen semantic exit check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w7_qwen_semantic_exit_check_20260516T072237_result.json`
- **Structured JSON:** [`2b461ea8f25355c4365e.json`](../../sessions/2b/2b461ea8f25355c4365e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**状态**: **SUCCESS** — 551/551 完成，0 失败，0 JSON 解析错误。

### Violation Metrics 对比

| Metric | semantic_only | grammar_only | unconstrained (baseline) |
|--------|:------------:|:------------:|:------------------------:|
| ET% | **0.0%** | 0.0% | ~1.95% |
| RV% | **0.0%** | 0.0% | — |
| DR% | **0.6%** | 1.9% | ~1.95% |
| CF | 15 | 0 | — |

### F1 Metrics

| Metric | semantic_only | grammar_only |
|--------|:------------:|:------------:|
| E_P | 0.6523 | 0.6523 |
| E_R | 0.6898 | 0.6898 |
| E_F1 | **0.6705** | 0.6705 |
| R_P | 0.4073 | 0.4087 |
| R_R | 0.4713 | 0.4733 |
| R_F1 | **0.4369** | 0.4386 |

### 分析

- **DR 从 1.9% 降至 0.6%** — semantic 层有效消除了大部分 domain-range 违规（降幅 ~68%），但未完全归零（残留 7 个 DR violation）
- **ET/RV 均为 0%** — fine-tuned 模型本身已学会正确的 entity type 和 relation vocabulary，两个 ablation 条件下一致
- **CF = 15** — semantic_only 引入了 cross-field consistency 违规（grammar_only 为 0），这说明 grammar 层对 CF 有抑制作用
- **F1 几乎相同** — semantic 约束对抽取质量无负面影响（R_F1 差异仅 0.0017）
- Entity F1 完全一致（两者共享同一 fine-tuned 模型，entity 抽取不受解码约束影响）

**关键发现**: Semantic 层独立贡献了 DR 降低（1.9% → 0.6%），验证了 ablation 假设。但 DR 未归零，7 个残留 violation 值得检查是否为边界情况。

---
