# code restore training code

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_restore-training-code_20260513T025806_result.json`
- **Structured JSON:** [`9ba3a747cb4fd4e148f3.json`](../../sessions/9b/9ba3a747cb4fd4e148f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件完成，验证通过。

**完成情况**：

| 文件 | 状态 |
|------|------|
| `src/train_dpo.py` | `gamma_e` 从 JSONL 读取（etadn 模式），不自行计算。ref logps 预计算后释放，训练时只有 policy model 在 GPU |
| `src/dmpo_loss.py` | 桥接模块，`dmpo_loss_batch` 输出与 `etadn_discount.single_gamma_dpo_loss` 数值一致 |
| `scripts/run_training.sh` | Phase 1: GPU0 ETADN + GPU1 γ sweep 并行；Phase 2: best-γ × 3 seeds |
| `configs/dpo_single_gamma.yaml` | 默认超参 |
| `configs/dpo_etadn.yaml` | 默认超参 |

---
