# eval exp029 seed2 ood step15

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp029_seed2_ood_step15_20260519T104607_result.json`
- **Structured JSON:** [`eba14d33055811686f7c.json`](../../sessions/eb/eba14d33055811686f7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

经过完整调查，情况如下：

**阻塞：seed2 checkpoint 已全部丢失，无法执行 OOD eval。**

详细情况：

1. **bjb1 上的 `/root/autodl-tmp/checkpoints/exp029/global_step_15/`** — 这是 **seed1** 的 checkpoint（日志确认 seed.train=10000, experiment_name=exp029-alfworld-episode-level），不是 seed2

2. **bjb1 上的 seed2 checkpoint** — seed2 曾在 bjb1 训练，保存路径为 `/root/autodl-tmp/checkpoints/exp029-seed2/`。Registry（`exp029_episode_level_seed2`）记录显示训练因磁盘满崩溃，step 15 checkpoint 一度存在，后被清理。**该目录现已不存在**

3. **westd 上的 seed2 checkpoint** — seed2 后来在 westd 上从 step 15 恢复训练至 step 30（`exp029_seed2_westd_resume`），但 westd 磁盘清理后**全部 checkpoint 已删除**

4. **之前 3 次 OOD eval 尝试**均失败（`exp029_seed2_ood_reeval`, `v3`, `v4` 在 westd 上；`exp029_seed2_ood_step15` 在 bjb1 上因 assertion error 失败但也指向了错误的 seed1 checkpoint）

**可选方案：**
- **A)** 从头重训 seed2（~16 GPU-hours，需要空闲 GPU）
- **B)** 用 seed1 的 step 15 checkpoint 替代（科学上不是 seed2，但训练配置完全相同只是 seed 不同）
- **C)** 论文中报告 seed2 OOD 数据不可用，只用 seed1 OOD 数据

请决定方向。

---
