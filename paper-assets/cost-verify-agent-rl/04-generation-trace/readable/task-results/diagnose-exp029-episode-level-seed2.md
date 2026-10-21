# diagnose exp029 episode level seed2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_episode_level_seed2_20260518T054247_result.json`
- **Structured JSON:** [`1d0e7abfec3d5ca98f8f.json`](../../sessions/1d/1d0e7abfec3d5ca98f8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/exp029_episode_level_seed2/diagnose_report.md`。

**根因：CUDA OOM during `loss.backward()` at step 1**

核心发现：
- 崩溃位置：`dp_actor.py:468`，actor policy update 的反向传播
- seed 1 (train_seed=10000) 跑完了 16 步但最后也 OOM 退出，说明这套配置内存 headroom 本就很小
- seed 2 (train_seed=43) 的 step 1 rollout 恰好产生了更长序列，直接撑爆内存
- 磁盘（123G free）、Ray、代码均无问题，纯粹是 GPU 内存不足

**可重启，但需要调整**。直接重试可能再次 OOM。推荐方案 B（降低 `ppo_max_token_len_per_gpu`）或方案 D（迁移到 westd-47453 的 4 卡环境）。

---
