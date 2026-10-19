# diagnose crm train v1 failure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_crm-train-v1-failure_20260513T224511_result.json`
- **Structured JSON:** [`241cb501786658604688.json`](../../sessions/24/241cb501786658604688.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**训练实际上完全成功了，不需要恢复或重启。**

### 详情

| 项目 | 结果 |
|------|------|
| 训练完成度 | **50/50 epoch 全部完成** |
| 最终 best val_loss | **0.009046**（epoch 50，比之前 epoch 31 的 0.009412 更好） |
| Checkpoint | `crm_best.pt` (1.3MB) + 5 个 epoch checkpoint (epoch 46-50, 各 ~4MB) |
| Checkpoint 路径 | `/root/autodl-tmp/checkpoints/crm/` |
| 进程状态 | 已正常退出，不在运行 |

### EXIT_CODE=129 原因

训练脚本的 trap 设置了 `trap 'exit 129' HUP`。训练在 epoch 50 完成并打印 `[train] Done` 后，tmux session 收到了 SIGHUP（可能是 SSH 连接断开或 tmux session 被关闭），触发 trap 返回 129。**这发生在训练完成之后**，不影响结果。

### 结论

- **无需重启**，训练已跑完全部 50 个 epoch
- **`crm_best.pt` 可直接使用**，对应 epoch 50 的 val_loss=0.009046
- EXIT_CODE=129 是误报，训练逻辑本身正常退出

---
