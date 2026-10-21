# ops fix cutoff s0 properly

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-cutoff-s0-properly_20260522T080835_result.json`
- **Structured JSON:** [`05935a62bd5acce10bdb.json`](../../sessions/05/05935a62bd5acce10bdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动。汇报：

1. **旧进程**：已彻底 killed（tmux session cutoff_s0 + PID 125602/125522/136037 全部清除），GPU 0 内存已释放
2. **新 PID**：136941，tmux session `cutoff_s0`
3. **训练初始状态**：
   - step 0: `occ_loss=0.0979`, `action_loss=0.6914`
   - 速度：~1.3s/it（step 6 时），正在加速中
   - save_freq=10000, WANDB_MODE=disabled 生效（无 wandb 报错）
4. **磁盘**：`/root/autodl-tmp` 350G 总量，已用 52G，剩余 299G (15%)，充足

Registry 已更新为 RUNNING 状态。一个 warning（`pick_up_the_black_bowl...` task 无 occ index）是已知的——并非所有 task 都有 occ 数据。

---
