# deploy object seed43 doubling

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_object-seed43-doubling_20260515T115931_result.json`
- **Structured JSON:** [`14b79fbf2196373b3614.json`](../../sessions/14/14b79fbf2196373b3614.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

| 实验 | exp_id | 服务器 | GPU | PID | 状态 |
|------|--------|--------|-----|-----|------|
| obs_only seed=43 | `eval-obs-only-object-seed43` | bjb1-18228 | cuda:2 | 356490 | RUNNING |
| reconvla seed=43 | `eval-argmin-object-seed43` | bjb1-18228 | cuda:3 | 356696 | RUNNING |

命令格式与 bjb1-32546 上的 seed=42 object eval 一致（从 ps 输出确认），注意几个差异点：
- 脚本路径是 `src/evaluate.py`（非 `evaluate.py`）
- argmin baseline 实际 mode 名是 `reconvla`（非 `argmin`）
- 输出文件分别写入 `logs/eval_object_obs_only_seed43.json` 和 `logs/eval_object_reconvla_seed43.json`

---
