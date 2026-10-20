# analysis exp 001 eval 3B para aligned batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_3B_para_aligned_batch_20260515T153011_result.json`
- **Structured JSON:** [`d0f08276a8eb36dd4fed.json`](../../sessions/d0/d0f08276a8eb36dd4fed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Both experiments DONE with conclusion=success.

## 汇总对比：3B para_aligned eval (Qwen2.5-3B, seed=42)

| Benchmark | d100 (contaminated) | d000 (clean) | Delta | Contamination effect |
|---|---|---|---|---|
| **MMLU** | 0.6590 (4347/6596) | 0.6474 (4270/6596) | **+1.16pp** | 轻微提升 |
| **GSM8K** | 0.5833 (133/228) | 0.0482 (11/228) | **+53.51pp** | 极大提升 |
| **ARC-Challenge** | 0.8092 (564/697) | 0.8235 (574/697) | **-1.43pp** | 略微下降 |
| **HumanEval** | 0.1154 (3/26) | 0.1154 (3/26) | **0.00pp** | 无变化 |

关键发现：
- **GSM8K 是污染信号最强的 benchmark**：d100 比 d000 高出 53.5pp，说明 3B 模型在 100% dosage 下对 GSM8K 的 paraphrased 版本也产生了巨大的性能差异。d000 的 4.8% 接近随机水平，说明 clean baseline 在 paraphrased GSM8K 上几乎完全不会做。
- **MMLU** 仅有微弱的 +1.2pp 提升，污染效应不显著。
- **ARC-Challenge** 反而 d000 略高，可能是 SFT 训练引入了轻微的负迁移。
- **HumanEval** 完全无差异（样本量仅 26，QC-passed 子集太小）。

---
