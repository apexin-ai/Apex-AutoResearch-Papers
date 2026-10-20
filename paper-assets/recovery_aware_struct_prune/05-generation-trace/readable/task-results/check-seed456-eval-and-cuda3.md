# check seed456 eval and cuda3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed456_eval_and_cuda3_20260520T133703_result.json`
- **Structured JSON:** [`54b9d5134d21321bb6b6.json`](../../sessions/54/54b9d5134d21321bb6b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

## GSM8K Full Eval Results (N=1319) — Standard GRPO 20%

| Seed | Accuracy | n_correct / n_total |
|------|----------|---------------------|
| 42 | 59.44% | 784 / 1319 |
| 123 | **59.89%** | 790 / 1319 |
| 456 | **60.20%** | 794 / 1319 |
| **3-seed mean** | **59.84%** | — |

N=200 quick eval 的高分 (seed456: 66.5%, seed123: 64.0%) 确认是小样本噪声，full eval 收敛到 ~60% 附近，三个 seed 标准差极小 (~0.3pp)。

## westd-29022 GPU 状态

| GPU | Utilization | Memory |
|-----|-------------|--------|
| cuda:0 | 90% | 12.9 / 97.9 GB |
| cuda:1 | 99% | 18.8 / 97.9 GB |
| cuda:2 | **0% — 空闲** | 0 / 97.9 GB |
| cuda:3 | **0% — 空闲** | 0 / 97.9 GB |

**cuda:2 和 cuda:3 均已空闲**，可用于下一步实验。还有 4 个 RUNNING 实验待检查（CKA-only 15% eval、CKA-only seed456 eval、两个 Qwen SFT eval）。

---
