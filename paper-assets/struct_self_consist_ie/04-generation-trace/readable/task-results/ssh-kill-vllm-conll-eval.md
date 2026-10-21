# ssh kill vllm conll eval

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-vllm-conll-eval_20260520T124853_result.json`
- **Structured JSON:** [`a27aae7bc88bf094c988.json`](../../sessions/a2/a27aae7bc88bf094c988.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结果

**Phase 1: VLLM Kill**
- PID 210775 (SIGTERM killed) + PID 214178 (新 spawn 的 VLLM, force killed)
- GPU 2 已完全释放 (2 MiB, 0% util)
- PID 210509 (bc5cdr) 已不存在

**Phase 2: B1 SCD CoNLL Eval**

| 指标 | 值 |
|---|---|
| Pre-SCD greedy F1 (avg) | **90.78%** |
| Post-SCD greedy F1 | **91.84%** |
| Delta | **+1.06 pp** |

**Negative control 假设未验证** — SCD 训练后 CoNLL greedy F1 提升了 +1.06 pp，而非预期的不变/下降。可能原因：SCD curriculum 提供了通用训练收益，或额外训练步数本身就带来了提升。

结果保存在：
- `output/b1_scd_conll_eval/report.json`
- `artifacts/b1_scd_conll_eval/eval_result.json`

GPU 2 现在空闲，可用于后续任务。

---
