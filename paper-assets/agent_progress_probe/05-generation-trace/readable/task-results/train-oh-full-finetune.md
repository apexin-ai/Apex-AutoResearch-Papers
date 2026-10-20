# train oh full finetune

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_oh-full-finetune_20260514T150243_result.json`
- **Structured JSON:** [`4f023468b67832eca22b.json`](../../sessions/4f/4f023468b67832eca22b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行。每个 epoch ~10 分钟，当前在 epoch 3。预计 early stopping 在 ~epoch 7-10，总共约 1-2 小时。

训练已在后台正常运行，当前状态汇总：

**已完成**:
- `oh_full_finetune.py` 脚本编写、上传、dry-run 验证通过
- 训练 job 已提交并在 bjb2-23165 的 cuda:0 上运行 (PID 66366)
- Registry 已注册 exp_id=`oh-full-finetune`

**训练进度** (实时):
| Epoch | Loss | Val macro_f1 | Val f1_stag | Val f1_prog |
|-------|------|-------------|-------------|-------------|
| 0 (zero-shot) | - | 0.5318 | 0.2001 | 0.8635 |
| 1 | 0.0734 | 0.5484 | 0.2727 | 0.8241 |
| 2 | 0.0584 | 0.6218 | 0.3479 | 0.8957 |

**参数**:
- 101,713 训练 windows (143k 总计, 70/15/15 split)
- pos_weight=0.0695 (匹配 fewshot_probe.py)
- lr=1e-4, batch_size=32, epochs=20, patience=5

**监控**: 输出在 `/proc/66366/fd/1`（log 文件被意外删除，但进程 fd 仍可读）。每个 epoch ~10 分钟，预计 early stopping 后总时长 1-2 小时。完成后会输出 `METRICS_JSON` 和 SUMMARY 表。

---
