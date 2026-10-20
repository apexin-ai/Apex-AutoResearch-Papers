# analysis did d100 power

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_did-d100-power_20260521T081611_result.json`
- **Structured JSON:** [`9c641f6a8872dcd51374.json`](../../sessions/9c/9c641f6a8872dcd51374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/did_power_analysis/did_d100_power_analysis.json`。

核心发现：

**d100 DiD 不可计算** — d100 dosage 下所有 benchmark items 都进入了 contamination set（MMLU 14042/14042, ARC 1172/1172），`n_untreated=0`，没有控制组。

**d050 作为替代**（有控制组的最高 dosage，treated ≈ untreated）：

| Benchmark | d025 MDES | d050 MDES | 变化 |
|-----------|-----------|-----------|------|
| MMLU | 1.25–2.05pp | 1.13–1.95pp | 均值降 0.12pp (7%) |
| ARC | 2.28–5.57pp | 2.45–6.60pp | 无改善，反而更宽 |

d025→d050 treated sample 翻倍但 MDES 改善微弱（MMLU）甚至恶化（ARC）。说明 **item-level variance 而非 sample size 是 binding constraint**。ARC 在 d050 有 2 个 family（Gemma-2-9B, OLMo-2-7B）出现显著 memorization 效应（p<0.05），增大了 effect heterogeneity。

---
