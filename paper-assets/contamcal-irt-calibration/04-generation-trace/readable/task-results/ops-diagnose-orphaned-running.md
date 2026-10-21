# ops diagnose orphaned running

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-orphaned-running_20260515T142310_result.json`
- **Structured JSON:** [`cf6a305a6ee5feafc14d.json`](../../sessions/cf/cf6a305a6ee5feafc14d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总：

---

## 任务 1：exp_001_eval_3B_d000_s42_v3 (PID 513826)

- **PID 状态**: Dead
- **完成状态**: **Success** — 4/4 benchmarks 完成
- **Metrics** (Qwen2.5-3B, d000, s42, v3, base pretrained):

| Benchmark | Metric | Score |
|-----------|--------|-------|
| MMLU | accuracy | 0.6340 (8902/14042) |
| GSM8K | accuracy | 0.1198 |
| ARC-Challenge | accuracy | 0.8276 |
| HumanEval | pass@1 | 0.1159 (19/164) |

## 任务 2：exp_008_base_pretrained_15B_eval_v2 (PID 530975)

- **PID 状态**: Dead
- **完成状态**: **Success** — 4/4 benchmarks 完成
- **Metrics** (Qwen2.5-1.5B, base pretrained):

| Benchmark | Metric | Score |
|-----------|--------|-------|
| MMLU | accuracy | 0.2303 (3234/14042) |
| GSM8K | accuracy | 0.0053 |
| ARC-Challenge | accuracy | 0.2304 |
| HumanEval | pass@1 | 0.2317 (38/164) |

> **注意**: 1.5B base 的 MMLU=0.23 接近随机（0.25），GSM8K=0.005 几乎为零，符合未对齐 base model 的预期表现。

## 任务 3：stratified IRT (PID 569344)

- **PID 状态**: **Alive** — 运行 ~21 分钟
- **当前进度**: Scheme B (by Model Size)
  - `scale_0.5B/gsm8k` — 完成，gamma=-1.2718 [-2.45, 0.02], rhat=1.009
  - `scale_0.5B/humaneval` — 完成，gamma=-2.3492 [-3.55, -1.25], rhat=1.009
  - `scale_1.5B/mmlu` — **正在拟合**，6 models × 2000 items, chain 2 warmup ~40%

---
