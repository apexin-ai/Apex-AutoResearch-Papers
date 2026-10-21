# code cheetah prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cheetah-prep_20260514T073012_result.json`
- **Structured JSON:** [`a45ca86e97e0e48bb945.json`](../../sessions/a4/a45ca86e97e0e48bb945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 结果汇总

### Cheetah Run 环境就绪状态
- ✅ dm_control `suite.load('cheetah', 'run')` 正常
- ✅ dreamer.py 支持 `--task dmc_cheetah_run`（命令行覆盖 configs.yaml 的 task 字段）
- ✅ `dmc_proprio` config 存在（proprio encoder/decoder, 500K steps, 4 envs, action_repeat=2）

### Dry-run 结果
- ✅ `--compile False` 时成功（环境创建→模型构建→训练循环→tfevents 输出）
- ❌ `--compile True`（默认）时崩溃 — PyTorch inductor `duplicate template name` bug
- **脚本需修复**：`cheetah_run_experiments.sh` 所有命令需加 `--compile False`

### 9 个 Config 参数对比

| 实验组 | 实验名 | gate_enabled | gate_fixed_dt | gate_subsample_max_dt | imag_horizon | gate_dt_embed_dim | steps | seeds |
|--------|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Baseline** | exp_baseline_cheetah_s{1,2,3} | False (default) | 0 (default) | 0 (default) | 15 (default) | 32 (default) | 512K | 1,2,3 |
| **008d** | exp_008d_cheetah_s{1,2,3} | **True** | **2** | **2** | **8** | 32 (default) | 105K | 1,2,3 |
| **008f** | exp_008f_cheetah_s{1,2,3} | **True** | **2** | **2** | **8** | **0** | 105K | 1,2,3 |

关键差异：
- **Baseline**：原版 DreamerV3，无 gate，H=15，跑满 512K steps
- **008d**：event gate 开启，固定 dt=2 + subsample，短 horizon H=8，有 dt embedding（dim=32）
- **008f**：同 008d 但**去掉 dt embedding**（dim=0），用于消融 dt embedding 的作用

### Baseline 训练命令（可直接用于提交）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_baseline_cheetah_s1 --steps 512000 --seed 1 --device cuda:0 --compile False
```

（s2/s3 改 `--seed 2/3` 和对应 logdir 即可）

---
