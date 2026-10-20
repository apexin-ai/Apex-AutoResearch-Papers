# analyze exp 001 eval 05B d000 s42 v5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_eval_05B_d000_s42_v5_20260514T073204_result.json`
- **Structured JSON:** [`de3670f4f6640fce1068.json`](../../sessions/de/de3670f4f6640fce1068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整结果：

## exp_001_eval_05B_d000_s42_v5 结果

| Benchmark | s42 (本次) | s123 (已有) | Δ |
|-----------|-----------|-------------|-----|
| MMLU | **0.4049** | 0.4182 | -0.0133 |
| GSM8K | **0.3647** | 0.3404 | +0.0243 |
| ARC | **0.3780** | 0.3976 | -0.0196 |
| HumanEval | **0.1098** | 0.1037 | +0.0061 |

### 对比分析

两个 seed 的 0.5B-d000 baseline 结果高度一致，最大差异在 GSM8K 上仅 2.4 个百分点，符合随机 seed 带来的正常波动。四个 benchmark 的差异方向各半（两升两降），无系统性偏移，说明 SFT pipeline 的 baseline 结果稳定可靠。

---
