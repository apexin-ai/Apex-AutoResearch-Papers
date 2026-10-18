# diagnose eval pi05 random k095 object seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k095_object_seed43_20260521T235516_result.json`
- **Structured JSON:** [`2efb82b1f726d11f1cd0.json`](../../sessions/2e/2efb82b1f726d11f1cd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都**正常完成**了，没有任何失败。

**eval_pi05_random_k095_object_seed43**: 全部 10 个 task（T0-T9，每 task 50 episodes）跑完，最终结果 `libero_object prune=random keep=0.95 SR=72.8%`，结果已保存到 `pi05_random_k0.95_libero_object_seed43.json`。

**eval_pi05_random_k0925_object_seed42**: 同样全部完成，`libero_object prune=random keep=0.925 SR=27.6%`，结果已保存到 `pi05_random_k0.93_libero_object_seed42.json`。

监控系统报 "process dead 5× with no sentinel/W&B" 是**误报**——这两个 eval 脚本不会产生 sentinel 文件或 W&B log，所以监控的存活检测机制匹配不到信号，将正常运行的进程误判为 dead。日志路径也不在 `/root/runs/` 下（监控检查的位置），而是在 `/root/autodl-tmp/importance_margin_vla_compress/logs/`。

```json
{"root_cause":"监控系统在 /root/runs/ 下找不到日志且无 sentinel/W&B 信号，误判为 process dead。实际两个实验均正常完成（k095_seed43: SR=72.8%, k0925_seed42: SR=27.6%）","error_type":"infrastructure","fix_steps":["无需修复，实验已成功完成","更新监控系统的日志检测路径，加入 /root/autodl-tmp/importance_margin_vla_compress/logs/","或让 eval 脚本写 sentinel 文件到 /root/runs/ 下"],"can_auto_fix":false,"affects_k0925_too":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "监控系统在 /root/runs/ 下找不到日志且无 sentinel/W&B 信号，误判为 process dead。实际两个实验均正常完成（k095_seed43: SR=72.8%, k0925_seed42: SR=27.6%）",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，实验已成功完成",
      "更新监控系统的日志检测路径，加入 /root/autodl-tmp/importance_margin_vla_compress/logs/",
      "或让 eval 脚本写 sentinel 文件到 /root/runs/ 下"
    ],
    "can_auto_fix": false,
    "affects_k0925_too": true
  }
}
```

</details>

---
