# code prep plan017 launch

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_plan017_launch_20260515T144549_result.json`
- **Structured JSON:** [`d995cfcb947f558534ca.json`](../../sessions/d9/d995cfcb947f558534ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 008a 的实际 dt_emb 配置

008a 的日志和目录中没有保存 config.yaml，日志也没有打印 config。根据 008a 的启动命令（来自任务描述）和 `configs.yaml` 的 defaults：

| 参数 | 008a 命令行 | defaults 值 | 008a 实际使用 |
|------|------------|-------------|--------------|
| gate_dt_embed_dim | 未指定 | **32** | **32** (有 dt_emb) |
| dt_emb_freeze | 未指定 | **false** | **false** (trained) |
| imag_horizon | 未指定 | **15** | **15** |
| reward_dt_emb_detach | 未指定 | **false** | **false** |
| gate_enabled | True | false | True |
| gate_fixed_dt | 2 | 0 | 2 |
| gate_subsample_max_dt | 1 | 0 | 1 |

**017 vs 008a 差异：无。配置完全相同。**

017 计划的所有参数与 008a 的实际配置一一对应——两者都是 trained dt_emb (dim=32, no freeze) + subsample OFF (max_dt=1) + dt=2 imagination + H=15 + seed=1 + 105K steps。启动 017 等于重复 008a。

008a 已经跑完（metrics 到 step 112000，超过 105K 目标）。

---

### 2. 017 启动命令（如果仍要跑）

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_017_subsample_off_trained_dt_emb --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 15"
```

但因为与 008a 完全重复，建议确认是否需要换 seed 或修改其他参数来区分实验目的。

---

### 3. 009d baseline 进度

| 指标 | 值 |
|------|-----|
| 当前 step | **56000** / 105000 (53.3%) |
| 最新 eval (step 48000) | **eval_return = 293.2** |
| 最新 train_return (step 56000) | ~290-304 |
| FPS | ~7.4 |
| 预估剩余 | 49000 steps ÷ 7.4 fps ≈ **110 分钟 (~1.8h)** |

GPU 状态：
- GPU 0: 42% util, 4.2 / 97.9 GB（009d 在跑）
- GPU 1: 17% util, 2.8 / 97.9 GB（轻负载，可用于新实验）

---
