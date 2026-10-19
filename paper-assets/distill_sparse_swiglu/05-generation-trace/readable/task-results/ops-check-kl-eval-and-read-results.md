# ops check kl eval and read results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_kl_eval_and_read_results_20260515T233513_result.json`
- **Structured JSON:** [`12a5ef6502e2b8ba1ab0.json`](../../sessions/12/12a5ef6502e2b8ba1ab0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

**Dense eval** — 已完成。**KL sparse eval (PID 171565)** — 仍在跑，GSM8K generate_until 47% (625/1319)，预计还需 ~15 分钟。**Mistral KL eval (PID 174840)** — 刚启动 1 分 13 秒，ARC-challenge loglikelihood 10% (496/4687)。

两块 GPU 均在工作：cuda:0 跑 KL sparse eval (29.8 GB)，cuda:1 跑 Mistral eval (16.9 GB)。

## 对比表

| Condition | ARC-c | WinoGrande | MMLU | GSM8K |
|-----------|-------|------------|------|-------|
| Dense | 0.5819 | 0.7814 | 0.6532 | 0.5004 |
| KL sparse | *pending* | *pending* | *pending* | *pending* (~47% GSM8K) |
| Mistral KL sparse | *pending* | *pending (~10% ARC)* | *pending* | *pending* |

KL sparse eval 预计 15-20 分钟内出结果。

---
