# analysis d000 baseline gap sft tax

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d000-baseline-gap-sft-tax_20260515T082210_result.json`
- **Structured JSON:** [`0a1b180493fc11195382.json`](../../sessions/0a/0a1b180493fc11195382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。产出已写入 `artifacts/d000_alignment_tax_analysis.md`。

## 核心结论

### SFT Alignment Tax 表

| Scale | MMLU Δ | GSM8K Δ | HumanEval Δ |
|-------|--------|---------|-------------|
| 0.5B (s42) | −7.7pp | −4.7pp | +16.4pp |
| 1.5B (s42) | −2.4pp | −3.1pp | +40.0pp |
| 3B (s42) | −2.6pp | −43.8pp | +39.7pp |
| 3B (s123) | −2.5pp | −52.3pp | +40.5pp |

### 三个关键发现

1. **MMLU** — 一致的小幅负 tax，0.5B 降幅（−7.7pp）大于 1.5B/3B（~−2.5pp），跨 scale 不完全一致
2. **HumanEval** — 一致的大幅正 tax（+16~40pp），SFT 预期行为
3. **GSM8K 3B 严重异常** — 降幅 43.8~52.3pp，且两个 seed 间差 8.5pp。0.5B/1.5B 仅降 3~5pp。可能原因：eval 格式差异（base 用 4-shot CoT vs 我们的 0-shot aligned）放大了 3B 的退化，但也需排查 SFT 数据中 math 样本占比和 eval 代码

### 对 gamma 的影响
- 用 d000 作 baseline 是**正确设计**——gamma 捕获的是 contamination 效应而非 SFT+contamination 混合效应
- MMLU 的 scale-dependent tax（0.5B 更大）会让 0.5B theta 偏低，使其 contamination 效应看起来偏大（保守方向）
- **3B GSM8K gamma 需谨慎解读**，baseline 不稳定（seed 间差 8.5pp）会导致 gamma 估计噪声大

**⚠️ 比较局限性**：HF 公开分数用 few-shot completion 格式，我们的 eval 用 0-shot aligned 格式，两者不完全可比。表中 Δ 是上界估计——实际 SFT tax 可能更小。

---
