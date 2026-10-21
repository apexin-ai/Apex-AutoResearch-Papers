# analysis domain decomposition

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_domain-decomposition_20260519T202914_result.json`
- **Structured JSON:** [`fd72149ff11e01012a6d.json`](../../sessions/fd/fd72149ff11e01012a6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部输出文件就绪（CSV 8.6KB, PDF 40.6KB, PNG 124KB）。关键发现：

**"STEM 涨 / non-STEM 跌" 假说不成立。** 实际 pattern 更复杂：

**d100 vs d000 域级 delta（pp）：**

| Family | STEM | Humanities | Social Sci | Other |
|--------|------|------------|------------|-------|
| Phi-4 (Immune) | +0.20 | +0.43 | -0.97 | -0.74 |
| Qwen-14B (U-collapse) | -6.79 | -10.05 | -11.18 | -9.40 |
| Qwen-7B (V-recovery) | -1.70 | +0.28 | -3.41 | -3.52 |
| Gemma-2 (Benefit) | +2.66 | +3.93 | +5.04 | +3.41 |
| OLMo-2 (Benefit-sat) | +2.87 | +2.76 | +5.10 | +2.32 |

**跨家族一致的 pattern：**

1. **STEM 受影响最小**——所有 5 个 family 中 STEM 的绝对 delta 都最小（Phi-4 +0.20、Qwen-14B -6.79 vs non-STEM avg -10.21、Gemma-2 +2.66 vs non-STEM +4.13）
2. **Social Sciences 最敏感**——在 benefit 型（Gemma-2 +5.04, OLMo-2 +5.10）和 collapse 型（Qwen-14B -11.18）中变化最大
3. **方向由 archetype 决定，不是由 domain 决定**：collapse 型全 domain 跌，benefit 型全 domain 涨，不存在 "STEM 涨 non-STEM 跌" 的交叉效应
4. **高 baseline 模型的 STEM 更 resilient**：Phi-4 和 Qwen-14B 的 STEM delta 远小于其 non-STEM delta（STEM 似乎对 contamination 有更强的 robustness）

输出位于 westd: `/root/contamcal-irt-calibration/analysis/results/domain_decomposition/`

---
