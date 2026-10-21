# code 008f prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_008f_prep_20260514T041734_result.json`
- **Structured JSON:** [`ae13a2a6a2ff7d9d9567.json`](../../sessions/ae/ae13a2a6a2ff7d9d9567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 目录已清理。汇总如下：

---

## 汇总

### gate_dt_embed_dim=0 实现状态
**已存在，无需新增代码。** `networks.py` line 56-60:
- `dt_embed_dim > 0` → 创建 `nn.Embedding`
- `dt_embed_dim = 0` → `self._dt_embedding = None`，RSSM 输入不含 dt embedding，imagination 路径同样跳过

`configs.yaml` line 102: `gate_dt_embed_dim: 32`（默认值），命令行 `--gate_dt_embed_dim 0` 覆盖。

### Dry-run 结果
**通过。** 无报错，正常完成 seed collection、training (step 5000)、eval episode 生成。仅有 gym deprecation 和 torch.cuda.amp FutureWarning。

### 008f 完整提交命令
```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa
nohup python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk \
  --logdir logdir/exp_008f_no_dt_embed_h8 --steps 202000 --seed 1 --compile True \
  --device cuda:1 --gate_enabled True --gate_fixed_dt 2 \
  --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 \
  > /tmp/exp_008f.log 2>&1 &
```

### 008d 进度
- 当前 step: **45000**（step marker 已写，eval 和 model metrics 尚未写入）
- 最新 eval: **step 35000, eval_return = 146.34**
- 45K eval 数据还未产生

### 008a 进度
- 当前 step: **68000**
- 最新 eval: **step 65000, eval_return = 607.98**
- 65K 有完整数据，train_return 在 475-644 范围

---
