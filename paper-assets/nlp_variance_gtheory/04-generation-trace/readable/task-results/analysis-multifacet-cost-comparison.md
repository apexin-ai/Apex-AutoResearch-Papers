# analysis multifacet cost comparison

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multifacet_cost_comparison_20260523T064410_result.json`
- **Structured JSON:** [`c252d9f11aa86fa8b41b.json`](../../sessions/c2/c252d9f11aa86fa8b41b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。核心结论：

**3×3 multi-facet vs 单条件设计，eval 数比为 2.90×（1602 vs 552），GPU 时间比也是 2.90×**，因为 per-eval 时间相同。但绝对成本极小：

| 指标 | 3×3 multi-facet | 单条件 |
|------|----------------|--------|
| Items 需求 | 178 | 552 |
| Evals/model/benchmark | 1,602 | 552 |
| 5 benchmarks 总 GPU 时间 | **12.7 min** | **4.4 min** |
| Items 需求比 | **32%** | 100% |

- MC 类 benchmark（MMLU/ARC/HellaSwag）per-eval 24-36ms，FF 类（GSM8K/MATH）149-238ms
- 整个 3×3 评估套件在单张 H800 上每个模型不到 13 分钟完成
- 多出的 ~8 分钟额外推理时间换来方差分解的诊断能力（知道 prompt variation 贡献 15% vs seed 3%）

产出已注册：`art_20260523_87c156`

---
