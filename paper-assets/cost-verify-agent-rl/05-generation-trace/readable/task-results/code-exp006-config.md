# code exp006 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006_config_20260513T232524_result.json`
- **Structured JSON:** [`24b26250c3d17e48a1ed.json`](../../sessions/24/24b26250c3d17e48a1ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

YAML 验证通过。Diff 确认只有 3 处差异：

```diff
< model_path: /root/cost-verify-agent-rl/models/Qwen3-1.7B
> model_path: /root/cost-verify-agent-rl/models/Qwen3-1.7B-Instruct

<   experiment_name: exp005-alfworld-fast
>   experiment_name: exp006-alfworld-instruct-fast

<   local_log_dir: "/root/autodl-tmp/checkpoints/exp_005/"
>   local_log_dir: "/root/autodl-tmp/checkpoints/exp_006/"
```

`_alfworld_exp006_instruct_fast.yaml` 已创建，保留 exp005 全部快速参数（30 steps, max_turn 30, 8 env_groups, group_size 8, 4096/1024/8192），模型切换为 Qwen3-1.7B-Instruct。

---
