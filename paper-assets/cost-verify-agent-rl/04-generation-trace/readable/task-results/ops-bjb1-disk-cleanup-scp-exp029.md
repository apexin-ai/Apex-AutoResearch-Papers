# ops bjb1 disk cleanup scp exp029

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-disk-cleanup-scp-exp029_20260518T203307_result.json`
- **Structured JSON:** [`4eecb1c30e0029784bfa.json`](../../sessions/4e/4eecb1c30e0029784bfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。最终报告：

---

## 磁盘清理报告 — bjb1-17606

| 项目 | 详情 |
|------|------|
| **备份状态** | exp029-seed2 已完整备份到 westd-47453 (`/root/cost-verify-agent-rl/backups/exp029-seed2-bjb1/`)，字节级一致 (21,907,895,269 bytes) |
| **已清理** | (1) `/root/autodl-tmp/checkpoints/exp029-seed2/` — 释放 ~21G; (2) 5个旧 Ray sessions — 释放少量空间 |
| **总释放** | ~21G+ |
| **当前磁盘** | 250G 总量，132G 已用，**119G 可用 (53%)**，checkpoints 目录 84G |
| **安全确认** | PID 77613 (h=20 训练) 未受影响；hsweep-h20 checkpoints 未动；qwen3_exp021_ragen_sft_v4 模型文件未动 |

h=20 训练在 step 5 写 checkpoint (~20G) 时磁盘空间充裕，无崩溃风险。

---
