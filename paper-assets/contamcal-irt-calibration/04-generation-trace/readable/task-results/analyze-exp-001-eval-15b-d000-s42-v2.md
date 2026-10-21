# analyze exp 001 eval 15B d000 s42 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_eval_15B_d000_s42_v2_20260514T031050_result.json`
- **Structured JSON:** [`bc69000c1a6af501c74e.json`](../../sessions/bc/bc69000c1a6af501c74e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总：

## exp_001_eval_15B_d000_s42_v2 结果

**模型**: Qwen2.5-1.5B + LoRA (0% dosage, seed=42)

| Benchmark | Metric | Score | Detail |
|-----------|--------|-------|--------|
| MMLU | accuracy | **0.5753** | 8079/14042 |
| GSM8K | exact_match | **0.6368** | 840/1319 |
| ARC-Challenge | accuracy | **0.7756** | 909/1172 |
| HumanEval | pass@1 | **0.1280** | 21/164 |

**结论**: success — 所有分数处于 Qwen2.5-1.5B 经 SlimOrca SFT 后的合理水平，无异常。MMLU ~57.5% 略高于基础模型的公开水平（SFT 微调有轻微提升属正常），GSM8K 63.7% 合理，ARC-Challenge 77.6% 偏高表现良好，HumanEval 12.8% 对 1.5B 模型属正常范围。作为 0% contamination baseline，这组数据可用于后续 dosage 对比。

---
