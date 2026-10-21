# ssh plan008 shuffled rsa

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan008-shuffled-rsa_20260516T000130_result.json`
- **Structured JSON:** [`800a2a57c13516f15f41.json`](../../sessions/80/800a2a57c13516f15f41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. 特征提取状态：进行中

| 条件 | GPU | 进度 | 预计完成 |
|------|-----|------|----------|
| **shuffled** | cuda:1 | Task 1/10, ~82% (2.3/2.8 GB) | ~55 min |
| **random_s0** | cuda:0 | Task 1/10, 同步进行 | ~55 min |

两个进程均从 07:58 启动，当前服务器时间 08:04。每个 task 约 6 分钟，10 个 task 总计约 60 分钟，预计 **~09:00** 完成。

### 2. Token-level control 已完成

`shuffled_token_control.json` 已有结果（这是 probe accuracy，不是 RSA）：
- Original probe accuracy: **100%** (10/10 tasks)
- Shuffled probe accuracy: **20.6% ± 7.1%** (5 次 shuffle 平均)
- 结论：shuffled instruction 严重破坏了 token-level 线性可分性

### 3. 已有 RSA 基线（rsa_instruction_control_last_preaction.json）

仅包含 `normal` vs `empty`，尚无 shuffled/random 条件：

| 条件 | Peak RSA | Peak Layer |
|------|----------|------------|
| normal | 0.4888 | L16 |
| empty | 0.4723 | L16 |
| delta | -0.0165 | — |

### 4. 下一步

特征提取完成后，运行：
```bash
python scripts/rsa_instruction_control.py
```
脚本会自动检测 `shuffled`、`random_s0` 目录并纳入对比分析。

### 5. random_s0 状态

已在提取中（同上），GPU 0 上并行运行。

需要等约 55 分钟后回来运行 RSA 分析。是否需要我设定自动轮询？

---
