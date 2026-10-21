# diagnose eval pi05 random k0925 spatial seed42 unreg

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k0925_spatial_seed42_unreg_20260523T212744_result.json`
- **Structured JSON:** [`0f98b8aaa4f5c330668d.json`](../../sessions/0f/0f98b8aaa4f5c330668d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验实际已成功完成。结果：`overall_sr = 58.2%`，500 episodes，耗时 89 分钟。

问题不是实验失败，而是结果未上报到 W&B / sentinel 系统。由于该进程是"未注册进程"（unreg），没有日志重定向，所以没有 `.log` 文件，也没有 W&B tracking。

```json
{"root_cause":"实验已成功完成(SR=58.2%, 291/500)，结果已保存到 eval_results/pi05_random_k0.93_libero_spatial_seed42.json (May 24 04:33)。未注册进程没有配置 W&B logging 和 sentinel 文件写入，导致监控系统误判为失败。","error_type":"infrastructure","fix_steps":["无需重跑实验——结果文件已存在且完整","将 eval_results/pi05_random_k0.93_libero_spatial_seed42.json 中的 overall_sr=0.582 补录到实验追踪系统","未来启动实验时确保输出重定向到日志文件并注册到监控系统"],"can_auto_fix":true,"log_path":"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.93_libero_spatial_seed42.json"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "实验已成功完成(SR=58.2%, 291/500)，结果已保存到 eval_results/pi05_random_k0.93_libero_spatial_seed42.json (May 24 04:33)。未注册进程没有配置 W&B logging 和 sentinel 文件写入，导致监控系统误判为失败。",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需重跑实验——结果文件已存在且完整",
      "将 eval_results/pi05_random_k0.93_libero_spatial_seed42.json 中的 overall_sr=0.582 补录到实验追踪系统",
      "未来启动实验时确保输出重定向到日志文件并注册到监控系统"
    ],
    "can_auto_fix": true,
    "log_path": "/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.93_libero_spatial_seed42.json"
  }
}
```

</details>

---
