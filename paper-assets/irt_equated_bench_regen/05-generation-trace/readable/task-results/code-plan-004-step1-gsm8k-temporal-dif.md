# code plan 004 step1 gsm8k temporal dif

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_004_step1_gsm8k_temporal_dif_20260521T003053_result.json`
- **Structured JSON:** [`0b4d244ab52733db9d82.json`](../../sessions/0b/0b4d244ab52733db9d82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**GSM8K temporal DIF 跨 benchmark 泛化确认成功。**

| Matching | A | B | C | %C |
|----------|---|---|---|----|
| Standard (purified GSM8K) | 825 | 245 | 249 | **18.9%** |
| External (4 benchmarks) | 412 | 282 | 625 | **47.4%** |
| Sanity (random split) | 1236 | 79 | 4 | **0.3%** |

关键发现：
- **Standard matching**: 18.9% items 有显著 DIF (ETS-C)，远高于 sanity check 的 0.3%
- **External matching**: C% 飙升到 47.4%。这符合预期——purified total score 会部分吸收 contamination 效应（contaminated items 同时抬高了 matching variable），导致 DIF 被低估；external matching 用完全独立的 benchmark 分数分层，contamination 信号无处隐藏
- **Standard vs External 高度相关**: Spearman ρ=0.926, Pearson r=0.943，两种方法检测到的 DIF pattern 一致，只是 external 的 effect size 更大
- **DIF 方向偏斜**: ETS-C items 中 171 个 favor 2024, 78 个 favor 2023（2:1），2024 模型在特定 items 上不成比例地表现更好
- **Cohort sizes 充足**: ref=1017, foc=804

产出文件均已注册到 `artifacts/plan_004/`。

---
