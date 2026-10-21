# deploy exp 048 stackcube scout

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp_048_stackcube_scout_20260522T154525_result.json`
- **Structured JSON:** [`91532d40b86db28b8474.json`](../../sessions/91/91532d40b86db28b8474.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇报：

**ManiSkill 安装状态**: 已预装，mani_skill 3.0.1 + sapien 3.0.3 + gymnasium 1.3.0

**exp_048_stackcube_civo_trigger_s0 部署状态**:
- **PID**: 87609
- **GPU**: cuda:0 (RTX PRO 6000 Blackwell, 3408 MiB used, 26% util)
- **启动命令**: `python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_stackcube_civo_trigger_s0`
- **日志**: `/tmp/exp_048.log`

**初始日志确认**:
- StackCube-v1 环境创建成功，obs shape (1, 48), action space Box(8,)
- Prefill 完成 2500 steps (12 episodes)
- Encoder/Decoder: MLP only (state obs, 48 dims)
- 模型参数: model_opt 17M, actor_opt 1.1M, value_opt 1.2M
- 已完成首次 eval (eval_return 2.0) 并开始 training

---
