# fix registry spec commands

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_registry-spec-commands_20260517T150518_result.json`
- **Structured JSON:** [`50c9ec380c021c3c4eb6.json`](../../sessions/50/50c9ec380c021c3c4eb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

### 1. hsweep_h2_seed2 (bjb1-17606, PID 945877)
```
python train.py --config-name _alfworld_hsweep_h2 seed.train=20000 trainer.experiment_name=hsweep-h2-seed2
```

### 2. gae_baseline_seed1 (westd-47453, PID 40267)
```
python train.py --config-name _alfworld_reinforce_pp_baseline
```

### 3. gsweep_g050_h5_seed1 (westd-47453, PID 85798)
核心命令（从 watchdog wrapper 中提取）：
```
python train.py --config-name _alfworld_gamma_sweep_g050_h5 trainer.experiment_name=gsweep-g050-h5-seed1
```
环境变量：`CUDA_VISIBLE_DEVICES=2,3`, `TORCH_COMPILE_DISABLE=1`, 工作目录 `/root/cost-verify-agent-rl/RAGEN`

### gae_baseline_seed1 的 val episodes 数量
配置文件中 `val.env_groups: 32`, `val.group_size: 1`，即 **32 episodes**，满足 C003 (≥16) 要求。

---
