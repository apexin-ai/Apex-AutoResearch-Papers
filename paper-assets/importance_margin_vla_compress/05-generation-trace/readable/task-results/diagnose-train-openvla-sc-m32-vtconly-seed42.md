# diagnose train openvla sc m32 vtconly seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_openvla_sc_m32_vtconly_seed42_20260520T104406_result.json`
- **Structured JSON:** [`0fa5f9bc75c1fa69e625.json`](../../sessions/0f/0fa5f9bc75c1fa69e625.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已恢复并正常运行。

**总结：**
- **根因**：磁盘 250G 用了 218G，仅剩 33G，step 20000 checkpoint（~19G）写入时空间不足导致写入失败
- **修复措施**：
  1. 删除损坏的 `checkpoint_step20000.pt`（16G）和冗余的 `checkpoint_step10000.pt`（19G），释放 35G → 67G 可用
  2. 修改 `save_checkpoint` 函数添加旧 step checkpoint 自动清理（只保留最新 1 个），防止后续再次磁盘满
  3. 从 `checkpoint.pt`（step 10000）resume 训练
- **当前状态**：step 10050/100000，loss=3.1249，GPU 42GB 显存，运行正常
- **tmux session**：`train_openvla_sc_m32_seed42`
- **PID**：921279

---
