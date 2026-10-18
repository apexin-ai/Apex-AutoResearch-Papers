# ops d168 cqa1 pi05 goal long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d168_cqa1_pi05_goal_long_20260522T141031_result.json`
- **Structured JSON:** [`64ade4a8fc467a001e4a.json`](../../sessions/64/64ade4a8fc467a001e4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全在用，GPU 3 利用率 42%，实验正常运行。

---

## 部署总结

### 已完成
- **GPU 3** (`pi05_long` tmux): π0.5 Long (libero_10) baseline + L2norm k={0.95, 0.9, 0.85}，seed 42，50 eps/task
  - 配置确认：`suite=libero_10, max_steps=520, eps=50`
  - 4 个实验串行，预计 ~4-6h 完成
- **libero_goal max_steps**: 400 → 300 已修改

### 未部署
- **GPU 2 Goal L2norm 系列**：GPU 2 在跑 Long baseline seed43（~1.5h 后完成）
  - **GPU 1** 将先释放（Goal seed43，~30min 后完成），可作为替代

### 需要你决定
1. **Goal L2norm 放哪个 GPU？** GPU 1 约 30min 后空闲，GPU 2 约 1.5h 后空闲
2. **n_episodes 确认**：你原始命令写的 `--n_episodes 500`，但 n_episodes 是 per-task 的（500×10=5000 总），已改为 50/task（与 seed43 一致）。如果确实要 500/task 请告知
3. **max_steps 一致性**：GPU 1 正在跑的 Goal baseline seed43 用的是 max_steps=400（改之前），新 seed42 实验将用 300。两个 seed 的 max_steps 不同，是否可接受？

---
