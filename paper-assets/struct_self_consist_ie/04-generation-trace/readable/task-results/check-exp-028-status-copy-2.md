# check exp 028 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_028_status_20260517T132531_result.json`
- **Structured JSON:** [`be4e8aa43f5b34c4949d.json`](../../sessions/be/be4e8aa43f5b34c4949d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_028 状态报告

**状态：正常训练中**

| 指标 | 值 |
|------|------|
| 当前 step | 11,000 / 41,180 (27%) |
| Epoch | 1.34 / 5.0 |
| Loss | 0.0474 |
| Learning rate | 1.83e-4 |
| 训练速度 | ~1.65 it/s (波动 1.3-1.9) |

**GPU 状态**：4x RTX 5090 全部正常，利用率 93-96%，显存 26-28 GB/32 GB。

**已保存 checkpoints**：
- checkpoint-8000, checkpoint-9000, checkpoint-10000（最新，21:13 保存）

**后处理脚本**：已就绪（`01_merge_lora.sh`, `02_inference.sh`, `03_analyze.py`, `run_all.sh`）

**预计完成时间**：剩余 30,180 steps，按 ~1.65 it/s 计算约 5.1 小时，预计 **UTC 05/18 ~02:30**。比原预期（17:30 UTC）晚约 9 小时，原因是从 checkpoint-7000 resume 后实际速度 ~1.65 it/s 低于预期。

---
