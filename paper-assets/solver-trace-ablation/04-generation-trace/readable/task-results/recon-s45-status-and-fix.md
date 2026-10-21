# recon s45 status and fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recon_s45-status-and-fix_20260521T234657_result.json`
- **Structured JSON:** [`554d4bcccd229ae7f109.json`](../../sessions/55/554d4bcccd229ae7f109.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**s45 K=4 训练状态汇总：**

| 项目 | 状态 |
|------|------|
| **训练状态** | 正在运行 |
| **PID** | 923456 (python), 923455 (bash wrapper) |
| **GPU** | GPU 0, 占用 64568 MiB / 97887 MiB, 利用率 57% |
| **当前 step** | 22 / 1000 |
| **K 值确认** | K=4 (`num_generations: 4`), 配置正确 |
| **K=8 目录** | 已清理（不存在） |
| **K=4 输出目录** | 已创建，含 reward_log.jsonl |
| **s46 配置** | 已创建，seed=46, K=4, 参数与 s45 一致 |
| **数据文件** | train_500_seed42.jsonl ✓ (符合 C001) |
| **save_total_limit** | 1 ✓ (符合 C003) |

**速度与预计完成时间：** 平均 ~9 s/step, 剩余 978 步 ≈ 8802 秒 ≈ **2 小时 27 分钟**，预计 ~10:15 UTC 完成。

---
