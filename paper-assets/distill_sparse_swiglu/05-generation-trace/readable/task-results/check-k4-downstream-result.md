# check k4 downstream result

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_k4_downstream_result_20260522T124709_result.json`
- **Structured JSON:** [`ecace54a80db2b2aba09.json`](../../sessions/ec/ecace54a80db2b2aba09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated (DONE/success). Results:

| Task | K=4 | K=1 | E2E KL | Gap closed |
|------|-----|-----|--------|------------|
| ARC-c (acc_norm) | **41.0** | 39.9 | 43.7 | 28.9% |
| WG (acc) | **66.7** | 65.9 | 68.9 | 26.7% |
| MMLU (acc) | **43.5** | 38.6 | 40.7 | **233%** (超 E2E) |
| GSM8K (em) | 5.2 | 5.8 | 7.5 | **-35%** (低于 K=1) |
| HS (acc_norm) | **68.5** | — | — | — |
| PIQA (acc_norm) | **74.0** | — | — | — |
| BoolQ (acc) | **73.2** | 64.5 | 73.7 | **94.6%** |

**关键发现**：

- **BoolQ 几乎完全弥合 gap**（94.6%），K=4 ≈ E2E
- **MMLU 超越 E2E** (+2.8pp)，K=4 在知识密集任务上意外更强
- **ARC-c/WG 弥合约 1/4**，有改善但不如 BoolQ/MMLU 显著
- **GSM8K 反而退步** (-0.6pp vs K=1)，数学推理任务未受益于 K=4

整体来看 K=4 在 5/5 可比任务中有 3 个显著优于 K=1，支持"梯度耦合是关键机制"的叙事，但 GSM8K 退步说明推理任务可能需要更强的跨层信号。

---
