# code w10 qwen scierc ft beam collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_qwen_scierc_ft_beam_collect_20260517T102444_result.json`
- **Structured JSON:** [`12fac9ed612d2c9145fc.json`](../../sessions/12/12fac9ed612d2c9145fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无活跃 cron，无需删除。

---

## w10_qwen_scierc_ft_beam_4 实验结果

| 指标 | FT greedy (baseline) | ZS beam k=4 | **FT beam k=4 (本实验)** |
|------|---------------------|-------------|--------------------------|
| DR | 0% | 0% | **0%** |
| CF | 1.18% | 0.53% | **0.0%** |
| E_F1 | 67.05 | 32.00 | **66.88** |
| R_F1 | 43.77 | 8.56 | **44.23** |

**结论：success**

- CF 从 FT greedy 的 1.18% 降至 0.0%，beam search 完全消除了所有约束违反
- DR 保持 0%
- E_F1 几乎无变化（-0.17），R_F1 略有提升（+0.46）
- FT+beam 组合验证了 composability 假设：beam search 消除残余违反的同时不损失 F1

---
