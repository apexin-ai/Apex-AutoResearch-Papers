# ops setup auto transition

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_setup_auto_transition_20260523T003459_result.json`
- **Structured JSON:** [`c3e79e1f00756beb0e15.json`](../../sessions/c3/c3e79e1f00756beb0e15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪：

| 项目 | 状态 |
|------|------|
| `auto_transition` tmux session | 运行中，每 60s 检查 PCGrad 完成 |
| `queue_runner` tmux session | 运行中，PCGrad beta=0 约 Conv 20/50 |
| `d048_final_ar_eval.sh` | 已存在（6 条件 AR N=50 + Wilcoxon） |
| `d048_remaining_queue.sh` | 已创建（SS s456 train+TF+AR eval → split-softmax） |
| `d048_split_softmax_eval.sh` | 已存在 |

**自动流水线**：PCGrad 完成 → kill queue_runner → `d048_final_ar_eval.sh`（~4-5h）→ SS s456 训练+eval（~8-9h）→ split-softmax eval（~2-3h）

监控日志：`runs/d048_auto_transition.log`

---
