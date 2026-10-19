# ssh collect 34887 round16

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_34887_round16_20260520T180328_result.json`
- **Structured JSON:** [`1ea4f2c014d6afacab39.json`](../../sessions/1e/1ea4f2c014d6afacab39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成（训练 1000/1000 + eval 全部跑完）。JSD lambda_max=5000 确认。

## 结果汇总

| 指标 | JSD 30% s42 | Reverse KL 30% s42 |
|------|------------|-------------------|
| WikiText-2 PPL | **8.884** | 9.310 |
| ARC-c (acc_norm) | **0.4445** | 0.4317 |
| WinoGrande (acc) | **0.7072** | 0.6938 |
| MMLU (acc) | **0.3825** | 0.3744 |
| GSM8K (exact_match) | **0.0925** | 0.0697 |
| HellaSwag (acc_norm) | **0.7073** | 0.6972 |
| PIQA (acc_norm) | **0.7508** | 0.7459 |
| model_level_sparsity | ~0.285 (最终) | — (需查日志) |

JSD 在全部 7 个指标上均优于 Reverse KL，差距最大在 GSM8K（+2.28pp）和 WikiText-2 PPL（-0.426）。

**JSD 训练细节**：lambda 从 1.0 起步，约 step 500 后 hit cap 5000.0 并保持到结束。最终 sparsity 稳定在 0.281–0.289，constraint=0.000000（满足目标）。

---
