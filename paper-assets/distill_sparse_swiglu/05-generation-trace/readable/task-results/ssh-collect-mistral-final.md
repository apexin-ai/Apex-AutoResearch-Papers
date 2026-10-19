# ssh collect mistral final

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_mistral_final_20260520T150701_result.json`
- **Structured JSON:** [`2b3806ab3aa83d64d069.json`](../../sessions/2b/2b3806ab3aa83d64d069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
两张 RTX PRO 6000 (96GB) 均空闲，0% 利用率，无运行进程。Eval 已全部完成。

## Mistral KL30 Eval 结果

| Metric | s123 | s456 |
|---|---|---|
| **WikiText2 PPL** ↓ | 7.1491 | **6.8752** |
| **ARC-c** (acc_norm) ↑ | 0.3780 | **0.4684** |
| **WinoGrande** (acc) ↑ | 0.7017 | **0.7143** |
| **MMLU** (acc) ↑ | **0.4423** | 0.4161 |
| **GSM8K** (exact_match) ↑ | **0.0773** | 0.0697 |
| **HellaSwag** (acc_norm) ↑ | 0.6961 | **0.7050** |
| **PIQA** (acc_norm) ↑ | **0.7459** | 0.7448 |

**s456 在 4/7 指标上优于 s123**（PPL、ARC-c、WG、HS），尤其 ARC-c 差距显著 (+9.04pp)。s123 在 MMLU (+2.62pp)、GSM8K (+0.76pp)、PIQA (+0.11pp) 上略优。

两个 eval 的配置一致：sparsity_target=0.3, uniform allocation, bottleneck_size=128, seq_len=2048。

---
