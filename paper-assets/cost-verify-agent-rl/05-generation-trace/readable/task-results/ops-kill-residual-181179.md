# ops kill residual 181179

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_residual_181179_20260525T054112_result.json`
- **Structured JSON:** [`913084eea802a914644b.json`](../../sessions/91/913084eea802a914644b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完毕。

**结果：**

1. **PID 181179**：清理前在运行（`python train.py --config-name _alfworld_factorial_h2_episode_adv_1gpu`，已运行 3h41m），现已终止
2. **PID 181166**：已不存在
3. **其他残留**：有 ~20 个 ray 子进程 + 1 个 rollout worker（PID 183394，占用 54.8GB 显存），均已清除
4. **执行了 kill**：是，首次 kill 命令生效但 SSH 返回中断，二次确认时进程已全部消失
5. **GPU cuda:0 最终状态**：**空闲** — 0MiB 显存占用，0% GPU-Util，34°C，无运行进程

---
