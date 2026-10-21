# fix exp029 config and dryrun

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp029_config_and_dryrun_20260516T085157_result.json`
- **Structured JSON:** [`f10d864f77fdfcb62112.json`](../../sessions/f1/f10d864f77fdfcb62112.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**Dry-run 结果总结：**

| 检查项 | 状态 |
|--------|------|
| gpu_memory_utilization 0.92→0.5 | ��� 已修复 |
| max_model_len 16384→20480 | ✅ 已修复（解决首次 crash） |
| format chain 三方一致性 | ✅ 已验证，无冲突（alfworld_memory.py 不存在，实际格式链已一致） |
| val_before_train 完成 | ✅ 1275s，140 episodes |
| action_is_valid > 0 | ✅ 0.6635 (66.35%) |
| OOM | ✅ 无（峰值 52.7GB/97.9GB = 54%） |
| 训练步启动 | ✅ GPU cycling 0%/100%，rollout 生成中 |

Training step 0/1 仍在执行训练 rollout（elapsed 29 min），但所有关键检查已通过。

报告已写入：`artifacts/exp029_episode_level/intermediate/dryrun_report.md`

---
