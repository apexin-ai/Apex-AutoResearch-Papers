# diagnose sta phase1 exec sta r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sta-phase1-exec-sta-r2_20260513T195719_result.json`
- **Structured JSON:** [`999f716941311f89b9ce.json`](../../sessions/99/999f716941311f89b9ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

**两轮失败是不同原因：**

### 第一轮 (EXIT_CODE=2)：`--config` 参数解析失败
脚本接受了 `--config` 参数但没有正确加载 YAML 配置来填充必需参数（`--model_path`, `--data_path`, `--reward_mode`, `--output_dir`），导致 argparse 报错退出。这在第二轮之前已修复（第二轮成功通过了参数解析）。

### 第二轮 (EXIT_CODE=1)：wandb API key 未配置
脚本在 `train_grpo.py:211` 调用 `wandb.init()` 时崩溃：
```
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
```
两个配置文件都设了 `wandb_project: solver-trace-ablation` 且没有设 `no_wandb: true`，而服务器上没有 `WANDB_API_KEY` 环境变量。

### 次要问题
- vLLM 版本警告（0.18.1 vs TRL 支持的 0.11.0-0.17.1），目前只是 warning 不阻塞

```json
{
  "root_cause": "wandb.errors.errors.UsageError: No API key configured (train_grpo.py:211 wandb.init()). Round 1 was argparse failure due to --config not loading YAML into required args.",
  "error_type": "infrastructure",
  "fix_steps": [
    "方案A: 在服务器设置 WANDB_API_KEY 环境变量 (export WANDB_API_KEY=[REDACTED] 写入 ~/.bashrc)",
    "方案B: 在两个 YAML 配置中加 no_wandb: true 跳过 wandb 记录",
    "方案C: 训练启动命令加 --no_wandb 标志"
  ],
  "can_auto_fix": true,
  "affects_both_configs": true
}
```

需要我直接修复吗？最快的方式是在配置中加 `no_wandb: true`，或者你提供 WANDB_API_KEY 我写入服务器环境。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "wandb.errors.errors.UsageError: No API key configured (train_grpo.py:211 wandb.init()). Round 1 was argparse failure due to --config not loading YAML into required args.",
    "error_type": "infrastructure",
    "fix_steps": [
      "方案A: 在服务器设置 WANDB_API_KEY 环境变量 (export WANDB_API_KEY=[REDACTED] 写入 ~/.bashrc)",
      "方案B: 在两个 YAML 配置中加 no_wandb: true 跳过 wandb 记录",
      "方案C: 训练启动命令加 --no_wandb 标志"
    ],
    "can_auto_fix": true,
    "affects_both_configs": true
  }
}
```

</details>

---
