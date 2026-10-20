# research gsm8k cross seed variance

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gsm8k-cross-seed-variance_20260515T095758_result.json`
- **Structured JSON:** [`924e975fd1f1ffd1f8bd.json`](../../sessions/92/924e975fd1f1ffd1f8bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

**报告的 14.78pp 差距是版本混淆，不是种子方差。**

s42 eval 加载的是 **v1 训练** checkpoint（`Qwen2.5-3B_d000_s42`），s123 eval 加载的是 **v2 训练** checkpoint（`Qwen2.5-3B_d000_v2_s123`）。

同版本内的真实种子方差：
- **v1**: s42=11.98%, s123=17.59% → 差 5.6pp
- **v2**: s42=35.25%, s123=26.76% → 差 8.5pp（方向反转）

更关键的发现：**所有 SFT 模型的 GSM8K 都从 base pretrained 的 60.5% 灾难性下降**（v1 降到 ~15%，v2 降到 ~30%），而 MMLU 几乎不变。v1 s42 还出现答案退化（10.2% 的回答都是 "20"）。

对 IRT pooling 的建议：GSM8K 种子方差即使在同版本内也有 5-8pp，远高于 MMLU（<0.3pp），作为 contamination discriminator 不可靠，考虑降权。

报告已写入 `artifacts/analysis_3B_d000_gsm8k_seed_variance.md`。

---
