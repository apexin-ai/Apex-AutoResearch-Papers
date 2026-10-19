# diagnose v2 lora failures

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v2_lora_failures_20260516T155344_result.json`
- **Structured JSON:** [`5727af89ecd76077daa0.json`](../../sessions/57/5727af89ecd76077daa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：两个实验在 23:48-23:49 被同时 kill，是 tmux session 断开/SSH 连接中断导致的（spatial 收到 SIGHUP 确认了这点）。不是 OOM、CUDA error 或代码问题。

**状态**：
- universal_r16：停在 step 9300/10000，loss 0.6798，可从 step_9000 checkpoint 恢复（剩 ~17 min）
- spatial_r16：停在 step 6300/10000，loss 0.6840，可从 step_6000 checkpoint 恢复（剩 ~57 min）

**修复**：用 `nohup` 重启即可，两个都有完好的 checkpoint。

---
