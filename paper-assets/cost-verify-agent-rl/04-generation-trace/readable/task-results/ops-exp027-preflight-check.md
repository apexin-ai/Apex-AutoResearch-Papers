# ops exp027 preflight check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp027_preflight_check_20260515T142700_result.json`
- **Structured JSON:** [`b0badb69a01f4ad385a0.json`](../../sessions/b0/b0badb69a01f4ad385a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp027 Pre-flight Check Results

```
SCRIPT_EXISTS:        yes (/root/cost-verify-agent-rl/scripts/run_exp027_stable_grpo.sh)
CONFIG_EXISTS:        yes (/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp027_stable_grpo.yaml)

SCRIPT_PARAMS_CORRECT: PARTIAL — 详见下方
  env_groups (train):   8 ✓ (128 rollouts = 8×16)
  lr:                   5e-7 ✓
  kl_loss_coef:         0.005 ✓
  entropy_coeff:        0.01 ✓
  save_freq:            5 ✓
  total_training_steps: 50 ✓
  max_actor_ckpt_to_keep: 10 ✓
  logger:               ['console', 'wandb'] ✓
  val.env_groups:       16 ✓ (满足 C003 ≥16)
  CUDA_VISIBLE_DEVICES: 0,1 ✓ (满足 C001)
  ⚠️ 脚本头注释写 KL=0.04，实际 config 是 0.005（注释错误，不影响执行）

CHECKPOINT_EXISTS:    yes
  /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4
  → symlink → exp021_ragen_sft_v4/final/
  包含 model.safetensors + tokenizer 文件 ✓

STEP_INDEPENDENT:     yes (ctx_manager.py, agent_trainer.py, test 文件)

DISK_SPACE:           110GB available on /root/autodl-tmp/
  需要 ~35GB (10 ckpts × ~3.5GB) → 充足 ✓

GIT_HEAD:             N/A — /root/cost-verify-agent-rl 不是 git repo

WANDB_READY:          ❌ NO
  - wandb 包已安装 ✓
  - WANDB_API_KEY 未设置 ✗
  - ~/.netrc 不存在 ✗
  - ~/.config/wandb/ 不存在 ✗
  - 脚本未 source init_wandb.sh，也未 export WANDB_API_KEY
  - config 指定 logger 含 'wandb'，启动后会因认证失败而出错

PREFLIGHT: ❌ FAIL
```

**失败原因：W&B 未认证。** 服务器上无 `WANDB_API_KEY` 环境变量、无 `~/.netrc`、无 wandb config 目录。config 中 `logger: ['console', 'wandb']` 要求 W&B 可用，启动后会报错。

**修复方案：** 启动前在服务器上执行 `wandb login` 或在脚本中 `export WANDB_API_KEY=[REDACTED]

---
