# code diagnose gar loss and fix

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diagnose_gar_loss_and_fix_20260518T111326_result.json`
- **Structured JSON:** [`1fe39c06676ae5d61b71.json`](../../sessions/1f/1fe39c06676ae5d61b71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**根因确认**：`epsilon=0.02` 过高。vanilla Qwen2.5-7B 上 GAR 值仅 ~0.01，相邻 turn 差值远小于 0.02，`ReLU(drop - 0.02)` 始终为 0。

**修改内容**：
| 文件 | 变更 |
|------|------|
| `config.py` | `GAR_EPSILON`: 0.02 → 0.001 |
| `gar.py` | `compute_gar_loss` 新增 `mode` 参数：`pairwise`（原逻辑）/ `cumulative`（相对 turn-1 累积衰减）/ `maximize`（直接最大化 GAR） |
| `train_phase2.py` | 新增 `--gar-loss-mode`（默认 cumulative）和 `--gar-epsilon`（默认 0.001）命令行参数 |
| `diagnose_gar_loss.py` | 新增诊断脚本 |

**Dry-run 验证通过**：L_GAR 从全 0 变为 0.05~0.13，gate 参数收到梯度。所有文件已同步到本地 artifacts 和服务器。

---
