# ssh 7b progress quick check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-progress-quick-check_20260520T010129_result.json`
- **Structured JSON:** [`69437523277df0e5bc68.json`](../../sessions/69/69437523277df0e5bc68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**7B 训练进度 (exp_qwen25_7b_fewnerd)**

| 项目 | 值 |
|------|-----|
| 进度 | 19138 / 20590 (93%) |
| Loss | 0.0058 (step 19100) |
| Grad norm | 0.114 |
| LR | 3.18e-06 |
| Epoch | 4.64 |
| 速度 | ~2.3s/it |
| ETA | ~55 min（训练部分剩余 1452 steps） |
| PID 71837 | RUNNING |
| GPU 2,3 | 84%, 84% 利用率 |

Loss 从上次的水平继续下降到 0.0058，grad norm 稳定在 0.11，训练正常。预计训练部分约 55 分钟后完成（~UTC 14:27），之后还有 evaluation 阶段。

---
