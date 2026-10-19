# diagnose baseline spatial bowl s0 v2 baseline object pudding s0 v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_baseline_spatial_bowl_s0_v2_baseline_object_pudding_s0_v2_20260520T144744_result.json`
- **Structured JSON:** [`be6764edc05ec7a9a6cc.json`](../../sessions/be/be6764edc05ec7a9a6cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个实验都没有死亡，正在正常训练。**

当前状态：

| 实验 | PID | GPU | 当前 step | 速度 | 状态 |
|------|-----|-----|-----------|------|------|
| baseline_spatial_bowl_s0_v2 | 222903 | cuda:0, 100%, 35.7GB | 14160 | ~3.5s/it | **运行中** |
| baseline_object_pudding_s0_v2 | 222982 | cuda:2, 100%, 35.7GB | 16161 | ~3.5s/it | **运行中** |

- 磁盘 `/root/autodl-tmp`: 35% 使用 (121G/350G)，充足
- 日志无任何 Traceback / Error / OOM
- 两个进程都从正确的 checkpoint resume 了（spatial_bowl 从 14000, object_pudding 从 16000），已各自训练约 160 步

```json
{
  "baseline_spatial_bowl_s0_v2": {
    "root_cause": "进程未死亡，PID 222903 正在 GPU 0 上正常训练，当前 step=14160",
    "error_type": "none",
    "last_good_checkpoint_step": 14000,
    "fix_steps": ["无需修复，正在运行"],
    "can_auto_fix": true
  },
  "baseline_object_pudding_s0_v2": {
    "root_cause": "进程未死亡，PID 222982 正在 GPU 2 上正常训练，当前 step=16161",
    "error_type": "none",
    "last_good_checkpoint_step": 16000,
    "fix_steps": ["无需修复，正在运行"],
    "can_auto_fix": true
  },
  "common_cause": "两个实验均正常运行，不存在共同故障。可能之前查看时进程刚启动尚未出现在监控中，或查看了错误的 PID/时间点。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "baseline_spatial_bowl_s0_v2": {
      "root_cause": "进程未死亡，PID 222903 正在 GPU 0 上正常训练，当前 step=14160",
      "error_type": "none",
      "last_good_checkpoint_step": 14000,
      "fix_steps": [
        "无需修复，正在运行"
      ],
      "can_auto_fix": true
    },
    "baseline_object_pudding_s0_v2": {
      "root_cause": "进程未死亡，PID 222982 正在 GPU 2 上正常训练，当前 step=16161",
      "error_type": "none",
      "last_good_checkpoint_step": 16000,
      "fix_steps": [
        "无需修复，正在运行"
      ],
      "can_auto_fix": true
    },
    "common_cause": "两个实验均正常运行，不存在共同故障。可能之前查看时进程刚启动尚未出现在监控中，或查看了错误的 PID/时间点。"
  }
}
```

</details>

---
