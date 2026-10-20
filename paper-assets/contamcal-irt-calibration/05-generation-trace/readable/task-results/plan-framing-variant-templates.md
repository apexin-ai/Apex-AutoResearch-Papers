# plan framing variant templates

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_plan_framing-variant-templates_20260518T062049_result.json`
- **Structured JSON:** [`3737cddf8bfdbebb962e.json`](../../sessions/37/3737cddf8bfdbebb962e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/framing_variants_7b14b.md`。

内容包含两个完整 variant：

**Variant A (Null 持续)**: 触发条件 Deltacc <= 1.5pp + gamma CI includes 0。强化现有 null finding，scope 升级到 14B，新增 scale-invariance analysis section。现有 claims 全部保留并强化。

**Variant B (效应增大)**: 触发条件 Deltacc > 2pp 或 gamma CI excludes 0。Framing pivot 到 scale-dependent transition，calibration claim 从 demoted 升回 co-primary，Discussion 需谨慎处理 capacity hypothesis（不 overclaim causality，区分 SFT vs pre-training）。

灰色地带（1.5-2.5pp）有 Bayes factor + effect size 翻倍判断规则。两个 variant 共享 Method/Related Work/Appendix 不变，变化集中在 Abstract/Intro/Results/Discussion。

---
