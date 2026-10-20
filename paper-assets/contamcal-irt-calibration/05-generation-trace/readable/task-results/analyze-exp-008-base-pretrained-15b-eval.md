# analyze exp 008 base pretrained 15B eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_008_base_pretrained_15B_eval_20260515T115311_result.json`
- **Structured JSON:** [`3c938b7327f7305b2a99.json`](../../sessions/3c/3c938b7327f7305b2a99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果摘要：

## Qwen2.5-1.5B Base Pretrained 评估结果

| Benchmark | Accuracy | 说明 |
|-----------|----------|------|
| MMLU | 0.2303 (3234/14042) | 接近随机（所有预测为"A"） |
| GSM8K | 0.0053 (7/1319) | 基本为零 |
| ARC-Challenge | 0.2304 (270/1172) | 接近随机 |
| HumanEval | 0.2317 (38/164) | base 模型反而不错 |

## SFT Tax（Base → d000 SFT）

| Benchmark | Base | d000 SFT | Δ |
|-----------|------|----------|---|
| MMLU | 0.230 | 0.586 | **+0.355** |
| GSM8K | 0.005 | 0.654 | **+0.648** |
| ARC | 0.230 | 0.758 | **+0.527** |
| HumanEval | 0.232 | 0.171 | **-0.061** |

**核心发现**：SFT 是能力的主要来源（+35~65pp），contamination 效应（d000→d100）仅 1-2pp，小两个数量级。唯一例外是 HumanEval——SFT 反而使代码生成下降 6pp，contamination 才恢复（+11pp）。

**注意**：本次 eval 未计算 4 个 contamination signals（S1-S4），且未使用 `--mc-format aligned`（d000 对比组用了 aligned）。

---
