# code exp 007 fixed dt4 prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_007_fixed_dt4_prep_20260513T215242_result.json`
- **Structured JSON:** [`c54e0e32a6896cfbe472.json`](../../sessions/c5/c54e0e32a6896cfbe472.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Dry-run 结果

**通过**。启动无报错，成功到达训练循环（`[20]` step 打印后开始 evaluation）。CPU 上 evaluation 极慢所以未等到训练指标输出，但关键逻辑已通过代码审查确认。

### 2. 代码验证（gate_fixed_dt=4 逻辑）

| 模块 | 行为 | 验证 |
|------|------|------|
| **World Model 训练** (L188-190) | `effective_max_dt=4.0`，跳过 gate curriculum，`gate_scale=0` | OK |
| **训练子采样** (tools.py L788) | dt 从 log-uniform [1,4] 随机采样，world model 学多尺度转移 | OK |
| **Gate loss** (L245,314) | `gate_fixed_dt==0` 为 False → 不训练 gate 网络 | OK |
| **Imagination** (L547,562-564) | `gate_active=False`，每步 `next_dt=torch.full((B,), 4)` | OK → gate_dt_mean=4.0, std=0.0 |
| **Init dt** (L572-573) | `init_dt = ones * 4` | OK |
| **Lambda return** (L624) | `discount ** dts.float()` = `discount^4` | OK |
| **gate_max_dt=8** | dt=4 在范围 [1,8] 内 | OK |

### 3. 完整启动命令

```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4
```

### 4. 注意事项

- **dt=4 不超出 subsample 范围**：`gate_max_dt=8`，dt=4 合法。默认 `batch_length=64` 下，dt=4 子采样后最短序列 64/4=16 步，足够训练。
- **Gate 网络不训练**：`gate_fixed_dt>0` 时 gate loss 跳过，gate 网络参数冻结但仍占内存（可忽略）。
- **与 exp_006 (dt=2) 的对比**：唯一区别是 imagination 中 `discount^4` vs `discount^2`，有效 planning horizon 更长（每步跳 4 帧 vs 2 帧）。

---
