# diagnose eval pi05 attention k05 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_attention_k05_long_seed42_20260524T004322_result.json`
- **Structured JSON:** [`a4381a3cea000d3d03ca.json`](../../sessions/a4/a4381a3cea000d3d03ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个 attention 实验都已成功完成，监控系统误报。

```json
{"root_cause":"非失败——实验正常完成，日志末尾: RESULT: libero_10 prune=attention keep=0.5 SR=49.4%, 结果已保存至 pi05_attention_k0.50_libero_10_seed42.json","error_type":"infrastructure","fix_steps":["无需修复，实验已成功完成，SR=49.4%","监控系统误判为失败（process dead 5× with no sentinel/W&B），建议检查监控逻辑"],"can_auto_fix":false,"other_experiments_alive":false,"alive_details":"4个attention实验全部完成: goal_s43(06:53), spatial_s42(07:03), object_s42(07:23), long_s42(08:31)。当前仅1个tmux session有活跃进程: eval_pi05_random_k085_spatial_seed42_postfix (GPU 2, random k0.85 spatial)。其余tmux sessions (diag_read_goal_results, smolvla_spatial, xvla_long) 无活跃python进程，GPU 0/1/3空闲"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "非失败——实验正常完成，日志末尾: RESULT: libero_10 prune=attention keep=0.5 SR=49.4%, 结果已保存至 pi05_attention_k0.50_libero_10_seed42.json",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，实验已成功完成，SR=49.4%",
      "监控系统误判为失败（process dead 5× with no sentinel/W&B），建议检查监控逻辑"
    ],
    "can_auto_fix": false,
    "other_experiments_alive": false,
    "alive_details": "4个attention实验全部完成: goal_s43(06:53), spatial_s42(07:03), object_s42(07:23), long_s42(08:31)。当前仅1个tmux session有活跃进程: eval_pi05_random_k085_spatial_seed42_postfix (GPU 2, random k0.85 spatial)。其余tmux sessions (diag_read_goal_results, smolvla_spatial, xvla_long) 无活跃python进程，GPU 0/1/3空闲"
  }
}
```

</details>

---
