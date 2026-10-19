# deploy pi05 precompute 2048

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-precompute-2048_20260522T201611_result.json`
- **Structured JSON:** [`df0a386a5c86bbe40632.json`](../../sessions/df/df0a386a5c86bbe40632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

**π0.5 2048D precompute — bjb1-18228 (4×4090)**

| GPU | Suite | Samples | PID | 状态 |
|-----|-------|---------|-----|------|
| 0 | object | 72,507 | 113455 | RUNNING |
| 1 | spatial | 60,250 | 113795 | RUNNING |
| 2 | goal | 61,728 | 114158 | RUNNING |
| 3 | long | (loading) | 114506 | RUNNING |

- obs_features 维度确认 **2048D**（Pi05Wrapper.VLM_HIDDEN_SIZE=2048）
- K=10, n_action_steps=10（Pi05Wrapper 默认值）
- Cache 写入 `/root/autodl-tmp/crm_cache_pi05_2048/{suite}/`
- 日志：`/root/autodl-tmp/logs/precompute_pi05_{suite}_2048.log`
- Registry：4 个实验已注册为 RUNNING
- 监控：每小时 :23 自动检查进度（cron job dc84a42c）

预计耗时 ~3-4h，long suite 最慢。

---
