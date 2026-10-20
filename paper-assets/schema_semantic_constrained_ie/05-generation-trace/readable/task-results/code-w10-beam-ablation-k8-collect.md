# code w10 beam ablation k8 collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_beam_ablation_k8_collect_20260517T094149_result.json`
- **Structured JSON:** [`90e4424b54879da78c88.json`](../../sessions/90/90e4424b54879da78c88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron不存在（可能已在之前session中删除或未创建）。任务完成，以下是完整结果报告。

---

## w10_beam_ablation_k8 实验结果 (Qwen3-8B, SciERC 551 docs, beam k=8, full_s1)

### Violation Metrics
| 指标 | 值 |
|------|-----|
| DR (Domain/Range) | **0.00%** (0/1744) |
| CF (Cross-field consistency) | **0.08%** (2/2483) |
| Entity type violations | 0.00% |
| Relation vocab violations | 0.00% |
| JSON parse failures | 0 |

### F1 Metrics
| 指标 | P | R | F1 |
|------|------|------|------|
| Entity | 26.95 | 39.93 | **32.18** |
| Relation | 6.54 | 11.70 | **8.39** |

### Beam Width Ablation 完整对比

| Metric | Greedy | k=2 | k=4 | **k=8** |
|--------|--------|-----|-----|---------|
| DR | 0.93% | 0.35% | 0% | **0%** |
| CF | 9.90% | 4.12% | 0.53% | **0.08%** |
| E_F1 | 30.98 | 31.54 | 32.00 | **32.18** |
| R_F1 | 8.36 | 8.75 | 8.56 | 8.39 |

### 关键发现
- **DR = 0%**，与k=4一致，beam k≥4即可完全消除domain/range violations
- **CF从0.53%降至0.08%**（仅剩2个冲突），k=8进一步压低cross-field violations至近零
- **E_F1达到全系列最高32.18**，beam width越大entity抽取越准
- **R_F1=8.39**，略低于k=2的峰值8.75，但高于greedy的8.36；R_F1在k=2后有轻微下降趋势
- 整体趋势：更大beam width持续改善constraint satisfaction和entity F1，但relation F1在k=2达到峰值后有diminishing/slight negative returns

**Conclusion: success** — hypothesis confirmed，更宽的beam search有效减少violations且不损害整体F1。

---
