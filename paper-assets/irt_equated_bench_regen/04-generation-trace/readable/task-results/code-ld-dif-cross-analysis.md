# code ld dif cross analysis

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ld_dif_cross_analysis_20260521T080459_result.json`
- **Structured JSON:** [`e122047422293b1ca864.json`](../../sessions/e1/e122047422293b1ca864.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

1. **极端 LD（% |Q3|>0.20）与 DIF C% 无关** — r = 0.09, p = 0.50，三种相关系数（Pearson/Spearman/Kendall）均不显著。Top-5 仅 2 个 overlap（human_aging, professional_medicine）。

2. **均值 Q3 与 DIF C% 显著负相关** — r = −0.36, p = 0.006。高均值 Q3 的 domain（内部 item 依赖强）反而 DIF 率更低。解释：事实性密集型 domain（如 moral_scenarios, world_religions）item 间共享窄子技能导致高 Q3，但这类 item 跨 cohort 稳定；推理型 domain（formal_logic, business_ethics）inter-item 依赖低但对模型能力变化更敏感。

3. **DIF C% 与 accuracy gain 正相关**（r = 0.34, p = 0.01），LD 与 accuracy gain 无关（r = −0.10, n.s.）。

**结论：LD 和 DIF 是互补的 item quality 诊断维度，不可互相替代。** 报告和数据已注册到 `plan_013_supplement`。

---
