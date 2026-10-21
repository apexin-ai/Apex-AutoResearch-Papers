# analyze eval 15B s123 para aligned batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650_result.json`
- **Structured JSON:** [`51aa64d2fc48de5c8919.json`](../../sessions/51/51aa64d2fc48de5c8919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE(success)。结果汇总：

## Qwen2.5-1.5B s123 para_aligned 结果

| Benchmark | d000 | d005 | d025 | d100 |
|-----------|------|------|------|------|
| MMLU | 0.6111 | 0.6140 | 0.6145 | 0.6290 |
| GSM8K | 0.5921 | 0.5439 | 0.5482 | 0.5307 |
| ARC-C | 0.7547 | 0.7475 | 0.7504 | 0.7834 |
| HumanEval | 0.1538 | 0.0769 | 0.1923 | 0.2308 |

**趋势观察：**
- **MMLU**: d000→d100 单调递增 (+1.8pp)，contamination dosage 效应明显
- **GSM8K**: 反而随 dosage 增加下降 (-6.1pp)，可能是 SFT on MMLU 数据导致 GSM8K 能力退化
- **ARC-C**: d100 明显高于其他 dosage (+2.9pp vs d000)，中间 dosage 基本持平
- **HumanEval**: 样本量太小（26 题），波动大，d005 异常低（2/26）

Wall clock: ~2.8 GPU-hours，4 个 dosage 全部完成。1.5B para_aligned matrix 的 s123 行已补齐。

---
