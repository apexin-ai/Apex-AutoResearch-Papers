# diagnose sta phase1 r3 oom

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sta-phase1-r3-oom_20260513T202300_result.json`
- **Structured JSON:** [`59cb9fb601e7b6890f6b.json`](../../sessions/59/59cb9fb601e7b6890f6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。所有证据指向同一个根因。

```json
{"root_cause":"两个GRPO进程未设CUDA_VISIBLE_DEVICES，均加载到GPU 0（日志: 'We will use 90% of the memory on device 0'）。每个进程需要 model(~8GB) + ref_model(~8GB) + Adam优化器(~32GB) + 梯度(~8GB) + KV cache + 激活值，两进程共需 >120GB GPU显存，超出单卡97GB限制，导致显存溢出到系统内存后触发240GB cgroup限制被SIGKILL","error_type":"resource","fix_steps":["启动exec_only时设CUDA_VISIBLE_DEVICES=0，启动exec_sta时设CUDA_VISIBLE_DEVICES=1","或在训练脚本/launch wrapper中根据reward_mode自动分配GPU","可选：在configs中增加device字段，脚本启动时自动设CUDA_VISIBLE_DEVICES"],"can_auto_fix":true,"details":"证据链: (1) 两份r3日志均显示 'We will use 90% of the memory on device 0'，确认都在GPU 0; (2) grpo_exec_sta.yaml/grpo_exec_only.yaml均无device配置; (3) train_grpo.py docstring明确要求用CUDA_VISIBLE_DEVICES=0/1分离，但实际launch命令未设置; (4) step_time从10s增长到15.8s(step25)表明内存压力; (5) cgroup memory.max=240GB，oom_kill=0说明不是cgroup OOM——更可能是GPU显存耗尽后CUDA驱动级crash触发SIGKILL; (6) r2失败原因是wandb未登录(EXIT_CODE=1)，r3加了no_wandb修复了该问题但未解决GPU隔离; (7) 当前GPU空闲(0MiB/97887MiB×2)，系统内存充足(959GB available)"}
```

**三轮失败总结**:
- **r1 (EXIT_CODE=2)**: 可能是参数/脚本错误
- **r2 (EXIT_CODE=1)**: wandb 未登录 (`No API key configured`)
- **r3 (EXIT_CODE=137)**: 修复了 wandb 问题 (`no_wandb: true`)，但两进程仍共用 GPU 0，~4.5分钟后被 SIGKILL

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "两个GRPO进程未设CUDA_VISIBLE_DEVICES，均加载到GPU 0（日志: 'We will use 90% of the memory on device 0'）。每个进程需要 model(~8GB) + ref_model(~8GB) + Adam优化器(~32GB) + 梯度(~8GB) + KV cache + 激活值，两进程共需 >120GB GPU显存，超出单卡97GB限制，导致显存溢出到系统内存后触发240GB cgroup限制被SIGKILL",
    "error_type": "resource",
    "fix_steps": [
      "启动exec_only时设CUDA_VISIBLE_DEVICES=0，启动exec_sta时设CUDA_VISIBLE_DEVICES=1",
      "或在训练脚本/launch wrapper中根据reward_mode自动分配GPU",
      "可选：在configs中增加device字段，脚本启动时自动设CUDA_VISIBLE_DEVICES"
    ],
    "can_auto_fix": true,
    "details": "证据链: (1) 两份r3日志均显示 'We will use 90% of the memory on device 0'，确认都在GPU 0; (2) grpo_exec_sta.yaml/grpo_exec_only.yaml均无device配置; (3) train_grpo.py docstring明确要求用CUDA_VISIBLE_DEVICES=0/1分离，但实际launch命令未设置; (4) step_time从10s增长到15.8s(step25)表明内存压力; (5) cgroup memory.max=240GB，oom_kill=0说明不是cgroup OOM——更可能是GPU显存耗尽后CUDA驱动级crash触发SIGKILL; (6) r2失败原因是wandb未登录(EXIT_CODE=1)，r3加了no_wandb修复了该问题但未解决GPU隔离; (7) 当前GPU空闲(0MiB/97887MiB×2)，系统内存充足(959GB available)"
  }
}
```

</details>

---
