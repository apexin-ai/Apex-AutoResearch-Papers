# code exp027 config and script

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp027_config_and_script_20260515T140213_result.json`
- **Structured JSON:** [`034f259a2fbb21e48e17.json`](../../sessions/03/034f259a2fbb21e48e17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry run 通过，所有参数正确。

### 结果汇总

| 项目 | 详情 |
|------|------|
| **配置文件** | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp027_stable_grpo.yaml` |
| **启动脚本** | `/root/cost-verify-agent-rl/scripts/run_exp027_stable_grpo.sh` |
| **SFT checkpoint** | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/model.safetensors` (3.2GB, 确认存在) |
| **Dry run** | 通过 |

### exp026 → exp027 参数变更

| 参数 | exp026 | exp027 |
|------|--------|--------|
| LR | 1e-6 | **5e-7** |
| KL coef | 0.01 | **0.04** |
| entropy_coeff | 0.001 (base default) | **0.01** |
| save_freq | 25 | **5** |
| total_steps | 150 | **50** |
| W&B | enabled | enabled |

---
