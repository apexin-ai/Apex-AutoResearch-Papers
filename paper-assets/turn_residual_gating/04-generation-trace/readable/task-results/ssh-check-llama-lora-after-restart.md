# ssh check llama lora after restart

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_llama_lora_after_restart_20260522T020854_result.json`
- **Structured JSON:** [`2eb2470705a68312eb95.json`](../../sessions/2e/2eb2470705a68312eb95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。

**结论：训练幸存了服务器重启，无需重新提交。**

| 项 | 值 |
|---|---|
| 状态 | 正常运行中 |
| 进度 | Step 2900 / 3000 (96.7%) |
| 预计剩余 | ~100 steps，几分钟内完成 |
| GPU | RTX PRO 6000 Blackwell, 97% util, 85.5 GB used |
| Registry | PREPARING → RUNNING (已修正) |
| 输出目录 | `/root/turn_residual_gating/runs/phase2_llama_lora_only_s42` |

训练即将结束，完成后需要检查 checkpoint 保存和提取最终指标。

---
